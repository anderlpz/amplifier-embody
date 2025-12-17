# Design System Generator - Experience Specification

> **An intelligence that helps designers explore and refine design system futures through guided iteration**

**Version**: 3.0.0  
**Status**: Hybrid Approach - Context + Generation + Refinement  
**Created**: December 17, 2024  
**Built with**: [Amplifier Framework](https://github.com/microsoft/amplifier)

---

## 🎯 Core Philosophy

### Design as Perspective, Not Production

**Design is the act of forming a point of view about a future state, not the act of assembling its implementation.**

Tools that collapse design into production optimize for output at the expense of imagination. When constraints enter too early, they shape what is thinkable rather than what is possible. This leads to conservative decisions, smaller ambition, and local maxima.

**Design intelligence should not replace thinking or prematurely encode feasibility.** Its role is to remain referential—helping designers externalize, examine, and evolve their perspective across states, flows, and intent. It should support dreaming, sensemaking, and communication before execution.

Great design emerges from a clear vision that is later realized through collaboration. **Designers imagine futures. Engineers make them real.** Tools should protect that distinction while strengthening the bridge between them.

Design succeeds not when it generates code faster, but when it preserves the conditions required for original thought and meaningful ambition.

---

## 🌊 The Hybrid Approach

### Not: Fully Conversational (Too Slow)
Full dialogue for every decision slows down exploration and can feel aimless.

### Not: Pick from 3 Cards (Too Limiting)
Pre-generated variants without context often miss the mark and feel like rolling dice.

### Instead: Context → Generate → Refine

**The Flow:**
```
1. Gather Key Context (brief, focused)
   Designer answers 2-3 questions about their goal
   
2. Generate Concepts (based on context)
   Tool creates 3-4 directions informed by designer intent
   
3. Quick Feedback (👍/👎)
   Designer reacts to concepts to guide refinement
   
4. Refine & Iterate (until satisfied)
   Tool evolves based on feedback, generates new directions
```

**Example:**
```
Tool: "What's your focus?"
Designer: [Selects "Rebrand - more modern feel"]

Tool: "What matters most?"
Designer: [Selects "Bold & confident" + "Accessible"]

Tool: [Generates 4 concepts]
      • Concept A: Bold colors, strong contrast
      • Concept B: Modern minimalism, lots of space
      • Concept C: Playful geometric, vibrant
      • Concept D: Sophisticated gradients, subtle

Designer: [👍 Concept A] [👎 Concept C] [🤔 Concept B]

Tool: [Refines]
      "You liked bold contrast. Here are 3 variations on that direction..."
```

---

## 🎨 The Experience: Context-Driven Exploration

### Step 1: Extraction (Automatic)
**Goal**: Understand current state without user input

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

### Step 2: Context Gathering (Brief, Focused)
**Goal**: Understand designer intent in ~60 seconds

**Question 1: What's your goal?**
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

**Question 2: What matters to you?** (Select 1-3)
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

**Optional Question 3: Any constraints?** (Optional)
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

**Context Summary:**
```
"Got it! You want to rebrand with a bold and modern feel, 
 while maintaining accessibility. Let me generate some concepts..."
```

**Time to complete**: ~60 seconds  
**Flexibility**: Can be more specific or stay general

---

### Step 3: Initial Generation (Context-Driven)
**Goal**: Show 3-4 concepts informed by designer's context

**Not random variants** - Each concept directly responds to stated intent.

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

### Step 4: Quick Feedback (Thumbs Up/Down)
**Goal**: Designer reacts to guide refinement

**Interaction:**
```
Designer clicks: 👍 Concept A, 👎 Concept C, Details on Concept B

Tool responds:
"You liked High Contrast Modernism and want to explore 
 Geometric Bold further. 
 
 Should I:
 • Refine the bold contrast direction
 • Blend geometric shapes with high contrast
 • Show variations on both approaches"
```

**Feedback Types:**
- **👍 Like**: "More like this"
- **👎 Dislike**: "Not this direction"  
- **Details**: "Show me more depth on this concept"
- **Combine**: "Blend aspects of A and B"

**Philosophy**: Fast feedback loop preserves momentum while keeping designer in control.

---

### Step 5: Refinement & Iteration
**Goal**: Evolve based on feedback until designer is satisfied

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

Tool: "Getting closer! Let me show you this direction applied 
       to different contexts..."

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

---

### Step 6: Documentation & Handoff
**Goal**: Capture the journey and prepare for engineering

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

**Documentation captures:**
- Where you started (current state)
- What you wanted (intent)
- What you explored (concepts & feedback)
- Where you landed (final direction)
- Why it works (rationale)

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

**Built with [Amplifier](https://github.com/microsoft/amplifier)** 🤖

*Design is forming a point of view about a future state.  
This tool helps designers reach that clarity through guided exploration.*
