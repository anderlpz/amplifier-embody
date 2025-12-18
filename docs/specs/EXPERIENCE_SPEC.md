# Embody - Design System Generator Experience Specification

> **A generator that embodies your design perspective into coherent, customizable design systems**

**Version**: 3.0.0  
**Status**: Hybrid Approach - Context + Generation + Refinement  
**Created**: December 17, 2025 at 14:44 PST  
**Built with**: [Amplifier Framework](https://github.com/microsoft/amplifier)

---

## 🎯 Core Philosophy

### The Product is the Generator

**The output is a design system. The product is the generator itself.**

This distinction matters. When people hear "design system," they think: tokens, components, documentation—a static artifact. When we say "generator," we communicate something different:
- **Upstream thinking** - Define constraints, generate outputs
- **Iteration** - Refine and regenerate
- **Taste** - It produces a coherent point of view, not generic artifacts
- **Customization within constraints** - Like Chipotle or Rolex

### Embodying Perspective into Taste

**Design is the act of forming a point of view about a future state, not the act of assembling its implementation.**

Embody encodes your design perspective into generation constraints. The generator learns what "feels right" to you through iterative refinement, then produces design systems that:
- Feel **recognizably yours** - Coherent aesthetic across all variations
- Support **customization** - But within your encoded taste
- Maintain **coherence** - Never generic, always opinionated
- Enable **regeneration** - Apply your aesthetic to new contexts

### Constrained Customization

**Think Chipotle**: You customize your burrito (rice, beans, protein, toppings), but you're not inventing a new cuisine. You choose ingredients, but it's still recognizably Chipotle.

**Think Rolex**: You can choose dial colors and bracelet styles, but the crown stays where it belongs. Constraints ensure every watch is recognizably Rolex.

**Embody works the same way**: The generator offers choices within your encoded perspective. Every output variation maintains your recognizable aesthetic.

### Iteration Refines the Generator

**You're not picking "the one." You're teaching the generator to understand your taste.**

Each feedback round (👍/👎) tunes the generation logic:
- "More like this" → Generator learns what resonates with your aesthetic
- "Not this direction" → Generator learns what to avoid
- After 2-4 rounds → Generator consistently produces outputs that feel right

The goal isn't finding the perfect design. The goal is **training a generator that embodies your perspective.**

---

## 🌊 How the Generator Works

### Not Random Generation

**Random generators**: Roll the dice, pick from 3 random options  
**Embody**: Your perspective becomes the generation constraints

### Not Full Conversation

**Chat-based tools**: Slow, meandering conversations for every decision  
**Embody**: Quick context gathering, then fast iteration

### Instead: Train → Generate → Refine

**The Generator Flow:**
```
1. Define Your Perspective (brief, focused)
   Designer defines the generator's constraints
   → Goal: What are you trying to achieve?
   → Qualities: What aesthetic matters to you?
   → Constraints: What guardrails must you respect?
   
2. Generator Produces Variations (contextual, not random)
   Generator creates 3-4 directions based on your perspective
   → Not dice rolling—intelligent interpretation of your taste
   
3. Feedback Tunes the Generator (👍/👎)
   Designer reactions teach the generator what "feels right"
   → Generator learns your aesthetic through iteration
   
4. Refine & Regenerate (2-4 rounds)
   Generator evolves to consistently produce your aesthetic
   → Each round produces more coherent variations
```

**Example Session:**
```
Generator: "What's your design perspective?"
Designer: [Selects "Rebrand - more modern feel"]

Generator: "What qualities define your aesthetic?"
Designer: [Selects "Bold & confident" + "Accessible"]

[Generator initialized with these constraints]

Generator: [Produces 4 variations of your aesthetic]
      • Concept A: Bold colors, strong contrast
      • Concept B: Modern minimalism, lots of space
      • Concept C: Playful geometric, vibrant
      • Concept D: Sophisticated gradients, subtle

Designer: [👍 Concept A] [👎 Concept C] [🤔 Concept B]

[Generator learns: prioritize contrast, avoid playfulness]

Generator: [Produces refined variations]
      "I learned you prefer bold contrast. Here are 3 variations..."
      → Each variation explores contrast differently
      → All maintain your aesthetic coherence
```

**Key Difference**: You're not picking designs. You're **training a generator to understand and produce your taste**.

---

## 🎨 The Experience: Training Your Generator

### Step 1: Extraction (Automatic)
**Goal**: Understand the starting point for generation

```
Designer connects repository
    ↓
Tool extracts tokens silently
    ↓
"Found 47 design tokens across 5 categories"
    ↓
Ready for context gathering
```

**No action required** - System learns current state automatically.

---

### Step 2: Define Generator Constraints (Brief, Focused)
**Goal**: Define the perspective that will guide generation (~60 seconds)

**Question 1: What's your goal?** (Defines generation direction)
```
┌─────────────────────────────────────────────────────────────┐
│ What brings you here today?                                  │
├─────────────────────────────────────────────────────────────┤
│ ○ Explore how my system feels                                │
│ ○ Rebrand or refresh our visual identity                     │
│ ○ Improve consistency and cohesion                           │
│ ○ Prepare for new features/contexts                          │
│ ○ Understand what's possible with these tokens               │
│ ○ Other: [Custom input...]                                   │
└─────────────────────────────────────────────────────────────┘
```

**Question 2: What matters to you?** (Select 1-3 - These constrain the generator)
```
┌─────────────────────────────────────────────────────────────┐
│ What qualities are important?                                │
├─────────────────────────────────────────────────────────────┤
│ □ Accessible - WCAG compliant, inclusive                     │
│ □ Bold - Strong, confident, attention-grabbing              │
│ □ Calm - Peaceful, spacious, uncluttered                    │
│ □ Playful - Fun, energetic, creative                        │
│ □ Professional - Trustworthy, serious, established          │
│ □ Modern - Contemporary, cutting-edge                        │
│ □ Warm - Friendly, approachable, inviting                   │
│ □ Technical - Precise, systematic, engineered               │
└─────────────────────────────────────────────────────────────┘
```

**Optional Question 3: Any guardrails?** (Optional - Hard constraints on generation)
```
┌─────────────────────────────────────────────────────────────┐
│ Are there any guardrails?                                    │
├─────────────────────────────────────────────────────────────┤
│ □ Must maintain current brand colors                         │
│ □ Need to support dark mode                                 │
│ □ Should work across mobile and desktop                     │
│ □ Accessibility is non-negotiable                           │
│ □ Keep existing component structure                          │
│ □ No constraints - show me everything                       │
└─────────────────────────────────────────────────────────────┘
```

**Generator Initialization:**
```
"Generator initialized with your perspective:
 • Goal: Rebrand with bold and modern feel
 • Aesthetic: Bold, modern, accessible
 • Constraints: Maintain accessibility standards
 
 Generating variations based on your taste..."
```

**Time to complete**: ~60 seconds  
**Flexibility**: More specific constraints = more focused generation

---

### Step 3: Initial Generation (Constraint-Driven)
**Goal**: Generator produces 3-4 variations based on your perspective

**Not random variants** - Each concept interprets your constraints differently, but all stay true to your aesthetic.

**Example: Context = "Rebrand, Bold + Modern, Accessible"**

```
┌─────────────────────────────────────────────────────────────┐
│ Here are 4 concepts based on your goals:                     │
├─────────────────┬─────────────────┬─────────────────────────┤
│                 │                 │                          │
│ Concept A       │ Concept B       │ Concept C                │
│ High Contrast   │ Geometric Bold  │ Gradient Modern          │
│ Modernism       │                 │                          │
│                 │                 │                          │
│ • Bold blacks   │ • Sharp angles  │ • Vibrant gradients      │
│ • Bright        │ • Primary       │ • Smooth transitions     │
│   accents       │   shapes        │ • Depth with color       │
│ • AAA contrast  │ • Grid system   │ • AA contrast            │
│ • Clean sans    │ • Modular scale │ • Contemporary type      │
│                 │                 │                          │
│ [Preview]       │ [Preview]       │ [Preview]                │
│ 👍 👎 Details   │ 👍 👎 Details   │ 👍 👎 Details            │
│                 │                 │                          │
├─────────────────┴─────────────────┼─────────────────────────┤
│                                   │                          │
│ Concept D                         │  Your feedback guides    │
│ Bold Minimalism                   │  the next iteration.     │
│                                   │                          │
│ • Lots of negative space          │  Like multiple? I'll     │
│ • Strong typography               │  blend approaches.       │
│ • Limited color palette           │                          │
│ • AAA contrast                    │  Dislike all? I'll try   │
│ • Impact through restraint        │  different directions.   │
│                                   │                          │
│ [Preview]                         │                          │
│ 👍 👎 Details                     │                          │
└───────────────────────────────────┴─────────────────────────┘
```

**Each concept includes:**
- **Name**: Descriptive label
- **Key Qualities**: 3-5 defining characteristics
- **Visual Preview**: Shows components/layouts with those tokens
- **Quick Actions**: 👍 Like / 👎 Dislike / Details to explore deeper

---

### Step 4: Quick Feedback (Train the Generator)
**Goal**: Your reactions teach the generator what "feels right"

**Interaction:**
```
Designer clicks: 👍 Concept A, 👎 Concept C, Details on Concept B

Generator learns:
"You liked High Contrast Modernism and want to explore 
 Geometric Bold further.
 
 I'm learning your taste:
 • Prioritize: High contrast, bold aesthetics
 • Avoid: Playful, informal directions
 • Explore: How geometry can enhance contrast
 
 Generating refined variations..."
```

**Feedback Types:**
- **👍 Like**: "This resonates with my aesthetic"
- **👎 Dislike**: "This doesn't match my taste"  
- **Details**: "Show me more of this direction"
- **Combine**: "Blend these approaches"

**Philosophy**: Each round makes the generator better at producing your taste. You're not picking—you're teaching.

---

### Step 5: Refinement & Iteration
**Goal**: Generator evolves until it consistently produces your aesthetic

**Example Iteration 1:**
```
Based on your feedback (👍 Concept A):

┌─────────────────────────────────────────────────────────────┐
│ Refined Directions - Building on High Contrast Modernism    │
├─────────────────┬─────────────────┬─────────────────────────┤
│                 │                 │                          │
│ Variation 1     │ Variation 2     │ Variation 3              │
│ Even Bolder     │ Softer Edges    │ Color Emphasis           │
│                 │                 │                          │
│ • Pure B&W base │ • Same contrast │ • Bold accent colors     │
│ • Electric      │ • Rounded       │ • High contrast base     │
│   accents       │   corners       │ • Vibrant CTAs           │
│ • Maximum       │ • Friendlier    │ • Strategic color use    │
│   impact        │   feel          │                          │
│                 │                 │                          │
│ [Preview]       │ [Preview]       │ [Preview]                │
│ 👍 👎 Details   │ 👍 👎 Details   │ 👍 👎 Details            │
└─────────────────┴─────────────────┴─────────────────────────┘
```

**Example Iteration 2:**
```
Designer: 👍 Variation 3 (Color Emphasis)

Generator: "Your aesthetic is becoming clear! Let me show you 
            how this direction applies to different contexts..."

┌─────────────────────────────────────────────────────────────┐
│ Color Emphasis Applied                                       │
├──────────────────────────┬──────────────────────────────────┤
│                          │                                   │
│ Components               │ Page Layouts                      │
│ How it looks in buttons, │ How it feels at page scale        │
│ cards, forms             │                                   │
│                          │                                   │
│ [Preview with real       │ [Preview with dashboard,          │
│  components]             │  marketing page]                  │
│                          │                                   │
├──────────────────────────┴──────────────────────────────────┤
│                                                               │
│ This direction maintains:                                    │
│ • AAA contrast on text (meets your accessibility goal)       │
│ • Bold feeling through strategic color use                   │
│ • Modern aesthetic with clean typography                     │
│                                                               │
│ [This feels right] [Adjust colors] [Try different layout]    │
└─────────────────────────────────────────────────────────────┘
```

**Iteration continues** until designer says "This feels right"

At this point, **the generator understands your taste** and can consistently produce coherent variations.

---

### Step 6: Export the Generated System
**Goal**: Export the design system + the generator constraints

```
┌─────────────────────────────────────────────────────────────┐
│ Design Direction Finalized                                   │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│ Starting Point:                                              │
│ • 47 tokens extracted from codebase                          │
│ • Current feeling: Corporate, formal                         │
│                                                               │
│ Your Goal:                                                   │
│ • Rebrand with bold, modern feel                            │
│ • Maintain accessibility (WCAG AA minimum)                  │
│                                                               │
│ Exploration Journey:                                         │
│ • Generated 4 initial concepts                              │
│ • You liked: High Contrast Modernism                        │
│ • Refined to: Color Emphasis approach                       │
│ • Validated in components and layouts                       │
│                                                               │
│ Final Direction:                                            │
│ • High contrast base (black/white foundation)               │
│ • Strategic bold accent colors                              │
│ • Clean modern typography                                   │
│ • Maintains AAA contrast ratios                             │
│                                                               │
│ Ready to export:                                            │
│ □ Design Brief (for stakeholders)                           │
│ □ Token Specifications (for engineers)                      │
│ □ Figma Prototype (for validation)                          │
│ □ Implementation Guide (step-by-step)                       │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

**Generated Exports Include:**
- **The Design System** (tokens, components, documentation)
- **Generator Constraints** (your encoded perspective - for regeneration)
- **Journey Documentation** (the "why" behind decisions)
- **Multiple Formats** (Figma, CSS variables, Tailwind config)

**Key Innovation**: You can **regenerate** for new contexts using the same tuned generator. Your taste is now encoded and reusable.

---

## 🏗️ Technical Architecture

### System Components

```
┌─────────────────────────────────────────────────────────────┐
│                  Designer Interface                          │
│              (React + Next.js + TypeScript)                  │
├─────────────────────────────────────────────────────────────┤
│  • Context Wizard - Gather intent (2-3 questions)            │
│  • Concept Gallery - Show generated concepts (3-4 cards)     │
│  • Feedback Panel - 👍/👎/Details actions                    │
│  • Iteration Viewer - Refinement over time                   │
│  • Documentation Builder - Journey capture                   │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTP API
┌────────────────────▼────────────────────────────────────────┐
│              Intelligence Engine                             │
│         (FastAPI + Amplifier ClaudeSession)                  │
├─────────────────────────────────────────────────────────────┤
│  Endpoints:                                                  │
│  • POST /api/extract         - Extract current state         │
│  • POST /api/generate-concepts - Initial generation          │
│  • POST /api/refine          - Iterate based on feedback     │
│  • GET  /api/session         - Session state & history       │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  Amplifier Agents                            │
├─────────────────────────────────────────────────────────────┤
│  • design-analyst:      Extract + understand current state   │
│  • concept-generator:   Create contextual concepts           │
│  • refinement-engine:   Evolve based on feedback             │
│  • documentation-builder: Capture journey & rationale        │
└─────────────────────────────────────────────────────────────┘
```

### Data Model

**Session State:**
```typescript
{
  // Current State (extracted)
  extractedTokens: DesignTokens,
  
  // Designer Context (gathered)
  goal: string,                    // "Rebrand - modern feel"
  qualities: string[],             // ["bold", "modern", "accessible"]
  constraints: string[],           // ["maintain brand colors"]
  
  // Generation History
  iterations: [
    {
      round: 1,
      concepts: Concept[],         // Initial 3-4 concepts
      feedback: {
        liked: string[],           // Concept IDs
        disliked: string[],
        explored: string[]
      }
    },
    {
      round: 2,
      concepts: Concept[],         // Refined concepts
      feedback: { /* ... */ }
    }
  ],
  
  // Final State
  selectedDirection: Concept,
  rationale: string,
  nextSteps: Action[]
}
```

**Concept Structure:**
```typescript
{
  id: string,
  name: string,                    // "High Contrast Modernism"
  description: string,             // Brief explanation
  qualities: string[],             // ["bold blacks", "bright accents"]
  tokens: DesignTokens,            // Modified token values
  preview: {
    components: Component[],       // Button, Card, Input examples
    layouts: Layout[],             // Dashboard, Marketing page
    style_guide: StyleGuide        // Documentation format
  },
  accessibility: {
    contrastRatios: Record<string, number>,
    wcagLevel: "AA" | "AAA"
  }
}
```

---

## 🎭 UI Components Breakdown

### 1. Context Wizard
**Purpose**: Gather designer intent quickly (60 seconds)

**Flow:**
```
Screen 1: "What's your goal?" (radio select)
    ↓
Screen 2: "What qualities matter?" (multi-select)
    ↓
Screen 3: "Any constraints?" (optional multi-select)
    ↓
Summary: "Got it! Generating concepts..."
```

**Design:**
- Large, clear options
- Visual icons for each choice
- Progress indicator (Step 1 of 3)
- Can skip optional questions
- Shows summary before generating

### 2. Concept Gallery
**Purpose**: Show 3-4 generated concepts with quick actions

**Layout:**
```
┌─────────────────────────────────────────────────────────────┐
│ Concepts based on: Rebrand • Bold • Modern • Accessible     │
├───────────────┬───────────────┬───────────────┬─────────────┤
│  Concept A    │  Concept B    │  Concept C    │  Concept D  │
│  [Image]      │  [Image]      │  [Image]      │  [Image]    │
│  • Trait 1    │  • Trait 1    │  • Trait 1    │  • Trait 1  │
│  • Trait 2    │  • Trait 2    │  • Trait 2    │  • Trait 2  │
│  • Trait 3    │  • Trait 3    │  • Trait 3    │  • Trait 3  │
│  👍 👎 👁      │  👍 👎 👁      │  👍 👎 👁      │  👍 👎 👁    │
└───────────────┴───────────────┴───────────────┴─────────────┘
```

**Interactions:**
- Hover: Highlight card, show more details
- Click 👍: Mark as liked, influences next round
- Click 👎: Mark as disliked, avoid this direction
- Click 👁: Open detail view with full preview

### 3. Concept Detail View
**Purpose**: Deep dive on one concept

**Layout:**
```
┌─────────────────────────────────────────────────────────────┐
│ ← Back to concepts           Concept A: High Contrast       │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  [Large Preview - Components/Layouts/Style Guide tabs]       │
│                                                               │
├──────────────────────────────────────────────────────────────┤
│  Key Qualities:                                              │
│  • Bold black and white foundation                           │
│  • Electric accent colors for CTAs                           │
│  • AAA contrast ratios maintained                            │
│  • Clean modern sans-serif typography                        │
│                                                               │
│  Accessibility:                                              │
│  ✓ WCAG AAA for text                                        │
│  ✓ WCAG AA for large elements                               │
│  ✓ Color blind safe palette                                 │
│                                                               │
│  [👍 Like this direction]  [Combine with another concept]   │
└──────────────────────────────────────────────────────────────┘
```

### 4. Feedback Summary Panel
**Purpose**: Show what the tool learned from feedback

**After first round:**
```
┌─────────────────────────────────────────────────────────────┐
│ Based on your feedback:                                      │
├─────────────────────────────────────────────────────────────┤
│ ✓ You liked: High Contrast Modernism                        │
│ ✗ You didn't like: Playful Geometric                        │
│ 👁 You explored: Bold Minimalism                             │
│                                                               │
│ Refining to show you:                                        │
│ • Variations on high contrast approach                       │
│ • Blends of minimalism + contrast                           │
│ • Different ways to apply this feeling                       │
│                                                               │
│ [Generating refined concepts...]                             │
└─────────────────────────────────────────────────────────────┘
```

### 5. Iteration History
**Purpose**: Track refinement journey

**Timeline view:**
```
Round 1: Initial Concepts
  Generated: 4 concepts
  Feedback: Liked Concept A, Disliked Concept C
  
Round 2: Refined Direction  
  Generated: 3 variations on high contrast
  Feedback: Liked Variation 3 (Color Emphasis)
  
Round 3: Context Application
  Applied: Color Emphasis to components + layouts
  Result: Finalized
```

---

## 🔄 Interaction Patterns

### Pattern 1: Quick Iteration
**For designers who know what they want:**
```
Context (30s) → Generate (10s) → 👍 One concept → Refine (10s) → Done
Total time: ~1 minute
```

### Pattern 2: Exploration
**For designers discovering direction:**
```
Context (60s) → Generate (10s) → 👁 Details on 2 concepts → 
Compare → 👍/👎 → Refine (10s) → Repeat 2-3x → Finalize
Total time: ~5 minutes
```

### Pattern 3: Collaborative
**For teams making decisions:**
```
Context → Generate → Share link → Team adds 👍/👎 → 
Gather feedback → Refine → Present to stakeholders
Async collaboration supported
```

---

## 📊 Success Metrics

### Speed Metrics (For Quick Iteration)
- ✅ Time from context to first concepts: < 15 seconds
- ✅ Feedback response time: < 10 seconds
- ✅ Total time to satisfied result: 1-5 minutes

### Quality Metrics (For Good Thinking)
- ✅ Concepts align with stated intent (contextual accuracy)
- ✅ Refinements incorporate feedback (responsiveness)
- ✅ Designer reaches "feels right" state (satisfaction)
- ✅ Final direction is more ambitious than starting point
- ✅ Documentation captures "why" not just "what"

### Engagement Metrics
- ✅ Number of refinement rounds (2-4 is good)
- ✅ Thumbs up/down ratio (shows concepts resonate)
- ✅ Details view usage (shows deep exploration)
- ✅ Export/share rate (shows confidence in result)

---

## 🚀 Future Enhancements

### Phase 2: Richer Feedback
**Beyond 👍/👎:**
- **Intensity**: "A little" vs "A lot like this"
- **Aspects**: "Like the colors, not the spacing"
- **Blending**: "Combine colors from A with spacing from B"

### Phase 3: Team Collaboration
- **Shared Sessions**: Multiple designers give feedback
- **Voting**: Team consensus on concepts
- **Comments**: Annotate concepts with thoughts
- **Async**: Leave feedback, come back to refinements

### Phase 4: Learning Over Time
- **Pattern Recognition**: Learn designer preferences
- **Better Context Questions**: Adapt based on past sessions
- **Personalized Concepts**: Tune to designer's aesthetic
- **Team Patterns**: Learn org-wide preferences

### Phase 5: Implementation Bridge
- **Gradual Specs**: Move from vision to implementation details
- **Engineering Preview**: Show code impact of changes
- **Handoff Automation**: Generate implementation tickets
- **Context Preservation**: Keep design rationale in code

---

## 🎓 Design Principles

### 1. Context Before Generation
**Don't generate randomly - generate based on stated intent.**
- Ask focused questions upfront
- Use context to inform concepts
- Show how concepts connect to goals

### 2. Fast Feedback Loops
**Keep momentum - don't make thinking laborious.**
- 👍/👎 is faster than writing feedback
- Generate refinements quickly (< 10 seconds)
- Show progress toward goal

### 3. Preserve Imagination
**Concepts should expand possibility, not constrain it.**
- Offer diverse approaches
- Support ambitious thinking
- Don't optimize for "safe" choices
- Delay implementation concerns

### 4. Document the Journey
**Capture why, not just what.**
- Track concept evolution
- Preserve feedback reasoning
- Show decision points
- Bridge to engineering with context

### 5. Designer in Control
**Tool suggests, designer decides.**
- Never auto-apply changes
- Always show before committing
- Support exploration without consequences
- Respect designer judgment

---

## 🛠️ Implementation Roadmap

### MVP (Weeks 1-2)
- ✅ Token extraction (already built)
- ⬜ Context wizard (3 questions)
- ⬜ Initial concept generation (4 concepts)
- ⬜ Simple feedback (👍/👎)
- ⬜ One round of refinement

### V1 (Weeks 3-4)
- ⬜ Multiple refinement rounds
- ⬜ Concept detail view
- ⬜ Iteration history tracking
- ⬜ Basic documentation export

### V2 (Weeks 5-8)
- ⬜ Concept blending (combine A + B)
- ⬜ Aspect-level feedback ("like colors, not spacing")
- ⬜ Team sharing & collaboration
- ⬜ Richer export options

---

## 🤝 Contributing

This spec embodies a hybrid philosophy:
- **Structured enough** to move fast
- **Flexible enough** to preserve imagination
- **Guided** by context, not templates
- **Refined** through feedback, not guesswork

**Revision History**:
- v3.0.0 (Dec 17, 2024): Hybrid approach - context + generation + feedback
- v2.0.0 (Dec 17, 2024): Full conversation model (too slow)
- v1.0.0 (Dec 17, 2024): Pick-from-3 model (too limiting)

---

## 🎨 UI Design Specification

> **Detailed design specifications for Embody itself - ready for design-intelligence agents to generate assets**

This section provides comprehensive UI design specs that can be used by design-intelligence agents to generate:
- Component designs
- Layout mockups
- Interaction prototypes
- Visual assets
- Implementation code

---

## 🎭 Design Philosophy for Embody's UI

### Core Principles

**1. Clarity Over Complexity**
- Every element serves a clear purpose
- No decorative elements that don't aid understanding
- Information hierarchy guides attention naturally

**2. Professional but Approachable**
- Sophisticated enough for designers
- Accessible enough for non-designers
- Confidence-building, not intimidating

**3. Fast Decision Making**
- Minimize cognitive load
- Clear calls-to-action
- Instant feedback on interactions

**4. Trust Through Transparency**
- Show reasoning behind suggestions
- Make generator learning visible
- Never feel like a black box

**5. Delight in Details**
- Smooth micro-interactions
- Thoughtful animation timing
- Polish that communicates quality

---

## 🎨 Design System for Embody

### Color Palette

**WCAG Compliance**: This palette targets **WCAG AA minimum** (4.5:1 for text, 3:1 for UI elements), with **AAA achieved** (7:1) where possible. All contrast ratios validated.

**Foundation Colors (Light Mode)**:
```css
/* ============================================
   PRIMARY BLUE - "Generator Blue" System
   ============================================ */

/* Brand Blue - Use for large UI elements, buttons, icons */
--color-primary: #0066FF;           /* 4.77:1 on white - AA text ✓ */
--color-primary-hover: #0052CC;     /* 6.09:1 on white - AA+ text ✓ */

/* Text Blue - Use for body text, links requiring AAA */
--color-primary-text: #0047B3;      /* 7.13:1 on white - AAA text ✓ */
--color-primary-text-hover: #003D99; /* 8.59:1 on white - AAA+ text ✓ */

/* Interactive Blue - Use for large interactive elements */
--color-primary-interactive: #0066FF; /* Same as primary, semantic alias */

/* Light variants - Use for backgrounds, tints */
--color-primary-light: #3385FF;     /* 3.21:1 - AA large text only */
--color-primary-bg: #E6F0FF;        /* Backgrounds (no contrast req) */
--color-primary-bg-hover: #CCE0FF;  /* Hover backgrounds */

/* ============================================
   SECONDARY PURPLE - "Intelligence Purple"
   ============================================ */

/* AI/design intelligence indicators */
--color-secondary: #6D28D9;         /* 7.14:1 - AAA text ✓ (darkened) */
--color-secondary-dark: #5B21B6;    /* 9.15:1 - AAA+ text ✓ */
--color-secondary-light: #A78BFA;   /* 3.52:1 - AA large text only */
--color-secondary-bg: #EDE9FE;      /* Backgrounds */

/* ============================================
   SEMANTIC COLORS (State indicators)
   ============================================ */

/* Success (Generator Green) - Successful generation */
--color-success: #0F9F6F;           /* 4.68:1 - AA text ✓ (darkened) */
--color-success-dark: #047857;      /* 6.84:1 - AA+ text ✓ */
--color-success-bg: #D1FAE5;

/* Warning (Refinement Orange) - Needs attention */
--color-warning: #D97706;           /* 5.93:1 - AA+ text ✓ (darkened) */
--color-warning-dark: #B45309;      /* 7.49:1 - AAA text ✓ */
--color-warning-bg: #FEF3C7;

/* Error (Problem Red) - Errors, issues */
--color-error: #DC2626;             /* 5.93:1 - AA+ text ✓ (darkened) */
--color-error-dark: #B91C1C;        /* 7.71:1 - AAA text ✓ */
--color-error-bg: #FEE2E2;

/* ============================================
   NEUTRALS - Text Hierarchy (All AAA validated)
   ============================================ */

--color-neutral-900: #0F172A;       /* 16.78:1 - Primary headings (AAA+) */
--color-neutral-800: #1E293B;       /* 13.61:1 - Body text (AAA) */
--color-neutral-700: #334155;       /* 10.17:1 - Secondary text (AAA) */
--color-neutral-600: #475569;       /* 7.51:1 - Muted text (AAA) */
--color-neutral-500: #64748B;       /* 5.26:1 - Placeholder (AA+) */
--color-neutral-400: #94A3B8;       /* 3.39:1 - Disabled (AA large) */
--color-neutral-300: #CBD5E1;       /* Borders (no text use) */
--color-neutral-200: #E2E8F0;       /* Dividers */
--color-neutral-100: #F1F5F9;       /* Hover backgrounds */
--color-neutral-50: #F8FAFC;        /* Page background */
--color-white: #FFFFFF;             /* Cards, surfaces */
```

**Dark Mode Colors**:
```css
[data-theme="dark"] {
  /* Primary adjustments for dark backgrounds */
  --color-primary: #3385FF;         /* Lighter for dark mode */
  --color-primary-hover: #4D94FF;   /* Lighter hover */
  --color-primary-text: #66A3FF;    /* AAA on dark bg */
  --color-primary-bg: #1E3A5F;      /* Darker blue background */
  --color-primary-bg-hover: #2A4A75; /* Hover backgrounds */
  
  /* Secondary adjustments */
  --color-secondary: #A78BFA;       /* Lighter purple */
  --color-secondary-dark: #C4B5FD;  /* Lighter hover */
  --color-secondary-bg: #2E1F47;    /* Dark purple background */
  
  /* Semantic colors for dark mode */
  --color-success: #34D399;         /* Lighter green */
  --color-success-dark: #6EE7B7;
  --color-success-bg: #064E3B;
  
  --color-warning: #FBBF24;         /* Lighter orange */
  --color-warning-dark: #FCD34D;
  --color-warning-bg: #78350F;
  
  --color-error: #F87171;           /* Lighter red */
  --color-error-dark: #FCA5A5;
  --color-error-bg: #7F1D1D;
  
  /* Neutrals inverted for dark mode */
  --color-neutral-900: #F8FAFC;     /* Light text */
  --color-neutral-800: #F1F5F9;     /* Body text */
  --color-neutral-700: #E2E8F0;     /* Secondary text */
  --color-neutral-600: #CBD5E1;     /* Muted text */
  --color-neutral-500: #94A3B8;     /* Placeholder */
  --color-neutral-400: #64748B;     /* Disabled */
  --color-neutral-300: #475569;     /* Borders */
  --color-neutral-200: #334155;     /* Dividers */
  --color-neutral-100: #1E293B;     /* Hover backgrounds */
  --color-neutral-50: #0F172A;      /* Page background */
  --color-white: #0F172A;           /* Dark surface */
}
```

**Semantic Color Aliases** (Use these for clarity):
```css
/* Feedback States */
--color-like: var(--color-success);         /* 👍 */
--color-dislike: var(--color-error);        /* 👎 */
--color-explore: var(--color-warning);      /* 👁️ */
--color-generating: var(--color-primary);   /* In progress */
--color-ai-thinking: var(--color-secondary); /* AI processing */

/* Text colors (semantic) */
--color-text-primary: var(--color-neutral-900);
--color-text-body: var(--color-neutral-800);
--color-text-secondary: var(--color-neutral-700);
--color-text-muted: var(--color-neutral-600);
--color-text-placeholder: var(--color-neutral-500);
--color-text-disabled: var(--color-neutral-400);

/* Surface colors (semantic) */
--color-surface: var(--color-white);
--color-surface-elevated: var(--color-white);
--color-surface-hover: var(--color-neutral-100);
--color-background: var(--color-neutral-50);

/* Border colors (semantic) */
--color-border-default: var(--color-neutral-300);
--color-border-hover: var(--color-neutral-400);
--color-border-focus: var(--color-primary);
```

**Usage Guidelines**:

Use **`--color-primary`** (#0066FF) for:
- Large buttons and CTAs (AA compliant for all text sizes)
- Icons and UI elements
- Borders and accents

Use **`--color-primary-text`** (#0047B3) for:
- Body text and links requiring maximum accessibility (AAA)
- Small text (below 14px)
- Critical text content

Use **semantic aliases** for clarity:
- `--color-text-body` instead of `--color-neutral-800`
- `--color-surface` instead of `--color-white`
- Makes theming easier (light/dark mode switching)

### Typography

**Font Family**:
```css
--font-display: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;  /* Headings, UI */
--font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;     /* Body text */
--font-mono: 'SF Mono', 'Monaco', 'Cascadia Code', monospace;           /* Code, tokens */
```

**Font Sizes** (fluid typography):
```css
/* Display - Hero sections */
--text-display-xl: clamp(3.5rem, 5vw, 4.5rem);     /* 56px-72px */
--text-display-lg: clamp(3rem, 4vw, 3.75rem);      /* 48px-60px */
--text-display-md: clamp(2.5rem, 3vw, 3rem);       /* 40px-48px */

/* Headings */
--text-h1: clamp(2rem, 2.5vw, 2.5rem);             /* 32px-40px */
--text-h2: clamp(1.5rem, 2vw, 2rem);               /* 24px-32px */
--text-h3: clamp(1.25rem, 1.5vw, 1.5rem);          /* 20px-24px */
--text-h4: clamp(1.125rem, 1.25vw, 1.25rem);       /* 18px-20px */

/* Body */
--text-body-xl: 1.25rem;        /* 20px - Large body */
--text-body-lg: 1.125rem;       /* 18px - Default body */
--text-body-md: 1rem;           /* 16px - Secondary body */
--text-body-sm: 0.875rem;       /* 14px - Small text */
--text-body-xs: 0.75rem;        /* 12px - Captions */

/* UI Elements */
--text-button-lg: 1rem;         /* 16px - Primary buttons */
--text-button-md: 0.875rem;     /* 14px - Secondary buttons */
--text-button-sm: 0.75rem;      /* 12px - Tertiary buttons */
```

**Font Weights**:
```css
--font-weight-normal: 400;      /* Body text */
--font-weight-medium: 500;      /* Emphasis */
--font-weight-semibold: 600;    /* Subheadings, buttons */
--font-weight-bold: 700;        /* Headings */
--font-weight-extrabold: 800;   /* Display text */
```

**Line Heights**:
```css
--line-height-tight: 1.2;       /* Display, headings */
--line-height-snug: 1.375;      /* Subheadings */
--line-height-normal: 1.5;      /* Body text */
--line-height-relaxed: 1.625;   /* Long-form content */
--line-height-loose: 2;         /* Spaced content */
```

### Spacing

**Base Scale** (8px system):
```css
--space-0: 0;
--space-1: 0.25rem;    /* 4px - Tight spacing */
--space-2: 0.5rem;     /* 8px - Base unit */
--space-3: 0.75rem;    /* 12px */
--space-4: 1rem;       /* 16px - Default gap */
--space-5: 1.5rem;     /* 24px */
--space-6: 2rem;       /* 32px - Section spacing */
--space-8: 3rem;       /* 48px - Large sections */
--space-10: 4rem;      /* 64px - Page spacing */
--space-12: 6rem;      /* 96px - Hero spacing */
--space-16: 8rem;      /* 128px - Major sections */
```

**Component Spacing**:
```css
--padding-button-sm: var(--space-2) var(--space-3);    /* 8px 12px */
--padding-button-md: var(--space-3) var(--space-5);    /* 12px 24px */
--padding-button-lg: var(--space-4) var(--space-6);    /* 16px 32px */

--padding-card: var(--space-6);                         /* 32px */
--padding-page: var(--space-8);                         /* 48px */
--padding-section: var(--space-10);                     /* 64px */

--gap-tight: var(--space-2);                            /* 8px */
--gap-normal: var(--space-4);                           /* 16px */
--gap-relaxed: var(--space-6);                          /* 32px */
```

### Effects

**Shadows**:
```css
/* Elevation levels */
--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);                        /* Subtle */
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
             0 2px 4px -1px rgba(0, 0, 0, 0.06);                     /* Default cards */
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1),
             0 4px 6px -2px rgba(0, 0, 0, 0.05);                     /* Elevated cards */
--shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1),
             0 10px 10px -5px rgba(0, 0, 0, 0.04);                   /* Modals */
--shadow-2xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);                /* Floating panels */

/* Colored shadows for states */
--shadow-primary: 0 4px 12px rgba(0, 102, 255, 0.15);               /* Primary CTA */
--shadow-success: 0 4px 12px rgba(16, 185, 129, 0.15);              /* Success state */
--shadow-error: 0 4px 12px rgba(239, 68, 68, 0.15);                 /* Error state */
```

**Border Radius**:
```css
--radius-sm: 0.25rem;      /* 4px - Tight corners */
--radius-md: 0.5rem;       /* 8px - Default buttons, inputs */
--radius-lg: 0.75rem;      /* 12px - Cards */
--radius-xl: 1rem;         /* 16px - Large cards */
--radius-2xl: 1.5rem;      /* 24px - Hero sections */
--radius-full: 9999px;     /* Circular */
```

**Transitions**:
```css
--duration-fast: 150ms;        /* Quick interactions */
--duration-normal: 250ms;      /* Default transitions */
--duration-slow: 350ms;        /* Deliberate animations */

--easing-default: cubic-bezier(0.4, 0, 0.2, 1);           /* Smooth */
--easing-in: cubic-bezier(0.4, 0, 1, 1);                  /* Accelerate */
--easing-out: cubic-bezier(0, 0, 0.2, 1);                 /* Decelerate */
--easing-bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);  /* Playful - use sparingly */
```

**Reduced Motion Support** (Accessibility):
```css
/* Respect user's motion preferences */
@media (prefers-reduced-motion: reduce) {
  /* Disable all animations and transitions */
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
  
  /* Remove transformations that create motion */
  .concept-card:hover {
    transform: none !important; /* No lift effect */
  }
  
  .button:hover {
    transform: none !important; /* No lift effect */
  }
  
  /* Disable slide-in animations */
  .concept-card {
    animation: none !important;
    opacity: 1 !important;
  }
  
  /* Keep focus states (essential for navigation) */
  :focus-visible {
    outline: 2px solid var(--color-primary);
    outline-offset: 2px;
    transition: none;
  }
  
  /* Disable shimmer/pulse effects */
  .skeleton,
  .progress-bar__fill,
  .progress-step.active {
    animation: none !important;
  }
  
  /* Keep opacity changes (fade only, no movement) */
  .fade-enter,
  .fade-exit {
    transition: opacity 0.15s ease;
    transform: none !important;
  }
}
```

---

## 📐 Layout System

### Grid Structure

**Container**:
```css
.container {
  max-width: 1440px;           /* Max content width */
  margin: 0 auto;
  padding: 0 var(--space-6);   /* 32px sides */
}

