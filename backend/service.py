"""
Embody Backend Service

FastAPI service that provides design system exploration via Amplifier Foundation.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
import os
from dotenv import load_dotenv

from .session_manager import SessionManager, parse_llm_json

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Embody API",
    description="Amplifier-powered design system exploration",
    version="0.1.0"
)

# CORS configuration
cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:3456,http://127.0.0.1:3456").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize SessionManager
session_manager = SessionManager()


# Request/Response Models

class CreateSessionRequest(BaseModel):
    repo_path: str = Field(..., description="Path to repository with design tokens")


class CreateSessionResponse(BaseModel):
    session_id: str
    extracted_tokens: Dict[str, Any]
    created_at: str


class GatherContextRequest(BaseModel):
    goal: str = Field(..., description="Primary design goal")
    qualities: List[str] = Field(..., description="Desired design qualities")
    constraints: List[str] = Field(default_factory=list, description="Design constraints")


class FeedbackRequest(BaseModel):
    liked: List[str] = Field(default_factory=list, description="Liked concept IDs")
    disliked: List[str] = Field(default_factory=list, description="Disliked concept IDs")
    explored: List[str] = Field(default_factory=list, description="Explored concept IDs")


class FinalizeRequest(BaseModel):
    selected_concept_id: str = Field(..., description="ID of selected final concept")


# Endpoints

@app.get("/")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "embody-backend",
        "version": "0.1.0"
    }


@app.post("/api/sessions/create", response_model=CreateSessionResponse)
async def create_session(request: CreateSessionRequest):
    """
    Create new design exploration session
    
    - Loads embody profile
    - Initializes Amplifier session
    - Extracts design tokens from repository
    - Returns session ID and tokens
    """
    try:
        result = await session_manager.create_session(request.repo_path)
        return CreateSessionResponse(**result)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Session creation failed",
                "detail": str(e)
            }
        )


@app.post("/api/sessions/{session_id}/gather-context")
async def gather_context(session_id: str, request: GatherContextRequest):
    """
    Gather designer intent context
    
    Uses embody-collection:context-gatherer agent to:
    - Parse designer inputs
    - Infer implicit needs
    - Provide generation guidance
    """
    try:
        # Check session exists
        session = await session_manager.get_session(session_id)
        if not session:
            raise HTTPException(status_code=404, detail="Session not found")
        
        # Build instruction for context-gatherer agent
        instruction = f"""
Analyze the designer's intent from these inputs:

- Goal: {request.goal}
- Qualities: {", ".join(request.qualities)}
- Constraints: {", ".join(request.constraints) if request.constraints else "None"}

Return your analysis as JSON with:
1. parsed_intent (primary_goal, explicit_qualities, implicit_needs, constraints, design_focus)
2. generation_guidance (concept_count, diversity_level, emphasis, avoid)
"""
        
        # Execute agent
        response = await session_manager.execute_agent(
            session_id=session_id,
            agent="embody-collection:context-gatherer",
            instruction=instruction
        )
        
        # Parse response
        parsed_intent = parse_llm_json(response)
        
        # Update session state
        session_manager.update_session_state(session_id, {
            "context": {
                "goal": request.goal,
                "qualities": request.qualities,
                "constraints": request.constraints,
                "parsed_intent": parsed_intent
            },
            "phase": "concept_generation"
        })
        
        return {
            "parsed_intent": parsed_intent,
            "phase": "concept_generation"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Context gathering failed",
                "detail": str(e),
                "session_id": session_id
            }
        )


@app.post("/api/sessions/{session_id}/generate-concepts")
async def generate_concepts(session_id: str):
    """
    Generate initial design concepts
    
    Uses embody-collection:concept-generator agent to create 3-4 distinct
    design concepts based on parsed intent and current tokens.
    """
    try:
        # Check session exists
        session = await session_manager.get_session(session_id)
        if not session:
            raise HTTPException(status_code=404, detail="Session not found")
        
        # Load session state
        state = session_manager.get_session_state(session_id)
        
        # Build instruction for concept-generator agent
        instruction = f"""
Generate 3-4 distinct design concepts based on:

Current Tokens:
{state.get('extracted_tokens', {})}

Designer Intent:
{state.get('context', {}).get('parsed_intent', {})}

For each concept, provide:
- id, name, description
- qualities (list of defining characteristics)
- tokens (colors, typography, spacing, effects)
- rationale (why this fits the intent)
- accessibility (contrast ratios, WCAG level)

