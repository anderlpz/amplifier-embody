"""
Session Manager

Manages Amplifier session lifecycle for design exploration.
"""

from pathlib import Path
from typing import Any, Dict, Optional
import uuid
import json
import re
from datetime import datetime, UTC

from .foundation import (
    load_embody_profile,
    extract_tokens_from_repo,
    save_session_state,
    load_session_state,
    get_session_dir,
)


class SessionManager:
    """Manages Amplifier session lifecycle for design exploration"""
    
    def __init__(self, sessions_dir: Path = Path(".embody/sessions")):
        self.sessions_dir = sessions_dir
        self.sessions_dir.mkdir(parents=True, exist_ok=True)
        self.active_sessions: Dict[str, Any] = {}  # session_id -> AmplifierSession
    
    async def create_session(self, repo_path: str) -> Dict[str, Any]:
        """
        Create new design exploration session
        
        Args:
            repo_path: Path to repository with design tokens
            
        Returns:
            {
                "session_id": str,
                "extracted_tokens": Dict[str, Any],
                "created_at": str (ISO timestamp)
            }
            
        Raises:
            ValueError: If profile loading or session initialization fails
        """
        from amplifier.session import AmplifierSession
        from amplifier.module_resolution import StandardModuleSourceResolver
        
        session_id = str(uuid.uuid4())
        
        # Load profile and compile to mount plan
        try:
            mount_plan = load_embody_profile()
        except Exception as e:
            raise ValueError(f"Failed to load embody profile: {e}")
        
        # Create AmplifierSession
        try:
            session = AmplifierSession(
                config=mount_plan,
                session_id=session_id
            )
        except Exception as e:
            raise ValueError(f"Failed to create AmplifierSession: {e}")
        
        # Mount module resolver for git sources
        try:
            resolver = StandardModuleSourceResolver(
                workspace_dir=Path(".embody/modules")
            )
            await session.coordinator.mount("module-source-resolver", resolver)
        except Exception as e:
            raise ValueError(f"Failed to mount module resolver: {e}")
        
        # Initialize session (downloads modules, mounts tools/providers)
        try:
            await session.initialize()
        except Exception as e:
            raise ValueError(f"Failed to initialize session: {e}")
        
        # Register session capabilities for task tool
        session.coordinator.register_capability("session.spawn", self._spawn_sub_session)
        session.coordinator.register_capability("session.resume", self._resume_sub_session)
        
        # Extract tokens from repository (non-blocking on failure)
        extracted_tokens = await extract_tokens_from_repo(repo_path)
        
        # Create initial session state
        state = {
            "session_id": session_id,
            "created_at": datetime.now(UTC).isoformat(),
            "updated_at": datetime.now(UTC).isoformat(),
            "repo_path": repo_path,
            "extracted_tokens": extracted_tokens,
            "profile": "default",
            "phase": "context_gathering",
            "context": {},
            "iterations": [],
            "documentation": {}
        }
        
        # Persist state
        try:
            save_session_state(session_id, state)
        except Exception as e:
            # Log but don't fail - keep in-memory state
            print(f"Warning: Failed to persist session state: {e}")
        
        # Store in active sessions
        self.active_sessions[session_id] = session
        
        return {
            "session_id": session_id,
            "extracted_tokens": extracted_tokens,
            "created_at": state["created_at"]
        }
    
    async def get_session(self, session_id: str) -> Optional[Any]:
        """
        Retrieve active AmplifierSession by ID
        
        Args:
            session_id: Session identifier
            
        Returns:
            AmplifierSession or None if not found
        """
        return self.active_sessions.get(session_id)
    
    def get_session_state(self, session_id: str) -> Dict[str, Any]:
        """
        Load session state from disk
        
        Args:
            session_id: Session identifier
            
        Returns:
            Session state dictionary
            
        Raises:
            FileNotFoundError: If session doesn't exist
            ValueError: If state is malformed
        """
        return load_session_state(session_id)
    
    def update_session_state(self, session_id: str, updates: Dict[str, Any]) -> None:
        """
        Update and persist session state
        
        Args:
            session_id: Session identifier
            updates: Dictionary with updates to merge into state
            
        Raises:
            FileNotFoundError: If session doesn't exist
        """
        # Load current state
        state = load_session_state(session_id)
        
        # Merge updates
        state.update(updates)
        
        # Update timestamp
        state["updated_at"] = datetime.now(UTC).isoformat()
        
        # Persist
        save_session_state(session_id, state)
    
    async def execute_agent(
        self,
        session_id: str,
        agent: str,
        instruction: str
    ) -> str:
        """
        Execute agent task using task tool
        
        Args:
            session_id: Session identifier
            agent: Agent name (e.g., "embody-collection:context-gatherer")
            instruction: Task instruction for agent
            
        Returns:
            Agent response content
            
        Raises:
            ValueError: If session not found or agent execution fails
        """
        session = await self.get_session(session_id)
        
        if not session:
            raise ValueError(f"Session not found: {session_id}")
        
        # Build prompt for agent execution via task tool
        prompt = f"""
Use the task tool to execute this agent task:

Agent: {agent}

Task:
{instruction}

Return the result in a structured format.
"""
        
        try:
            result = await session.execute(prompt)
            return result.content
        except Exception as e:
            raise ValueError(f"Agent execution failed: {e}")
    
    async def cleanup_session(self, session_id: str) -> None:
        """
        Clean up session resources
        
        Args:
            session_id: Session identifier
        """
        # Remove from active sessions
        if session_id in self.active_sessions:
            session = self.active_sessions[session_id]
            
            # Clean up session resources
            try:
                await session.cleanup()
            except Exception as e:
                print(f"Warning: Session cleanup failed: {e}")
            
            del self.active_sessions[session_id]
    
    # Helper methods for task tool capabilities
    
    async def _spawn_sub_session(self, *args, **kwargs):
        """Spawn sub-session for task tool"""
        # This would be implemented based on Amplifier Foundation's sub-session protocol
        # For now, placeholder
        pass
    
    async def _resume_sub_session(self, *args, **kwargs):
        """Resume sub-session for task tool"""
        # This would be implemented based on Amplifier Foundation's sub-session protocol
        # For now, placeholder
        pass


# Utility helper functions

def parse_llm_json(content: str) -> Dict[str, Any]:
    """
    Extract and parse JSON from LLM response
    
    Handles:
    - Raw JSON
    - JSON in markdown code blocks
    - JSON mixed with text
    
    Args:
        content: LLM response content
        
    Returns:
        Parsed JSON dictionary
        
    Raises:
        ValueError: If no valid JSON found
    """
    # Try to find JSON in markdown code block
    json_block_match = re.search(r'```(?:json)?\n(.*?)\n```', content, re.DOTALL)
    if json_block_match:
        json_str = json_block_match.group(1)
    else:
        # Try to find JSON object/array directly
        json_match = re.search(r'(\{.*\}|\[.*\])', content, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
        else:
            # Assume entire content is JSON
            json_str = content
    
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON from LLM response: {e}")