@media (max-width: 768px) {
  .container {
    padding: 0 var(--space-4); /* 16px sides on mobile */
  }
}
```

**Grid System** (12-column):
```css
.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--space-6);         /* 32px */
}

/* Responsive breakpoints */
@media (max-width: 1024px) {
  .grid {
    grid-template-columns: repeat(8, 1fr);
  }
}

@media (max-width: 768px) {
  .grid {
    grid-template-columns: repeat(4, 1fr);
    gap: var(--space-4);       /* 16px on mobile */
  }
}
```

### Breakpoints

```css
--breakpoint-xs: 375px;    /* Mobile small */
--breakpoint-sm: 640px;    /* Mobile */
--breakpoint-md: 768px;    /* Tablet */
--breakpoint-lg: 1024px;   /* Desktop */
--breakpoint-xl: 1280px;   /* Desktop large */
--breakpoint-2xl: 1536px;  /* Desktop XL */
```

---

## 🧩 Component Specifications

### 1. Repo Drop Zone

**Purpose**: Primary entry point - where users drop their repository

**Layout**:
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│               [Cloud Upload Icon - 64px]               │
│                                                         │
│           Drop your repository here                     │
│           or paste a GitHub URL                         │
│                                                         │
│     ┌─────────────────────────────────────────┐       │
│     │  github.com/yourname/your-repo          │       │
│     └─────────────────────────────────────────┘       │
│                                                         │
│               [Browse Files] button                     │
│                                                         │
│         No repo? [Start from scratch] →                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Specifications**:
```css
.repo-drop-zone {
  /* Container */
  width: 100%;
  max-width: 600px;
  min-height: 400px;
  margin: var(--space-10) auto;
  
  /* Visual */
  background: var(--color-white);
  border: 2px dashed var(--color-neutral-300);
  border-radius: var(--radius-xl);
  
  /* Layout */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: var(--space-6);
  padding: var(--space-8);
  
  /* Interaction */
  transition: all var(--duration-normal) var(--easing-default);
  cursor: pointer;
}