Return as JSON array of concepts.
"""
        
        # Execute agent
        response = await session_manager.execute_agent(
            session_id=session_id,
            agent="embody-collection:concept-generator",
            instruction=instruction
        )
        
        # Parse response
        result = parse_llm_json(response)
        concepts = result.get("concepts", result) if isinstance(result, dict) else result
        
        # Update session state with first iteration
        iterations = state.get("iterations", [])
        iterations.append({
            "round": 1,
            "concepts": concepts,
            "feedback": {},
            "timestamp": None
        })
        
        session_manager.update_session_state(session_id, {
            "iterations": iterations,
            "phase": "feedback"
        })
        
        return {
            "concepts": concepts,
            "round": 1,
            "phase": "feedback"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Concept generation failed",
                "detail": str(e),
                "session_id": session_id
            }
        )


@app.post("/api/sessions/{session_id}/refine")
async def refine_concepts(session_id: str, request: FeedbackRequest):
    """
    Refine concepts based on feedback
    
    Uses embody-collection:refinement-engine agent to evolve concepts
    based on designer feedback (liked/disliked/explored).
    """
    try:
        # Check session exists
        session = await session_manager.get_session(session_id)
        if not session:
            raise HTTPException(status_code=404, detail="Session not found")
        
        # Load session state
        state = session_manager.get_session_state(session_id)
        iterations = state.get("iterations", [])
        
        if not iterations:
            raise HTTPException(status_code=400, detail="No concepts to refine")
        
        current_round = len(iterations)
        previous_concepts = iterations[-1]["concepts"]
        
        # Build instruction for refinement-engine agent
        instruction = f"""
Refine concepts based on designer feedback:

Round: {current_round + 1}

Previous Concepts:
{previous_concepts}

Feedback:
- Liked: {request.liked}
- Disliked: {request.disliked}
- Explored: {request.explored}

Generate 2-3 refined concepts that:
1. Build on liked directions
2. Avoid disliked approaches
3. Blend promising elements

Return as JSON with:
- refinement_round
- learned_from_feedback
- approach
- concepts (array)
- confidence (0-1)
- next_round_guidance
"""
        
        # Execute agent
        response = await session_manager.execute_agent(
            session_id=session_id,
            agent="embody-collection:refinement-engine",
            instruction=instruction
        )
        
        # Parse response
        refined = parse_llm_json(response)
        
        # Update session state
        iterations.append({
            "round": current_round + 1,
            "concepts": refined.get("concepts", []),
            "feedback": {
                "liked": request.liked,
                "disliked": request.disliked,
                "explored": request.explored
            },
            "learned": refined.get("learned_from_feedback", ""),
            "confidence": refined.get("confidence", 0.0),
            "timestamp": None
        })
        
        # Check if ready for finalization
        phase = "finalization" if refined.get("confidence", 0.0) > 0.85 else "feedback"
        
        session_manager.update_session_state(session_id, {
            "iterations": iterations,
            "phase": phase
        })
        
        return {
            "concepts": refined.get("concepts", []),
            "round": current_round + 1,
            "learned": refined.get("learned_from_feedback", ""),
            "confidence": refined.get("confidence", 0.0),
            "phase": phase
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Refinement failed",
                "detail": str(e),
                "session_id": session_id
            }
        )


@app.post("/api/sessions/{session_id}/finalize")
async def finalize_direction(session_id: str, request: FinalizeRequest):
    """
    Finalize and document design direction
    
    Uses embody-collection:documentation-builder agent to create
    comprehensive documentation of the design journey.
    """
    try:
        # Check session exists
        session = await session_manager.get_session(session_id)
        if not session:
            raise HTTPException(status_code=404, detail="Session not found")
        
        # Load session state
        state = session_manager.get_session_state(session_id)
        
        # Build instruction for documentation-builder agent
        instruction = f"""
Create comprehensive documentation for this design journey:

Session State:
{state}

Selected Concept ID: {request.selected_concept_id}

Generate documentation that includes:
1. Starting point (extracted tokens, current feeling)
2. Design intent (goals, qualities, constraints)
3. Exploration journey (all rounds, feedback, learnings)
4. Final direction (selected concept details, rationale)
5. Engineering handoff (implementation phases, critical paths)
6. Success metrics

Return as JSON with:
- markdown (full documentation)
- final_direction (selected concept details)
- exports (figma_tokens, css_variables, tailwind_config)
"""
        
        # Execute agent
        response = await session_manager.execute_agent(
            session_id=session_id,
            agent="embody-collection:documentation-builder",
            instruction=instruction
        )
        
        # Parse response
        documentation = parse_llm_json(response)
        
        # Save markdown documentation to file
        from .foundation import get_session_dir
        session_dir = get_session_dir(session_id)
        doc_file = session_dir / "documentation.md"
        doc_file.write_text(documentation.get("markdown", ""), encoding="utf-8")
        
        # Update session state
        session_manager.update_session_state(session_id, {
            "phase": "completed",
            "selected_concept_id": request.selected_concept_id,
            "documentation": documentation
        })
        
        return {
            "documentation": documentation,
            "phase": "completed",
            "doc_file": str(doc_file)
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Finalization failed",
                "detail": str(e),
                "session_id": session_id
            }
        )


@app.get("/api/sessions/{session_id}")
async def get_session(session_id: str):
    """
    Get session state
    
    Returns current session state including:
    - Session metadata
    - Extracted tokens
    - Context and parsed intent
    - All iteration rounds
    - Current phase
    """
    try:
        # Load state from disk
        state = session_manager.get_session_state(session_id)
        return state
        
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Session not found")
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Failed to retrieve session",
                "detail": str(e),
                "session_id": session_id
            }
        )


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    host = os.getenv("HOST", "0.0.0.0")
    uvicorn.run(app, host=host, port=port)
