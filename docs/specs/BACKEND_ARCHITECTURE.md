# Embody Backend Architecture

> **Foundation-powered backend for a design system generator**

**Project Name**: Embody  
**Version**: 1.0.0  
**Status**: Architecture Specification  
**Created**: December 17, 2025 at 14:44 PST  
**Built on**: [Amplifier Foundation](https://github.com/microsoft/amplifier-foundation)

---

## 🎯 Overview

Embody's backend uses **Amplifier Foundation** to power a **design system generator**. The product is the generator itself—a system that learns your design perspective and produces coherent design systems based on your encoded taste.

Unlike traditional generate-and-forget tools, Embody maintains **stateful sessions** where each feedback round tunes the generator to better understand and produce your aesthetic.

**Key Insight**: Embody is a **generator that learns taste** through a **collection-based agent system**:
- **Developer expertise** (zen-architect, modular-builder) for code understanding
- **Design intelligence** (design-system-architect, component-designer) for design thinking  
- **Foundation utilities** (foundation-explorer, researcher, session-finder) for discovery
- **Custom generator agents** (context-gatherer, concept-generator, refinement-engine) for training and tuning the generator

### Core Principles

1. **Generator-First**: The product is the generator that learns and produces taste
2. **Collection-Based**: Use existing Amplifier collections + Embody-specific generator agents
3. **Foundation-Native**: Use bundles, profiles, and agents as primary abstractions
4. **Stateful Learning**: Each session trains the generator to understand designer's aesthetic
5. **Cross-Domain**: Design + code + research agents work together to inform generation
6. **Composable**: Modules can be swapped, extended, or replaced
7. **Standalone First**: Web app initially, Amplifier module later

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    Frontend (Next.js)                        │
│   Context Wizard → Concept Gallery → Refinement Loop        │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTP REST API
┌────────────────────▼────────────────────────────────────────┐
│              Embody Backend (FastAPI)                        │
│                                                               │
│  ┌─────────────────────────────────────────────────────────┐│
│  │  API Layer (FastAPI Routes)                             ││
│  │  • POST /api/sessions/create     - Start new session   ││
│  │  • POST /api/sessions/{id}/gather-context              ││
│  │  • POST /api/sessions/{id}/generate-concepts           ││
│  │  • POST /api/sessions/{id}/refine                      ││
│  │  • GET  /api/sessions/{id}       - Get session state   ││
│  │  • POST /api/sessions/{id}/finalize                    ││
│  └─────────────────────────────────────────────────────────┘│
│                           ↓                                   │
│  ┌─────────────────────────────────────────────────────────┐│
│  │  Session Manager                                        ││
│  │  • Maintains AmplifierSession per user session         ││
│  │  • Tracks context, concepts, refinement history        ││
│  │  • Persists to ~/.embody/sessions/{session_id}/        ││
│  └─────────────────────────────────────────────────────────┘│
│                           ↓                                   │
│  ┌─────────────────────────────────────────────────────────┐│
│  │  Amplifier Foundation Integration                       ││
│  │                                                          ││
│  │  Profile Loader → Bundle Composition → Session Creation││
│  │       ↓                    ↓                    ↓        ││
│  │  Load embody.md    Compose modules    AmplifierSession ││
│  └─────────────────────────────────────────────────────────┘│
│                           ↓                                   │
│  ┌─────────────────────────────────────────────────────────┐│
│  │  Amplifier Collection Agents (via task tool)           ││
│  │                                                          ││
│  │  Developer Expertise:                                   ││
│  │  • developer-expertise:zen-architect - Code analysis   ││
│  │  • developer-expertise:modular-builder - Implementation││
│  │  • developer-expertise:researcher - Content research    ││
│  │                                                          ││
│  │  Design Intelligence:                                   ││
│  │  • design-intelligence:design-system-architect         ││
│  │  • design-intelligence:component-designer              ││
│  │  • design-intelligence:art-director                    ││
│  │                                                          ││
│  │  Foundation Utilities:                                  ││
│  │  • foundation:explorer - Codebase reconnaissance       ││
│  │  • foundation:session-finder - Past session search     ││
│  │                                                          ││
│  │  Embody-Specific (embody-collection):                  ││
│  │  • embody-collection:context-gatherer                  ││
│  │  • embody-collection:concept-generator                 ││
│  │  • embody-collection:refinement-engine                 ││
│  │  • embody-collection:documentation-builder             ││
│  └─────────────────────────────────────────────────────────┘│
│                           ↓                                   │
│  ┌─────────────────────────────────────────────────────────┐│
│  │  Foundation Modules                                     ││
│  │                                                          ││
│  │  • provider-anthropic:   Claude Sonnet 4               ││
│  │  • tool-task:           Agent delegation               ││
│  │  • tool-filesystem:     Extract tokens from repos      ││
│  │  • context-simple:      300K token context             ││
│  │  • loop-streaming:      Orchestrator with streaming    ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

---

## 📦 Bundle System

### Embody Profile Bundle

Located at `.embody/profiles/default.md`:

```yaml
---
profile:
  name: embody-default
  version: 1.0.0
  description: Design system exploration profile

session:
  orchestrator:
    module: loop-streaming
    source: git+https://github.com/microsoft/amplifier-module-loop-streaming@main
    config:
      extended_thinking: true
      stream_tokens: true
  
  context:
    module: context-simple
    source: git+https://github.com/microsoft/amplifier-module-context-simple@main
    config:
      max_tokens: 300000
      compact_threshold: 0.8

providers:
  - module: provider-anthropic
    source: git+https://github.com/microsoft/amplifier-module-provider-anthropic@main
    config:
      default_model: claude-sonnet-4-20250514

tools:
  - module: tool-filesystem
    source: git+https://github.com/microsoft/amplifier-module-tool-filesystem@main
  
  - module: tool-task
    source: git+https://github.com/microsoft/amplifier-module-tool-task@main

collections:
  # Amplifier collections (git sources)
  - name: developer-expertise
    source: git+https://github.com/microsoft/amplifier-collection-developer-expertise@main
  
  - name: design-intelligence
    source: git+https://github.com/microsoft/amplifier-collection-design-intelligence@main
  
  - name: foundation
    source: git+https://github.com/microsoft/amplifier-collection-foundation@main
  
  # Embody-specific collection (local)
  - name: embody-collection
    path: .embody/collections/embody

agents: all  # Load all agents from all collections
---

# Embody Generator Profile

This profile configures Claude Sonnet with design-focused agents for training
and running the design system generator.
```

---

## 🗂️ Collection Architecture

### Collection Structure

Embody uses **Amplifier Collections** - organized sets of agents that work together:

```
Collections Available to Embody:

1. developer-expertise (git)
   ├── zen-architect.md          # Code analysis & architecture
   ├── modular-builder.md         # Implementation
   ├── researcher.md              # Content research
   ├── bug-hunter.md              # Debugging
   └── integration-specialist.md  # API integration

2. design-intelligence (git)
   ├── design-system-architect.md # System-level design
   ├── component-designer.md      # Component-level design
   ├── art-director.md            # Aesthetic direction
   ├── layout-architect.md        # Page structure
   └── voice-strategist.md        # UX writing

3. foundation (git)
   ├── explorer.md                # Codebase reconnaissance
   ├── session-finder.md          # Past session search
   └── amplifier-explainer.md     # Framework explanation

4. embody-collection (local)
   ├── context-gatherer.md        # Parse designer perspective into generator constraints
   ├── concept-generator.md       # Generate design system variations
   ├── refinement-engine.md       # Train generator based on feedback
   └── documentation-builder.md   # Export system + generator state
```

### Why Collection-Based?

**Cross-Domain Intelligence for Generation**:
```
User: "Train a generator for my design aesthetic"

Embody Generator:
  1. Uses foundation:explorer to survey codebase (understand current state)
  2. Uses developer-expertise:zen-architect to analyze structure (technical context)
  3. Uses embody-collection:context-gatherer to define generator constraints
  4. Uses embody-collection:concept-generator to produce design system variations
  5. Uses embody-collection:refinement-engine to tune generator based on feedback
  6. Uses design-intelligence:component-designer to refine generated components
```

**Reusability**:
- Existing agents (zen-architect, researcher) work in Embody's generator without changes
- Embody's generator agents could be used in other design tools
- Collections are versioned and maintained independently
- The trained generator constraints are portable and reusable

**Modularity**:
- Swap collections without touching Embody code
- Add new collections as they're published
- Update agents via git pulls

---

## 📚 Embody Generator Collection Agents

These are the **new agents** specific to Embody's generator workflow—training and running a design system generator.

### 1. `context-gatherer.md`
Located at `.embody/collections/embody/agents/context-gatherer.md`:

```yaml
---
name: context-gatherer
role: Generator Constraint Parser
version: 1.0.0
---

# Context Gatherer Agent

You are an expert at translating designer perspective into generator constraints.

## Your Task

Given designer responses to context questions, extract the constraints that will guide the generator:
1. **Primary Goal**: What they're trying to achieve (generation direction)
2. **Desired Qualities**: Aesthetic characteristics that define their taste
3. **Hard Constraints**: Guardrails the generator must respect
4. **Implicit Preferences**: What they might not have said but is implied from their choices

## Input Format

You receive:
- `goal`: String selected from predefined options or custom input
- `qualities`: Array of selected qualities
- `constraints`: Optional array of constraints

## Output Format

Return JSON:
```json
{
  "parsed_intent": {
    "primary_goal": "Rebrand with modern feel",
    "explicit_qualities": ["bold", "modern", "accessible"],
    "implicit_needs": ["differentiation from competitors", "appeal to younger audience"],
    "constraints": ["maintain existing brand colors"],
    "design_focus": "visual_identity"  // or "consistency", "expansion", etc.
  },
  "generation_guidance": {
    "concept_count": 4,
    "diversity_level": "high",  // how different concepts should be
    "emphasis": ["color", "typography"],  // what to focus on
    "avoid": ["playful", "informal"]  // what to avoid based on constraints
  }
}
```

## Guidelines

- Be concise - this is parsed by code
- Infer implicit needs from explicit ones
- Suggest appropriate emphasis areas
- Flag conflicts (e.g., "bold" + "calm" is tension to explore)
```

### 2. `concept-generator.md`
Located at `.embody/collections/embody/agents/concept-generator.md`:

```yaml
---
name: concept-generator
role: Design System Variation Generator
version: 1.0.0
---

# Concept Generator Agent

You are the core generation engine that produces design system variations based on learned constraints.

## Your Task

Given:
- Current design tokens (extracted from codebase)
- Generator constraints (from context-gatherer)
- Learned preferences (from previous feedback rounds)

Produce 3-4 **distinct design system variations** that:
- Stay true to the defined constraints (the designer's encoded taste)
- Explore different interpretations within those constraints
- Maintain coherence (all variations feel like they came from the same perspective)

## Concept Structure

Each concept must include:

```json
{
  "id": "high-contrast-modernism",
  "name": "High Contrast Modernism",
  "description": "Bold black and white foundation with electric accents",
  "qualities": [
    "Strong visual hierarchy through contrast",
    "Modern sans-serif typography",
    "AAA accessibility compliance",
    "Electric blue accent for CTAs",
    "Spacious, uncluttered layouts"
  ],
  "tokens": {
    "colors": {
      "primary": "#000000",
      "secondary": "#FFFFFF",
      "accent": "#0066FF",
      "text": "#1A1A1A",
      "background": "#FFFFFF"
    },
    "typography": {
      "fontFamily": {
        "heading": "Inter, sans-serif",
        "body": "Inter, sans-serif"
      },
      "fontSize": {
        "base": "16px",
        "lg": "20px",
        "xl": "28px"
      }
    },
    "spacing": {
      "sm": "8px",
      "md": "16px",
      "lg": "32px"
    },
    "effects": {
      "shadows": {
        "sm": "0 2px 4px rgba(0,0,0,0.1)"
      },
      "borderRadius": {
        "md": "8px"
      }
    }
  },
  "rationale": "This approach maximizes impact through stark contrast...",
  "accessibility": {
    "contrastRatios": {
      "text_on_background": "16:1",
      "accent_on_background": "8.2:1"
    },
    "wcagLevel": "AAA"
  }
}
```

## Guidelines

1. **Diversity**: Each concept should explore a different approach
2. **Grounded**: Start from current tokens, evolve them
3. **Concrete**: Provide actual token values, not placeholders
4. **Justified**: Explain why this concept fits the intent
5. **Accessible**: Always check contrast ratios

## Diversity Strategies

If designer wants "bold + modern":
- Concept A: High contrast (black/white)
- Concept B: Bold colors (vibrant palette)
- Concept C: Bold typography (strong type hierarchy)
- Concept D: Bold geometry (sharp angles, grids)

Each explores "bold" differently while staying "modern".
```

### 3. `refinement-engine.md`
Located at `.embody/collections/embody/agents/refinement-engine.md`:

```yaml
---
name: refinement-engine
role: Generator Training Engine
version: 1.0.0
---

# Refinement Engine Agent

You tune the generator based on designer feedback, improving its ability to produce their aesthetic.

## Your Task

Given:
- Previously generated variations
- Designer feedback (👍 liked, 👎 disliked, 👁️ explored)
- Current generator state

**Train the generator** to better understand the designer's aesthetic:
1. **Learn from positive feedback**: What qualities resonated? Prioritize these in future generation
2. **Learn from negative feedback**: What qualities didn't work? Avoid these directions
3. **Refine constraints**: Update the generator's understanding of the designer's taste
4. **Produce refined variations**: Generate new outputs using the updated generator state

## Feedback Types

**Thumbs Up (👍)**:
- Designer likes this direction
- Generate 2-3 variations exploring this approach further
- Show: bolder version, softer version, applied to different contexts

**Thumbs Down (👎)**:
- Designer dislikes this direction
- Avoid similar approaches in future concepts
- Learn: What specific aspect didn't work?

**Details (👁️)**:
- Designer is curious but not committed
- Include one refined version in next round
- Blend with another liked concept

## Refinement Strategies

### Round 2 (After initial feedback)
If designer liked "High Contrast Modernism":
```json
{
  "refinement_approach": "variations_on_liked",
  "concepts": [
    {
      "name": "Even Bolder Contrast",
      "description": "Pure B&W with neon accents",
      "changes_from_original": "Removed grays, stronger accent colors"
    },
    {
      "name": "Softer Modernism", 
      "description": "High contrast with rounded edges",
      "changes_from_original": "Added border radius, friendlier feel"
    },
    {
      "name": "Color Emphasis",
      "description": "High contrast base with strategic color",
      "changes_from_original": "More accent colors for hierarchy"
    }
  ]
}
```

### Round 3 (Converging)
Designer liked "Color Emphasis" → Show it in different contexts:
```json
{
  "refinement_approach": "context_application",
  "concepts": [
    {
      "name": "Components View",
      "description": "Color Emphasis applied to UI components",
      "preview_type": "components",
      "components": ["button", "card", "input", "modal"]
    },
    {
      "name": "Layout View",
      "description": "Color Emphasis at page scale",
      "preview_type": "layouts",
      "layouts": ["dashboard", "marketing", "settings"]
    },
    {
      "name": "Documentation View",
      "description": "Color Emphasis as style guide",
      "preview_type": "documentation",
      "sections": ["colors", "typography", "spacing"]
    }
  ]
}
```

## Output Format

Always return:
```json
{
  "refinement_round": 2,
  "learned_from_feedback": "Designer likes high contrast but wants more color",
  "approach": "variations_on_liked",
  "concepts": [/* 2-3 refined concepts */],
  "confidence": 0.8,  // How close we think we are
  "next_round_guidance": "If designer likes Color Emphasis, show in real contexts"
}
```
```

### 4. `documentation-builder.md`
Located at `.embody/collections/embody/agents/documentation-builder.md`:

```yaml
---
name: documentation-builder
role: Generator Export & Documentation Agent
version: 1.0.0
---

# Documentation Builder Agent

You export the generated design system AND the trained generator constraints for future use.

## Your Task

Given:
- Session history (context, concepts, feedback, refinements)
- Final selected direction
- Trained generator state (learned constraints)

Create comprehensive exports:
1. **The Generated Design System**: Tokens, components, documentation, usage guidelines
2. **Generator Constraints**: The encoded perspective (for regeneration in new contexts)
3. **Journey Documentation**: How the generator learned this aesthetic
4. **Engineering Handoff**: Clear implementation steps with full context

## Output Format

```markdown
# Design Exploration: [Project Name]

**Date**: [ISO Date]  
**Designer**: [Name]  
**Session ID**: [UUID]

---

## 🎯 Starting Point

**Current State**:
- 47 design tokens extracted from codebase
- Current feeling: Corporate, formal, technical
- Used across 23 components

**Extracted Tokens**:
- Colors: 12 tokens (blues, grays, black/white)
- Typography: 8 tokens (Inter font family, 5 sizes)
- Spacing: 6 tokens (8px base scale)
- Effects: 5 tokens (subtle shadows, 8px border radius)
- Behaviors: 3 tokens (300ms transitions)

---

## 💭 Design Intent

**Primary Goal**: Rebrand with bold, modern feel

**Desired Qualities**:
- Bold: Strong, confident, attention-grabbing
- Modern: Contemporary, cutting-edge
- Accessible: WCAG AA minimum (AAA preferred)

**Constraints**:
- Must work across mobile and desktop
- Accessibility is non-negotiable

**Implicit Needs** (inferred):
- Differentiation from competitors (likely corporate/formal style)
- Appeal to younger, tech-savvy audience
- Maintain professionalism while adding energy

---

## 🔄 Exploration Journey

### Round 1: Initial Concepts (4 generated)

**Concept A: High Contrast Modernism**
- Bold B&W foundation + electric blue accent
- Designer feedback: 👍 Liked

**Concept B: Gradient Modern**
- Vibrant gradients, smooth transitions
- Designer feedback: 👎 Disliked ("too trendy, won't age well")

**Concept C: Geometric Bold**
- Sharp angles, grid system, modular
- Designer feedback: 👁️ Explored details

**Concept D: Bold Minimalism**
- Negative space, strong typography, limited palette
- Designer feedback: 👎 Disliked ("too minimal, lacks energy")

**Learning**: Designer wants boldness through contrast and color, not through minimalism or trends.

### Round 2: Refinement (3 variations)

Based on liked "High Contrast Modernism":

**Variation 1: Even Bolder**
- Pure B&W, neon accents
- Designer feedback: 👎 ("Too intense")

**Variation 2: Softer Edges**
- Same contrast, rounded corners
- Designer feedback: 👁️ ("Friendlier, but loses impact")

**Variation 3: Color Emphasis** ⭐
- High contrast base + strategic bold accent colors
- Designer feedback: 👍 ("This feels right!")

**Learning**: Balance between impact and approachability. Color used strategically, not everywhere.

### Round 3: Context Application

Showed "Color Emphasis" in three contexts:
- Components: Buttons, cards, inputs, modals
- Layouts: Dashboard, marketing page, settings
- Documentation: Color swatches, typography specimens, spacing scale

**Designer feedback**: ✅ "This is the direction. Let's document it."

---

## 🎨 Final Direction: Color Emphasis Modernism

### Overview
A bold, modern design system built on high-contrast foundations with strategic use of vibrant accent colors to create hierarchy and direct attention.

### Token Changes

**Colors**:
```diff
- primary: #1E3A8A (dark blue)
+ primary: #000000 (pure black - foundation)

- secondary: #64748B (gray)
+ secondary: #FFFFFF (pure white - foundation)

+ accent_primary: #0066FF (electric blue - CTAs)
+ accent_secondary: #FF3366 (vibrant pink - secondary actions)
+ accent_tertiary: #00CC88 (teal - success states)

- text: #1F2937 (dark gray)
+ text: #1A1A1A (near black - better contrast)
```

**Typography**:
```diff
  fontFamily: Inter (unchanged - already modern)
- fontSize.base: 16px
+ fontSize.base: 18px (better readability, more confident)

- fontWeight.medium: 500
+ fontWeight.medium: 600 (stronger hierarchy)
```

**Spacing**:
```diff
- Base scale: 8px
+ Base scale: 8px (unchanged, works well)

+ Added: xl (48px), 2xl (64px) for hero sections
```

**Effects**:
```diff
- shadows.sm: 0 1px 2px rgba(0,0,0,0.05)
+ shadows.sm: 0 2px 4px rgba(0,0,0,0.1) (more pronounced)

- borderRadius: 8px everywhere
+ borderRadius: 12px for cards, 8px for buttons (more nuance)
```

### Design Rationale

**Why this works**:
1. **High Contrast Foundation** (B&W) creates strong visual hierarchy without color
2. **Strategic Color Use** makes accents *mean something* - not decoration
3. **Accessibility First**: AAA contrast on text (16:1), AA on UI elements (8.2:1+)
4. **Scalable System**: Rules are clear, easy for engineers to extend
5. **Modern Without Trendy**: Won't feel dated in 2 years

**Emotional Impact**:
- Bold: Strong contrast, confident typography
- Modern: Clean, systematic, no unnecessary decoration
- Approachable: Rounded corners, vibrant (not harsh) accents

**Trade-offs Accepted**:
- Lost: Subtlety of original blue palette
- Gained: Clarity, impact, differentiation from competitors

---

## 🚀 Engineering Handoff

### Implementation Phases

**Phase 1: Foundation (Week 1)**
- Update color tokens to B&W base + 3 accent colors
- Update typography scale and weights
- Test contrast ratios across all components

**Phase 2: Component Updates (Weeks 2-3)**
- Update Button: Primary (accent_primary), Secondary (outline)
- Update Card: Stronger shadows, 12px radius
- Update Input: Focus states use accent_primary
- Update Modal: Hero sections use 2xl spacing

**Phase 3: Layout Applications (Week 4)**
- Dashboard: Accent colors for key metrics
- Marketing: Hero with bold typography
- Settings: Form structure with clear hierarchy

**Phase 4: Documentation & Testing (Week 5)**
- Generate style guide
- Accessibility audit
- Cross-browser/device testing

### Critical Paths

**Must maintain**:
- WCAG AA minimum on all interactive elements
- 16:1 contrast on body text
- Mobile responsiveness (320px+)

**Can iterate**:
- Exact accent color values (can tune hue/saturation)
- Border radius values (12px vs 10px vs 16px)
- Shadow intensity (can soften if needed)

### Questions for Engineering

1. Does our current CSS architecture support this level of token nesting?
2. Any components that can't support 18px base font size?
3. Performance impact of stronger shadows?
4. Dark mode: Invert or separate palette?

---

## 📊 Success Metrics

**Measure after launch**:
- Design QA: Visual consistency across pages (target: 95%+)
- Accessibility: Lighthouse score (target: 100 a11y)
- User Perception: "Bold and modern" sentiment (survey)
- Engineering: Implementation velocity vs old system

**Review in 3 months**:
- Are accent colors still feeling fresh?
- Is the system scaling to new features?
- Any accessibility issues reported?

---

## 🤝 Appendix

### All Concepts Explored

[Include thumbnails or descriptions of all 10 concepts generated across 3 rounds]

### Session Transcript

[Link to full JSON transcript in ~/.embody/sessions/{id}/transcript.json]

### Token Export

[Attached: Figma tokens, CSS variables, Tailwind config]

---

**Generated by Embody** • [Session ID]
```

## Guidelines

1. **Narrative Flow**: Read like a story, not a spec
2. **Preserve Decisions**: Show what was rejected and why
3. **Bridge Contexts**: Connect design thinking to engineering constraints
4. **Actionable**: Engineering team can start work immediately
5. **Referenceable**: Future designers understand the history
```

---

## 🔄 Generator Session Flow

### 1. Session Creation (Initialize Generator)

```python
# POST /api/sessions/create
async def create_session(repo_path: str) -> SessionResponse:
    """
    Create new Embody generator session
    
    Steps:
    1. Extract tokens from repository (background)
    2. Load embody profile
    3. Create AmplifierSession with profile mount plan
    4. Initialize session (downloads modules if needed)
    5. Return session_id for subsequent calls
    """
    # Load profile
    profile_loader = ProfileLoader([Path(".embody/profiles")])
    profile = profile_loader.load_profile("default")
    
    # Compile to mount plan with agent discovery
    agent_loader = AgentLoader(resolver=agent_resolver)
    mount_plan = compile_profile_to_mount_plan(
        profile,
        agent_loader=agent_loader
    )
    
    # Create session
    session = AmplifierSession(
        config=mount_plan,
        session_id=str(uuid.uuid4())
    )
    
    # Mount module resolver (for git sources)
    resolver = StandardModuleSourceResolver(
        workspace_dir=Path(".embody/modules")
    )
    await session.coordinator.mount("module-source-resolver", resolver)
    
    # Initialize (download + mount all modules)
    await session.initialize()
    
    # Register session capabilities for task tool
    session.coordinator.register_capability("session.spawn", spawn_sub_session)
    session.coordinator.register_capability("session.resume", resume_sub_session)
    
    # Extract tokens (async, non-blocking)
    extracted_tokens = await extract_tokens_from_repo(repo_path)
    
    # Store session state
    session_state = {
        "session_id": session.session_id,
        "created_at": datetime.now(UTC).isoformat(),
        "extracted_tokens": extracted_tokens,
        "profile": "default",
        "phase": "context_gathering",
        "history": []
    }
    
    return {"session_id": session.session_id, "tokens": extracted_tokens}
```

### 2. Define Generator Constraints

```python
# POST /api/sessions/{session_id}/gather-context
async def gather_context(
    session_id: str,
    goal: str,
    qualities: list[str],
    constraints: list[str] = []
) -> GeneratorConstraints:
    """
    Define generator constraints using embody-collection:context-gatherer agent
    
    Uses task tool to spawn agent from embody collection:
    - Translates designer perspective into generation constraints
    - Infers implicit aesthetic preferences
    - Initializes generator with these constraints
    """
    session = sessions[session_id]
    
    # Use task tool with collection:agent syntax
    result = await session.execute(f"""
    Use the task tool to analyze designer intent:
    
    Agent: embody-collection:context-gatherer
    
    Input:
    - Goal: {goal}
    - Qualities: {", ".join(qualities)}
    - Constraints: {", ".join(constraints)}
    
    Return the parsed intent and generation guidance.
    """)
    
    # Parse agent response
    parsed_intent = parse_llm_json(result.content)
    
    # Update session state
    session_state = load_session_state(session_id)
    session_state["context"] = {
        "goal": goal,
        "qualities": qualities,
        "constraints": constraints,
        "parsed_intent": parsed_intent
    }
    session_state["phase"] = "concept_generation"
    save_session_state(session_id, session_state)
    
    return parsed_intent
```

### 3. Generate Design System Variations

```python
# POST /api/sessions/{session_id}/generate-concepts
async def generate_concepts(session_id: str) -> list[DesignSystemVariation]:
    """
    Generate design system variations using the initialized generator
    
    The generator (concept-generator agent) produces variations based on:
    - Current tokens (from extraction)
    - Generator constraints (from context-gatherer)
    - Design system principles (from design-intelligence:design-system-architect)
    
    Each variation explores a different interpretation within the constraints
    """
    session = sessions[session_id]
    session_state = load_session_state(session_id)
    
    # First, optionally consult design-system-architect for foundation
    prompt = f"""
    Use the task tool to generate design concepts:
    
    Step 1: Consult design-intelligence:design-system-architect
    - Ask: "Given these tokens and intent, what design system principles should guide us?"
    - Tokens: {json.dumps(session_state["extracted_tokens"], indent=2)}
    - Intent: {json.dumps(session_state["context"]["parsed_intent"], indent=2)}
    
    Step 2: Use embody-collection:concept-generator
    - Generate 4 distinct concepts following the architect's guidance
    - Each concept should explore a different approach
    """
    
    # Stream response with progress updates
    concepts = []
    async for chunk in session.stream_execute(prompt):
        if chunk.type == "tool_use":
            # Track agent execution
            emit_progress_event(session_id, f"Generating concept {len(concepts)+1}")
        elif chunk.type == "content":
            # Accumulate response
            pass
    
    # Parse concepts from agent response
    result = parse_llm_json(final_content)
    concepts = result["concepts"]
    
    # Update session state
    session_state["iterations"].append({
        "round": 1,
        "concepts": concepts,
        "timestamp": datetime.now(UTC).isoformat()
    })
    session_state["phase"] = "feedback"
    save_session_state(session_id, session_state)
    
    return concepts
```

### 4. Train Generator (Refinement Loop)

```python
# POST /api/sessions/{session_id}/refine
async def refine_concepts(
    session_id: str,
    feedback: dict[str, list[str]]  # {"liked": [...], "disliked": [...]}
) -> list[DesignSystemVariation]:
    """
    Train the generator based on feedback
    
    The refinement-engine agent:
    1. Learns from feedback (what resonated vs what didn't)
    2. Updates generator constraints to better match designer's aesthetic
    3. Uses updated generator to produce refined variations
    
    May consult additional agents for deeper refinement:
    - design-intelligence:component-designer - Component-level details
    - design-intelligence:art-director - Aesthetic guidance
    """
    session = sessions[session_id]
    session_state = load_session_state(session_id)
    
    current_round = len(session_state["iterations"])
    previous_concepts = session_state["iterations"][-1]["concepts"]
    
    prompt = f"""
    Use the task tool to refine concepts:
    
    Agent: embody-collection:refinement-engine
    
    Round: {current_round + 1}
    Previous Concepts: {json.dumps(previous_concepts, indent=2)}
    Feedback: {json.dumps(feedback, indent=2)}
    
    If refinement needs component-level details:
    - Consult design-intelligence:component-designer
    
    If refinement needs aesthetic guidance:
    - Consult design-intelligence:art-director
    
    Generate refined concepts that build on what worked.
    """
    
    result = await session.execute(prompt)
    refined = parse_llm_json(result.content)
    
    # Update session state
    session_state["iterations"].append({
        "round": current_round + 1,
        "concepts": refined["concepts"],
        "feedback": feedback,
        "learned": refined["learned_from_feedback"],
        "confidence": refined["confidence"],
        "timestamp": datetime.now(UTC).isoformat()
    })
    
    # Check if converging
    if refined["confidence"] > 0.85:
        session_state["phase"] = "finalization"
    
    save_session_state(session_id, session_state)
    
    return refined["concepts"]
```

### 5. Export Generated System + Generator State

```python
# POST /api/sessions/{session_id}/finalize
async def finalize_direction(
    session_id: str,
    selected_concept_id: str
) -> GeneratorExport:
    """
    Export the generated design system + trained generator state
    
    Uses multiple agents for complete export:
    - embody-collection:documentation-builder - Export system + generator constraints
    - developer-expertise:zen-architect - Implementation guidance
    - design-intelligence:design-system-architect - Design system specification
    
    Returns:
    - Design system artifacts (tokens, components, docs)
    - Generator constraints (for regeneration in new contexts)
    - Journey documentation (the "why" behind the aesthetic)
    """
    session = sessions[session_id]
    session_state = load_session_state(session_id)
    
    prompt = f"""
    Use the task tool to document this design journey:
    
    Step 1: embody-collection:documentation-builder
    - Create narrative documentation of the exploration journey
    - Include: context, iterations, feedback, final direction
    
    Step 2: developer-expertise:zen-architect
    - Analyze implementation complexity
    - Suggest modular architecture for token system
    - Identify technical considerations
    
    Step 3: design-intelligence:design-system-architect
    - Generate design system specification
    - Document token structure, usage patterns
    - Provide accessibility guidelines
    
    Session: {json.dumps(session_state, indent=2)}
    Selected: {selected_concept_id}
    """
    
    result = await session.execute(prompt)
    documentation = parse_llm_json(result.content)
    
    # Export in multiple formats
    exports = {
        "markdown": documentation["markdown"],
        "figma_tokens": generate_figma_tokens(documentation["final_direction"]),
        "css_variables": generate_css_variables(documentation["final_direction"]),
        "tailwind_config": generate_tailwind_config(documentation["final_direction"])
    }
    
    # Save final documentation
    doc_path = Path(f".embody/sessions/{session_id}/documentation.md")
    doc_path.write_text(documentation["markdown"])
    
    session_state["phase"] = "completed"
    session_state["documentation"] = exports
    save_session_state(session_id, session_state)
    
    return documentation
```

---

## 🗂️ File Structure

```
embody/
├── backend/
│   ├── service.py                    # FastAPI service (main entry point)
│   ├── session_manager.py            # Session lifecycle management
│   ├── foundation_integration.py     # Amplifier Foundation wrapper
│   └── exporters/                    # Format exporters
│       ├── figma_tokens.py
│       ├── css_variables.py
│       └── tailwind_config.py
│
├── .embody/
│   ├── profiles/
│   │   └── default.md                # Embody profile bundle
│   │
│   ├── collections/                  # Amplifier collections
│   │   ├── embody/                   # Embody-specific collection
│   │   │   ├── collection.md         # Collection metadata
│   │   │   └── agents/
│   │   │       ├── context-gatherer.md
│   │   │       ├── concept-generator.md
│   │   │       ├── refinement-engine.md
│   │   │       └── documentation-builder.md
│   │   │
│   │   ├── developer-expertise/      # Downloaded from git
│   │   ├── design-intelligence/      # Downloaded from git
│   │   └── foundation/               # Downloaded from git
│   │
│   ├── modules/                      # Downloaded Foundation modules
│   │   └── [auto-populated by Foundation]
│   │
│   └── sessions/                     # Session persistence
│       └── {session_id}/
│           ├── state.json            # Session state
│           ├── transcript.json       # Full conversation
│           └── documentation.md      # Final output
│
├── app/                              # Next.js frontend
│   └── [existing structure]
│
└── pyproject.toml                    # Python dependencies
```

---

## 📦 Dependencies

### `pyproject.toml`

```toml
[project]
name = "embody-backend"
version = "0.1.0"
description = "Amplifier Foundation-powered design system exploration backend"
requires-python = ">=3.11"

dependencies = [
    "fastapi>=0.109.0",
    "uvicorn[standard]>=0.27.0",
    "amplifier-foundation @ git+https://github.com/microsoft/amplifier-foundation@main",
    "amplifier-core @ git+https://github.com/microsoft/amplifier-core@main",
    "amplifier-profiles @ git+https://github.com/microsoft/amplifier-profiles@main",
    "amplifier-module-resolution @ git+https://github.com/microsoft/amplifier-module-resolution@main",
    "pydantic>=2.0.0",
    "python-multipart>=0.0.6",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

---

## 🚀 Development Workflow

### Setup

```bash
# Install Python dependencies
cd backend
uv sync

# Create .embody structure
mkdir -p .embody/{profiles,agents,modules,sessions}

# Copy default profile
cp backend/embody-profile.md .embody/profiles/default.md

# Copy agents
cp backend/agents/*.md .embody/agents/

# Set API key
echo 'ANTHROPIC_API_KEY=sk-ant-...' > .env

# Start backend
uvicorn backend.service:app --reload --port 8000

# Start frontend (separate terminal)
cd app && pnpm dev
```

### First Request Flow

```bash
# 1. Create session (extracts tokens, loads profile)
curl -X POST http://localhost:8000/api/sessions/create \
  -H "Content-Type: application/json" \
  -d '{"repo_path": "/path/to/your/codebase"}'

# Returns: {"session_id": "abc-123", "tokens": {...}}

# 2. Gather context
curl -X POST http://localhost:8000/api/sessions/abc-123/gather-context \
  -H "Content-Type: application/json" \
  -d '{
    "goal": "Rebrand - more modern feel",
    "qualities": ["bold", "modern", "accessible"],
    "constraints": []
  }'

# Returns: {"parsed_intent": {...}, "generation_guidance": {...}}

# 3. Generate concepts (takes ~15s)
curl -X POST http://localhost:8000/api/sessions/abc-123/generate-concepts

# Returns: {"concepts": [{...}, {...}, {...}, {...}]}

# 4. Provide feedback
curl -X POST http://localhost:8000/api/sessions/abc-123/refine \
  -H "Content-Type: application/json" \
  -d '{
    "feedback": {
      "liked": ["concept-a"],
      "disliked": ["concept-c"]
    }
  }'

# Returns: {"concepts": [{...}, {...}, {...}]}

# 5. Finalize (when satisfied)
curl -X POST http://localhost:8000/api/sessions/abc-123/finalize \
  -H "Content-Type: application/json" \
  -d '{"selected_concept_id": "concept-a-variation-2"}'

# Returns: {"documentation": {...}, "exports": {...}}
```

---

## 🎯 Key Differences from amplifier-forge

| Aspect | amplifier-forge | Embody |
|--------|----------------|--------|
| **App Type** | Tauri desktop app | Web app (FastAPI + Next.js) |
| **Communication** | JSON-RPC over stdio | HTTP REST API |
| **Session Model** | Chat-like conversation | Iterative design refinement |
| **Agents** | General-purpose | Design-specialized |
| **State** | In-memory during session | Persisted across requests |
| **Output** | Code/files | Design documentation + exports |

### Why Not Tauri?

1. **Web-first**: Easier deployment, no installation
2. **Shareable**: Send link to session for team collaboration
3. **Embeddable**: Could become Amplifier module later
4. **Simpler**: No Rust build, no native permissions

### Why Similar Foundation Usage?

1. **Profile-based**: Same `.amplifier/profiles/` pattern
2. **Bundle composition**: Same module loading mechanism
3. **Agent delegation**: Same task tool pattern
4. **Stateful sessions**: Same AmplifierSession lifecycle

---

## 🔐 Security Considerations

### API Key Handling

```python
# backend/.env
ANTHROPIC_API_KEY=sk-ant-...

# Loaded at startup
load_dotenv()

# Never exposed to frontend
# Used only by Foundation modules
```

### Session Isolation

- Each session has unique ID
- Sessions stored in user's `.embody/sessions/`
- No cross-session data leakage
- Can be deleted after finalization

### Rate Limiting

```python
from slowapi import Limiter

limiter = Limiter(key_func=get_remote_address)

@app.post("/api/sessions/create")
@limiter.limit("5/minute")  # Max 5 sessions per minute
async def create_session(...):
    pass
```

---

## 🎓 Future: Amplifier Module

Eventually, Embody could become an Amplifier module:

```yaml
# .amplifier/profiles/my-profile.md
tools:
  - module: embody
    source: git+https://github.com/yourorg/amplifier-module-embody@main
    config:
      mode: embedded  # vs standalone
```

Then designers could use it directly in Amplifier CLI sessions:

```
You: "Let's explore design system directions for this codebase"

Amplifier: [Spawns embody agent] "I'll start by extracting your current 
           design tokens. What's your focus for this exploration?"

You: "Make it feel more modern and bold"

Amplifier: [Shows 4 concept previews] "Here are four directions..."
```

**Advantages**:
- No separate web app needed
- Works in any Amplifier session
- Can combine with other tools (task, bash, filesystem)
- Session history in Amplifier's transcript system

**Trade-offs**:
- Less visual UI (terminal-based)
- Requires Amplifier setup
- Not shareable via link (unless using Amplifier collaboration features)

---

## 🎁 Amplifier Contribution Strategy

**Core Principle**: Build for Amplifier from day one. Every component should be a potential contribution back to the Amplifier ecosystem.

### Contribution Candidates (Identified)

#### 1. `amplifier-module-design-tokens` (High Priority)

**Purpose**: Extract and convert design tokens from codebases

**Functionality**:
- Parse CSS, SCSS, Tailwind config, CSS-in-JS
- Extract colors, typography, spacing, effects, behaviors
- Convert between formats (Figma tokens, CSS variables, Tailwind config)
- Token analysis and classification

**Why Valuable to Amplifier**:
- Any Amplifier project needing design context benefits
- Standalone utility independent of Embody
- Useful for code analysis, documentation, migration

**Implementation Status**: Core extraction in Phase 1 (Week 1-2)  
**Contribution Timeline**: End of Phase 1 (Week 4)

**Location in Codebase**:
```
amplifier-embody/modules/design-tokens/
└── (extract to) amplifier-module-design-tokens/
```

---

#### 2. `embody-collection` (High Priority)

**Purpose**: Design intelligence agents for generation and refinement

**Agents**:
- `context-gatherer.md`: Parse design perspective into generator constraints
- `concept-generator.md`: Generate design system variations
- `refinement-engine.md`: Train generator based on feedback
- `documentation-builder.md`: Export systems with documentation

**Why Valuable to Amplifier**:
- Provides design intelligence for all Amplifier users
- Complements existing developer-expertise and design-intelligence collections
- Enables design-first workflows for non-designers

**Implementation Status**: Core agents in Phase 1 (Week 1-2)  
**Contribution Timeline**: End of Phase 1 (Week 4)

**Location in Codebase**:
```
amplifier-embody/.embody/collections/embody/
└── (extract to) amplifier-collection-embody/
```

---

#### 3. `amplifier-module-design-export` (Medium Priority)

**Purpose**: Export design systems to multiple formats

**Functionality**:
- Figma tokens JSON
- CSS variables
- Tailwind config
- Styled-components theme
- Chakra UI theme
- Design documentation generation

**Why Valuable to Amplifier**:
- Standard export utilities for design tooling
- Useful for any project generating design systems
- Format conversions between design tools

**Implementation Status**: Basic exports in Phase 1, enhanced in Phase 2  
**Contribution Timeline**: Phase 2 (Week 10)

**Location in Codebase**:
```
amplifier-embody/modules/design-export/
└── (extract to) amplifier-module-design-export/
```

---

#### 4. `amplifier-module-embody-ui` (Lower Priority)

**Purpose**: UI orchestration layer for design tools

**Functionality**:
- Session management UI patterns
- Concept gallery components
- Feedback collection interfaces
- Export/download flows

**Why Valuable to Amplifier**:
- Reusable UI patterns for design-focused Amplifier apps
- Could enable other design tools in ecosystem
- Standard UI components for design workflows

**Implementation Status**: Built throughout Phase 1-3  
**Contribution Timeline**: Phase 4 (Week 20) after validation

**Location in Codebase**:
```
amplifier-embody/app/ (extract reusable components)
└── (extract to) amplifier-module-embody-ui/
```

---

#### 5. `amplifier-collection-design-education` (Future)

**Purpose**: Educational agents that explain design principles

**Agents**:
- Design rationale explainer
- Accessibility guidance
- Best practice suggestions
- Design vocabulary builder

**Why Valuable to Amplifier**:
- Helps all users learn design while working
- Reduces need for design expertise
- Improves design literacy across ecosystem

**Implementation Status**: Phase 3  
**Contribution Timeline**: Phase 3 (Week 16)

---

### Component Architecture for Contribution

**Standalone Modules** (can work independently):
- `amplifier-module-design-tokens`: No Embody dependencies
- `amplifier-module-design-export`: Depends only on token format
- Both can be used in any Amplifier project

**Embody-Dependent** (require Embody context):
- `embody-collection`: Agents designed for generator workflow
- `amplifier-module-embody-ui`: UI components for Embody patterns

**However**: Even Embody-dependent components follow Amplifier patterns and could inform future features.

---

### Repository Structure for Contributions

**During Development** (all in `amplifier-embody`):
```
amplifier-embody/
├── .embody/collections/embody/          # embody-collection
├── backend/service.py                   # Embody-specific backend
├── app/                                 # Embody UI
└── modules/                             # Module development area
    ├── design-tokens/                   # develop here
    ├── design-export/                   # develop here
    └── embody-ui/                       # develop here
```

**After Extraction** (separate repositories):
```
amplifier-module-design-tokens/          # Standalone repo
├── README.md
├── pyproject.toml
├── src/design_tokens/
└── tests/

amplifier-collection-embody/             # Standalone repo
├── collection.md
├── agents/
│   ├── context-gatherer.md
│   ├── concept-generator.md
│   ├── refinement-engine.md
│   └── documentation-builder.md
└── README.md
```

**Embody References Official Modules**:
```yaml
# .embody/profiles/default.md (after contribution)
tools:
  - module: design-tokens
    source: git+https://github.com/microsoft/amplifier-module-design-tokens@main
  
  - module: design-export
    source: git+https://github.com/microsoft/amplifier-module-design-export@main

collections:
  - name: embody
    source: git+https://github.com/microsoft/amplifier-collection-embody@main
```

---

### Contribution Workflow

**For Each Module/Collection**:

1. **Develop in Embody**: Build and test within `amplifier-embody` repo
2. **Validate Thoroughly**: Use in production, dogfood with Amplifier team
3. **Extract to Standalone**: Move to separate repository with clean history
4. **Documentation**: Complete README, API docs, usage examples
5. **Testing**: Comprehensive test suite independent of Embody
6. **Follow Guidelines**: Amplifier contribution guidelines
7. **Submit PR**: To Amplifier ecosystem with rationale
8. **Iterate**: Address feedback, improve based on review
9. **Once Accepted**: Update Embody to use official module

---

### Testing Strategy for Contributions

**Each module must**:
- Work independently (no Embody dependencies unless stated)
- Have comprehensive test suite
- Include usage examples
- Pass Amplifier quality standards
- Be documented for non-Embody users

**Validation Checklist**:
- ✅ Works in isolation
- ✅ Clear API/interface
- ✅ Documented usage
- ✅ Test coverage > 80%
- ✅ Follows Amplifier patterns
- ✅ Valuable beyond Embody

---

## 🤝 Contributing

This architecture embodies Foundation best practices:
- **Bundle-based configuration**: Profiles, agents, modules
- **Stateful sessions**: AmplifierSession lifecycle
- **Agent delegation**: Task tool for specialized intelligence
- **Composable**: Swap modules, extend with new agents
- **Amplifier-ready**: Every component designed for potential contribution

**For detailed contribution process**:
See [CONTRIBUTING_TO_AMPLIFIER.md](../planning/CONTRIBUTING_TO_AMPLIFIER.md)

**Questions?**
- Foundation docs: https://github.com/microsoft/amplifier-foundation
- amplifier-forge reference: `/Users/alexlopez/Sites/OCTO/amplifier-forge`
- Contribution guidelines: [TBD - Amplifier contribution docs]

---

**Built with [Amplifier Foundation](https://github.com/microsoft/amplifier-foundation)** 🤖

*Every component designed to give back to the ecosystem that makes it possible.*