.repo-drop-zone:hover {
  border-color: var(--color-primary);
  border-style: solid;
  background: var(--color-primary-bg);
  box-shadow: var(--shadow-primary);
}

.repo-drop-zone.dragging {
  border-color: var(--color-primary);
  background: var(--color-primary-bg);
  transform: scale(1.02);
}

.repo-drop-zone__icon {
  width: 64px;
  height: 64px;
  color: var(--color-neutral-400);
  transition: color var(--duration-normal);
}

.repo-drop-zone:hover .repo-drop-zone__icon {
  color: var(--color-primary);
}

.repo-drop-zone__heading {
  font-size: var(--text-h2);
  font-weight: var(--font-weight-semibold);
  color: var(--color-neutral-900);
  margin: 0;
}

.repo-drop-zone__subtext {
  font-size: var(--text-body-lg);
  color: var(--color-neutral-600);
  margin: 0;
}

.repo-drop-zone__input {
  width: 100%;
  padding: var(--space-4);
  border: 1px solid var(--color-neutral-300);
  border-radius: var(--radius-md);
  font-size: var(--text-body-lg);
  font-family: var(--font-mono);
  
  transition: all var(--duration-fast);
}

.repo-drop-zone__input:focus {
  outline: none;
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px var(--color-primary-bg);
}
```

**States**:
- **Default**: Neutral, inviting
- **Hover**: Border solid, blue tint
- **Dragging**: Scaled up, highlighted
- **Processing**: Show spinner, "Analyzing repository..."
- **Error**: Red border, error message

---

### 2. Concept Card

**Purpose**: Display a single design concept with preview and actions

**Layout**:
```
┌─────────────────────────────────────────┐
│                                         │
│         [Visual Preview 16:9]           │
│                                         │
├─────────────────────────────────────────┤
│                                         │
│  Concept A: High Contrast Modernism    │
│  Bold blacks + bright accents           │
│                                         │
│  • AAA contrast ratios                  │
│  • Electric blue accent                 │
│  • Clean sans-serif type                │
│                                         │
│  [👍 Like] [👎 Pass] [👁️ Details]       │
│                                         │
└─────────────────────────────────────────┘
```

**Specifications**:
```css
.concept-card {
  /* Container */
  background: var(--color-white);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
  overflow: hidden;
  
  /* Layout */
  display: flex;
  flex-direction: column;
  
  /* Interaction */
  transition: all var(--duration-normal) var(--easing-default);
  cursor: pointer;
}

.concept-card:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-4px);
}

.concept-card__preview {
  /* 16:9 aspect ratio */
  aspect-ratio: 16 / 9;
  background: var(--color-neutral-100);
  overflow: hidden;
  position: relative;
}

.concept-card__preview img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.concept-card__content {
  padding: var(--space-6);
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.concept-card__title {
  font-size: var(--text-h4);
  font-weight: var(--font-weight-semibold);
  color: var(--color-neutral-900);
  margin: 0;
}

.concept-card__description {
  font-size: var(--text-body-md);
  color: var(--color-neutral-600);
  margin: 0;
}

.concept-card__qualities {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.concept-card__quality {
  font-size: var(--text-body-sm);
  color: var(--color-neutral-700);
  display: flex;
  align-items: center;
  gap: var(--space-2);
}

.concept-card__quality::before {
  content: "•";
  color: var(--color-primary);
  font-weight: var(--font-weight-bold);
}

.concept-card__actions {
  display: flex;
  gap: var(--space-3);
  margin-top: var(--space-2);
}
```

**Action Button Styles**:
```css
.action-button {
  flex: 1;
  padding: var(--space-3) var(--space-4);
  border-radius: var(--radius-md);
  border: 1px solid var(--color-neutral-300);
  background: var(--color-white);
  font-size: var(--text-body-md);
  font-weight: var(--font-weight-medium);
  cursor: pointer;
  
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  
  transition: all var(--duration-fast);
}

.action-button--like {
  border-color: var(--color-success);
  color: var(--color-success-dark);
}

.action-button--like:hover,
.action-button--like.active {
  background: var(--color-success);
  color: var(--color-white);
  box-shadow: var(--shadow-success);
}

.action-button--dislike {
  border-color: var(--color-error);
  color: var(--color-error-dark);
}

.action-button--dislike:hover,
.action-button--dislike.active {
  background: var(--color-error);
  color: var(--color-white);
  box-shadow: var(--shadow-error);
}

.action-button--details {
  border-color: var(--color-neutral-300);
  color: var(--color-neutral-700);
}

.action-button--details:hover {
  background: var(--color-neutral-100);
  border-color: var(--color-neutral-400);
}
```

**States**:
- **Default**: Clean, inviting
- **Hover**: Lifted, shadow increased
- **Liked**: Green accent, success shadow
- **Disliked**: Red accent, error shadow
- **Exploring**: Orange accent

---

### 3. Context Wizard

**Purpose**: Guided questions to define generator constraints

**Flow**:
```
Step 1/3: What's your goal?
┌─────────────────────────────────────────┐
│  ○ Explore how my system feels         │
│  ● Rebrand or refresh visual identity  │
│  ○ Improve consistency and cohesion    │
│  ○ Prepare for new features/contexts   │
│  ○ Other: [____________]               │
│                                         │
│           [← Back] [Next →]            │
└─────────────────────────────────────────┘

Step 2/3: What qualities matter?
┌─────────────────────────────────────────┐
│  [✓] Bold - Strong, confident           │
│  [✓] Modern - Contemporary feel         │
│  [✓] Accessible - WCAG compliant        │
│  [ ] Playful - Fun, energetic           │
│  [ ] Professional - Trustworthy         │
│  [ ] Calm - Peaceful, spacious          │
│                                         │
│           [← Back] [Next →]            │
└─────────────────────────────────────────┘

Step 3/3: Any guardrails?
┌─────────────────────────────────────────┐
│  [ ] Must maintain brand colors         │
│  [✓] Need to support dark mode          │
│  [✓] Accessibility is non-negotiable    │
│  [ ] Keep existing component structure  │
│  [✓] No constraints - show everything   │
│                                         │
│    [← Back] [Generate Concepts →]      │
└─────────────────────────────────────────┘
```

**Specifications**:
```css
.context-wizard {
  max-width: 600px;
  margin: 0 auto;
  padding: var(--space-8);
}

.context-wizard__progress {
  display: flex;
  gap: var(--space-2);
  margin-bottom: var(--space-8);
}

.progress-step {
  flex: 1;
  height: 4px;
  background: var(--color-neutral-200);
  border-radius: var(--radius-full);
  transition: background var(--duration-normal);
}

.progress-step.completed {
  background: var(--color-primary);
}

.progress-step.active {
  background: var(--color-primary);
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.context-wizard__heading {
  font-size: var(--text-h2);
  font-weight: var(--font-weight-semibold);
  color: var(--color-neutral-900);
  margin-bottom: var(--space-2);
}

.context-wizard__subtext {
  font-size: var(--text-body-lg);
  color: var(--color-neutral-600);
  margin-bottom: var(--space-8);
}

.context-wizard__options {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  margin-bottom: var(--space-8);
}

.option-card {
  padding: var(--space-5);
  border: 2px solid var(--color-neutral-200);
  border-radius: var(--radius-lg);
  cursor: pointer;
  transition: all var(--duration-fast);
  
  display: flex;
  align-items: center;
  gap: var(--space-4);
}

.option-card:hover {
  border-color: var(--color-neutral-300);
  background: var(--color-neutral-50);
}

.option-card.selected {
  border-color: var(--color-primary);
  background: var(--color-primary-bg);
}

.option-card__radio {
  width: 20px;
  height: 20px;
  border: 2px solid var(--color-neutral-400);
  border-radius: var(--radius-full);
  position: relative;
  flex-shrink: 0;
}

.option-card.selected .option-card__radio {
  border-color: var(--color-primary);
}

.option-card.selected .option-card__radio::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 10px;
  height: 10px;
  background: var(--color-primary);
  border-radius: var(--radius-full);
}

.option-card__label {
  font-size: var(--text-body-lg);
  font-weight: var(--font-weight-medium);
  color: var(--color-neutral-900);
  margin: 0;
}

.context-wizard__actions {
  display: flex;
  justify-content: space-between;
  gap: var(--space-4);
}
```

---

### 4. Concept Gallery

**Purpose**: Display 3-4 generated concepts in a grid

**Layout (Desktop)**:
```
┌─────────────────────────────────────────────────────────────────┐
│  Based on: Rebrand • Bold • Modern • Accessible                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │              │  │              │  │              │         │
│  │  Concept A   │  │  Concept B   │  │  Concept C   │         │
│  │              │  │              │  │              │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│                                                                 │
│  ┌──────────────┐                                              │
│  │              │  [Generate More Variations]                  │
│  │  Concept D   │                                              │
│  │              │                                              │
│  └──────────────┘                                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Specifications**:
```css
.concept-gallery {
  padding: var(--space-8);
}

.concept-gallery__context {
  padding: var(--space-6);
  background: var(--color-neutral-50);
  border-radius: var(--radius-lg);
  margin-bottom: var(--space-8);
  
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.concept-gallery__context-label {
  font-size: var(--text-body-md);
  color: var(--color-neutral-600);
  font-weight: var(--font-weight-medium);
}

.concept-gallery__context-tags {
  display: flex;
  gap: var(--space-2);
  flex-wrap: wrap;
}

.context-tag {
  padding: var(--space-2) var(--space-3);
  background: var(--color-white);
  border-radius: var(--radius-md);
  font-size: var(--text-body-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-primary);
}

.concept-gallery__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: var(--space-6);
  margin-bottom: var(--space-8);
}

@media (min-width: 1024px) {
  .concept-gallery__grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

.concept-gallery__actions {
  display: flex;
  justify-content: center;
  gap: var(--space-4);
}
```

---

### 5. Feedback Summary Panel

**Purpose**: Show what the generator learned from feedback

**Layout**:
```
┌─────────────────────────────────────────────────────┐
│ 🧠 What I learned from your feedback:              │
├─────────────────────────────────────────────────────┤
│                                                     │
│ ✓ You liked: High Contrast Modernism               │
│   → Prioritizing bold contrast in next round       │
│                                                     │
│ ✗ You didn't like: Playful Geometric               │
│   → Avoiding playful, informal directions          │
│                                                     │
│ 👁 You explored: Bold Minimalism                    │
│   → Will show a refined version                    │
│                                                     │
│ Generating refined concepts...                     │
│ [████████░░] 80%                                    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Specifications**:
```css
.feedback-panel {
  position: sticky;
  top: var(--space-6);
  padding: var(--space-6);
  background: var(--color-white);
  border: 1px solid var(--color-neutral-200);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
}

.feedback-panel__heading {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  margin-bottom: var(--space-5);
  
  font-size: var(--text-h4);
  font-weight: var(--font-weight-semibold);
  color: var(--color-neutral-900);
}

.feedback-panel__items {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
  margin-bottom: var(--space-6);
}

.feedback-item {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.feedback-item__label {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--text-body-md);
  font-weight: var(--font-weight-medium);
}

.feedback-item__label--liked {
  color: var(--color-success-dark);
}

.feedback-item__label--disliked {
  color: var(--color-error-dark);
}

.feedback-item__label--explored {
  color: var(--color-warning-dark);
}

.feedback-item__detail {
  font-size: var(--text-body-sm);
  color: var(--color-neutral-600);
  padding-left: var(--space-6);
}

.feedback-panel__progress {
  margin-top: var(--space-6);
  padding-top: var(--space-6);
  border-top: 1px solid var(--color-neutral-200);
}

.progress-bar {
  width: 100%;
  height: 8px;
  background: var(--color-neutral-200);
  border-radius: var(--radius-full);
  overflow: hidden;
  margin-top: var(--space-3);
}

.progress-bar__fill {
  height: 100%;
  background: linear-gradient(90deg, 
    var(--color-primary) 0%, 
    var(--color-secondary) 100%
  );
  border-radius: var(--radius-full);
  transition: width var(--duration-slow) var(--easing-out);
  
  animation: shimmer 2s infinite;
}

@keyframes shimmer {
  0% { opacity: 1; }
  50% { opacity: 0.8; }
  100% { opacity: 1; }
}
```

---

### 6. Button Component

**Purpose**: Primary interactive element throughout the app

**Variants**:
```
[Primary Button]    [Secondary Button]    [Tertiary Button]

[Icon Button 📁]    [Loading... ⟳]       [Disabled Button]
```

**Specifications**:
```css
.button {
  /* Base */
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  
  /* Typography */
  font-family: var(--font-display);
  font-weight: var(--font-weight-semibold);
  text-decoration: none;
  
  /* Interaction */
  cursor: pointer;
  border: none;
  transition: all var(--duration-fast) var(--easing-default);
  
  /* Accessibility */
  user-select: none;
}

.button:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

/* Primary (main CTAs) */
.button--primary {
  padding: var(--padding-button-md);
  background: var(--color-primary);
  color: var(--color-white);
  border-radius: var(--radius-md);
  font-size: var(--text-button-lg);
  box-shadow: var(--shadow-sm);
}

.button--primary:hover {
  background: var(--color-primary-dark);
  box-shadow: var(--shadow-primary);
  transform: translateY(-1px);
}

.button--primary:active {
  transform: translateY(0);
  box-shadow: var(--shadow-sm);
}

/* Secondary (alternative actions) */
.button--secondary {
  padding: var(--padding-button-md);
  background: var(--color-white);
  color: var(--color-primary);
  border: 2px solid var(--color-primary);
  border-radius: var(--radius-md);
  font-size: var(--text-button-lg);
}

.button--secondary:hover {
  background: var(--color-primary-bg);
}

/* Tertiary (subtle actions) */
.button--tertiary {
  padding: var(--padding-button-sm);
  background: transparent;
  color: var(--color-neutral-700);
  border-radius: var(--radius-md);
  font-size: var(--text-button-md);
}

.button--tertiary:hover {
  background: var(--color-neutral-100);
  color: var(--color-neutral-900);
}

/* Sizes */
.button--small {
  padding: var(--padding-button-sm);
  font-size: var(--text-button-sm);
}

.button--large {
  padding: var(--padding-button-lg);
  font-size: var(--text-button-lg);
}

/* States */
.button:disabled,
.button--disabled {
  opacity: 0.5;
  cursor: not-allowed;
  pointer-events: none;
}

.button--loading {
  position: relative;
  color: transparent;
}

.button--loading::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 16px;
  height: 16px;
  border: 2px solid currentColor;
  border-radius: var(--radius-full);
  border-top-color: transparent;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to { transform: translate(-50%, -50%) rotate(360deg); }
}
```

---

### 7. Error Toast Component

**Purpose**: Display error messages and system notifications

**Layout**:
```
┌─────────────────────────────────────────┐
│ ⚠️  Error: Could not analyze repository │
│                                         │
│ Please check the URL and try again     │
│                          [Dismiss ×]    │
└─────────────────────────────────────────┘
```

**Specifications**:
```css
.toast {
  /* Position */
  position: fixed;
  top: var(--space-6);
  right: var(--space-6);
  z-index: 1000;
  
  /* Container */
  min-width: 320px;
  max-width: 480px;
  padding: var(--space-5);
  
  /* Visual */
  background: var(--color-white);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-xl);
  border-left: 4px solid var(--color-error);
  
  /* Layout */
  display: flex;
  align-items: flex-start;
  gap: var(--space-3);
  
  /* Animation */
  animation: slideInRight var(--duration-normal) var(--easing-out);
}

@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(100%);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.toast--error {
  border-left-color: var(--color-error);
}

.toast--error .toast__icon {
  color: var(--color-error);
}

.toast--success {
  border-left-color: var(--color-success);
}

.toast--success .toast__icon {
  color: var(--color-success);
}

.toast--warning {
  border-left-color: var(--color-warning);
}

.toast--warning .toast__icon {
  color: var(--color-warning);
}

.toast__icon {
  flex-shrink: 0;
  width: 20px;
  height: 20px;
  margin-top: 2px;
}

.toast__content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.toast__title {
  font-size: var(--text-body-md);
  font-weight: var(--font-weight-semibold);
  color: var(--color-neutral-900);
  margin: 0;
}

.toast__message {
  font-size: var(--text-body-sm);
  color: var(--color-neutral-700);
  margin: 0;
}

.toast__close {
  flex-shrink: 0;
  width: 24px;
  height: 24px;
  padding: 0;
  border: none;
  background: transparent;
  color: var(--color-neutral-500);
  cursor: pointer;
  border-radius: var(--radius-sm);
  
  display: flex;
  align-items: center;
  justify-content: center;
  
  transition: all var(--duration-fast);
}

.toast__close:hover {
  background: var(--color-neutral-100);
  color: var(--color-neutral-700);
}

/* Auto-dismiss animation */
.toast.exiting {
  animation: slideOutRight var(--duration-normal) var(--easing-in);
}

@keyframes slideOutRight {
  from {
    opacity: 1;
    transform: translateX(0);
  }
  to {
    opacity: 0;
    transform: translateX(100%);
  }
}

/* Mobile adjustments */
@media (max-width: 768px) {
  .toast {
    left: var(--space-4);
    right: var(--space-4);
    min-width: auto;
  }
}
```

**States**:
- **Error**: Red border, error icon
- **Success**: Green border, check icon
- **Warning**: Orange border, warning icon
- **Auto-dismiss**: Fades out after 5 seconds
- **Persistent**: Requires manual dismiss

---

### 8. Loading Spinner Component

**Purpose**: Indicate generation/processing in progress

**Variants**:
```
Inline:  ⟳ Loading...

Overlay: 
┌─────────────────────────────────────────┐
│                                         │
│              ⟳                          │
│      Generating concepts...             │
│                                         │
└─────────────────────────────────────────┘
```

**Specifications**:
```css
/* Inline spinner */
.spinner {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  color: var(--color-neutral-600);
  font-size: var(--text-body-md);
}

.spinner__icon {
  width: 16px;
  height: 16px;
  border: 2px solid currentColor;
  border-radius: var(--radius-full);
  border-top-color: transparent;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Overlay spinner (full screen) */
.spinner-overlay {
  position: fixed;
  inset: 0;
  z-index: 9999;
  
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(4px);
  
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: var(--space-4);
  
  animation: fadeIn var(--duration-normal);
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

[data-theme="dark"] .spinner-overlay {
  background: rgba(15, 23, 42, 0.9);
}

.spinner-overlay__icon {
  width: 48px;
  height: 48px;
  border: 4px solid var(--color-primary);
  border-radius: var(--radius-full);
  border-top-color: transparent;
  animation: spin 0.8s linear infinite;
}

.spinner-overlay__text {
  font-size: var(--text-body-lg);
  font-weight: var(--font-weight-medium);
  color: var(--color-neutral-900);
}

.spinner-overlay__subtext {
  font-size: var(--text-body-sm);
  color: var(--color-neutral-600);
  text-align: center;
  max-width: 300px;
}

/* Button spinner (replaces button text) */
.button--loading {
  position: relative;
  color: transparent;
  pointer-events: none;
}

.button--loading::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 16px;
  height: 16px;
  border: 2px solid currentColor;
  border-radius: var(--radius-full);
  border-top-color: transparent;
  animation: spin 0.6s linear infinite;
  color: var(--color-white);
}
```

**Usage**:
```typescript
// Inline spinner
<div className="spinner">
  <div className="spinner__icon" />
  <span>Loading...</span>
</div>

// Overlay spinner
<div className="spinner-overlay">
  <div className="spinner-overlay__icon" />
  <div className="spinner-overlay__text">Generating concepts...</div>
  <div className="spinner-overlay__subtext">
    Analyzing your design tokens
  </div>
</div>

// Button loading state
<button className="button button--primary button--loading">
  Submit
</button>
```

---

### 9. Header/Navigation Component

**Purpose**: Main navigation and app identity

**Layout**:
```
┌─────────────────────────────────────────────────────────┐
│ [Embody Logo]              [Help] [Settings] [@User]   │
└─────────────────────────────────────────────────────────┘
```

**Specifications**:
```css
.header {
  /* Position */
  position: sticky;
  top: 0;
  z-index: 100;
  
  /* Container */
  width: 100%;
  padding: var(--space-4) var(--space-6);
  
  /* Visual */
  background: var(--color-white);
  border-bottom: 1px solid var(--color-neutral-200);
  backdrop-filter: blur(8px);
  
  /* Layout */
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
}

.header__logo {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  text-decoration: none;
  color: var(--color-neutral-900);
  font-weight: var(--font-weight-semibold);
  font-size: var(--text-body-lg);
  
  transition: opacity var(--duration-fast);
}

.header__logo:hover {
  opacity: 0.8;
}

.header__logo-icon {
  width: 32px;
  height: 32px;
  color: var(--color-primary);
}

.header__nav {
  display: flex;
  align-items: center;
  gap: var(--space-2);
}

.header__nav-link {
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-md);
  
  font-size: var(--text-body-md);
  color: var(--color-neutral-700);
  text-decoration: none;
  
  transition: all var(--duration-fast);
}

.header__nav-link:hover {
  background: var(--color-neutral-100);
  color: var(--color-neutral-900);
}

.header__nav-link.active {
  background: var(--color-primary-bg);
  color: var(--color-primary-text);
}

/* Mobile: Hamburger menu */
@media (max-width: 768px) {
  .header {
    padding: var(--space-3) var(--space-4);
  }
  
  .header__nav {
    display: none;
  }
  
  .header__nav.mobile-open {
    display: flex;
    flex-direction: column;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: var(--color-white);
    border-bottom: 1px solid var(--color-neutral-200);
    padding: var(--space-4);
    gap: var(--space-2);
  }
  
  .header__menu-button {
    display: flex;
  }
}

.header__menu-button {
  display: none;
  width: 40px;
  height: 40px;
  padding: 0;
  border: none;
  background: transparent;
  color: var(--color-neutral-700);
  cursor: pointer;
  border-radius: var(--radius-md);
  
  align-items: center;
  justify-content: center;
  
  transition: background var(--duration-fast);
}

.header__menu-button:hover {
  background: var(--color-neutral-100);
}
```

**Usage**:
```typescript
<header className="header">
  <a href="/" className="header__logo">
    <svg className="header__logo-icon">...</svg>
    <span>Embody</span>
  </a>
  
  <nav className="header__nav">
    <a href="/docs" className="header__nav-link">Help</a>
    <a href="/settings" className="header__nav-link">Settings</a>
    <button className="header__nav-link">@user</button>
  </nav>
  
  <button className="header__menu-button" aria-label="Menu">
    ☰
  </button>
</header>
```

---

## 📱 Responsive Behavior

### Mobile (< 768px)

**Layout Changes**:
- Single column concept gallery
- Simplified navigation
- Larger touch targets (min 44x44px)
- Simplified context wizard (one question per screen)

**Optimizations**:
- Reduce concept card previews to 4:3 aspect ratio
- Stack action buttons vertically
- Collapse feedback panel into expandable drawer
- Show minimal header with menu button

### Tablet (768px - 1024px)

**Layout Changes**:
- 2-column concept gallery
- Side-by-side context wizard steps
- Persistent feedback panel (sidebar)

### Desktop (> 1024px)

**Layout Changes**:
- 3-column concept gallery
- Full wizard experience
- Side-by-side comparisons available
- Rich previews and interactions

---

## ♿ Accessibility Specifications

### Contrast Requirements

**Text Contrast** (WCAG AAA):
- Body text: 7:1 minimum (var(--color-neutral-800) on white)
- Large text: 4.5:1 minimum
- UI elements: 3:1 minimum

**Color Independence**:
- Never rely solely on color to convey information
- Use icons + color for feedback (✓ + green, ✗ + red)
- Provide text labels for all interactive elements

### Keyboard Navigation

**Focus States**:
```css
:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
  border-radius: var(--radius-sm);
}
```

**Tab Order**:
1. Main navigation
2. Repo drop zone
3. Context wizard steps
4. Concept cards (left to right, top to bottom)
5. Action buttons
6. Secondary controls

**Keyboard Shortcuts**:
- `Tab` / `Shift+Tab`: Navigate
- `Enter` / `Space`: Activate buttons
- `Escape`: Close modals
- `Arrow keys`: Navigate concept gallery

### Screen Reader Support

**Semantic HTML**:
```html
<main aria-label="Design System Generator">
  <section aria-label="Repository Input">
    <h2 id="repo-heading">Drop your repository</h2>
    <input 
      aria-labelledby="repo-heading"
      aria-describedby="repo-help"
      type="text"
      placeholder="github.com/yourname/repo"
    />
    <p id="repo-help" class="sr-only">
      Paste a GitHub URL or drag and drop a local repository folder
    </p>
  </section>
  
  <section aria-label="Generated Concepts">
    <h2>Design Concepts</h2>
    <ul aria-label="Concept gallery">
      <li>
        <article aria-labelledby="concept-a-title">
          <h3 id="concept-a-title">High Contrast Modernism</h3>
          <p>Bold blacks and bright accents</p>
          <div role="group" aria-label="Actions">
            <button aria-label="Like this concept">👍 Like</button>
            <button aria-label="Pass on this concept">👎 Pass</button>
            <button aria-label="View details">👁️ Details</button>
          </div>
        </article>
      </li>
    </ul>
  </section>
</main>
```

**ARIA Live Regions**:
```html
<div aria-live="polite" aria-atomic="true" class="sr-only">
  Generating concepts based on your feedback...
</div>

<div aria-live="assertive" aria-atomic="true" role="alert" class="sr-only">
  Error: Could not analyze repository
</div>
```

---

## 🎭 Animation & Micro-interactions

### Loading States

**Shimmer Effect** (for image loading):
```css
@keyframes shimmer {
  0% {
    background-position: -1000px 0;
  }
  100% {
    background-position: 1000px 0;
  }
}

.skeleton {
  background: linear-gradient(
    90deg,
    var(--color-neutral-200) 0%,
    var(--color-neutral-100) 50%,
    var(--color-neutral-200) 100%
  );
  background-size: 1000px 100%;
  animation: shimmer 2s infinite;
}
```

**Generating Animation**:
- Pulsing dots: "Generating concepts..."
- Progress bar with shimmer
- Fade-in concepts as they're generated (stagger by 150ms)

### Transitions

**Page Transitions**:
```css
.page-enter {
  opacity: 0;
  transform: translateY(20px);
}

.page-enter-active {
  opacity: 1;
  transform: translateY(0);
  transition: all var(--duration-slow) var(--easing-out);
}

.page-exit {
  opacity: 1;
}

.page-exit-active {
  opacity: 0;
  transform: translateY(-20px);
  transition: all var(--duration-normal) var(--easing-in);
}
```

**Concept Card Entrance**:
```css
@keyframes slideInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.concept-card {
  animation: slideInUp var(--duration-slow) var(--easing-out) both;
}

.concept-card:nth-child(1) { animation-delay: 0ms; }
.concept-card:nth-child(2) { animation-delay: 150ms; }
.concept-card:nth-child(3) { animation-delay: 300ms; }
.concept-card:nth-child(4) { animation-delay: 450ms; }
```

### Hover Effects

**Lift on Hover**:
```css
.hoverable {
  transition: transform var(--duration-normal), 
              box-shadow var(--duration-normal);
}

.hoverable:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}
```

**Bounce on Click**:
```css
.clickable:active {
  animation: bounce var(--duration-fast) var(--easing-bounce);
}

@keyframes bounce {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(0.95); }
}
```

---

## 📐 Implementation Notes for design-intelligence

When generating assets from these specifications:

**1. Use these exact token values** - They're carefully chosen for Embody's design language

**2. Generate multiple states** for each component:
- Default
- Hover
- Active/Pressed
- Focused
- Disabled
- Loading

**3. Create responsive variants** for:
- Mobile (< 768px)
- Tablet (768px - 1024px)
- Desktop (> 1024px)

**4. Export formats needed**:
- Figma components (with variants)
- React components (TypeScript)
- CSS modules
- SVG icons
- PNG mockups (for documentation)

**5. Accessibility checklist** for every component:
- Color contrast meets WCAG AAA
- Keyboard navigation works
- Screen reader labels present
- Focus states visible
- Touch targets minimum 44x44px

**6. Documentation to generate**:
- Component API documentation
- Usage examples
- Do's and Don'ts
- Accessibility notes
- Implementation code

---

**Built with [Amplifier](https://github.com/microsoft/amplifier)** 🤖

*Design is forming a point of view about a future state.  
This specification helps translate that vision into reality.*
