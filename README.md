# 🎨 Embody

> **An Amplifier-powered design system exploration tool that helps designers form and refine their perspective**

**Status**: Architecture & Design Phase  
**Built with**: [Amplifier Foundation](https://github.com/microsoft/amplifier-foundation)

---

## 🎯 What is Embody?

Embody is a design system exploration tool that embodies a core philosophy:

> **Design is the act of forming a point of view about a future state, not the act of assembling its implementation.**

Most design system tools collapse design into production, optimizing for output at the expense of imagination. Embody stays **referential**—helping designers externalize, examine, and evolve their perspective through guided iteration.

### The Hybrid Approach

Embody is **not** a "roll the dice and pick one" generator.  
Embody is **not** a fully conversational chatbot that's too slow.

**Embody is**: Context → Generate → Refine

```
1. Gather Context (60 seconds)
   Designer answers 2-3 focused questions
   
2. Generate Concepts (AI-powered, contextual)
   4 distinct design concepts based on intent
   
3. Quick Feedback (👍/👎/Details)
   Designer reacts to guide refinement
   
4. Iterative Refinement (2-4 rounds)
   Concepts evolve based on feedback until "this feels right"
   
5. Document Journey
   Capture the thinking process for engineering handoff
```

---

## 📚 Documentation

- **[EXPERIENCE_SPEC.md](./EXPERIENCE_SPEC.md)** - Complete user experience specification (v3.0)
  - Hybrid approach philosophy
  - User flows and interactions
  - UI component breakdown
  - Success metrics
  
- **[BACKEND_ARCHITECTURE.md](./BACKEND_ARCHITECTURE.md)** - Technical architecture
  - Amplifier Foundation integration
  - Collection-based agent system
  - Session management
  - API design

---

## 🏗️ Architecture Highlights

### Collection-Based Intelligence

Embody uses **Amplifier Collections** for cross-domain expertise:

```yaml
Collections:

1. developer-expertise
   • zen-architect - Code analysis
   • modular-builder - Implementation
   • researcher - Content research

2. design-intelligence
   • design-system-architect - System design
   • component-designer - Component design
   • art-director - Aesthetic direction

3. foundation
   • explorer - Codebase reconnaissance
   • session-finder - Past session search

4. embody-collection (new)
   • context-gatherer - Parse designer intent
   • concept-generator - Generate concepts
   • refinement-engine - Iterative refinement
   • documentation-builder - Journey documentation
```

### Stack

**Backend**:
- FastAPI (Python 3.11+)
- Amplifier Foundation (bundles, profiles, agents)
- Amplifier Collections (git-based agent libraries)

**Frontend**:
- Next.js 15 (App Router)
- React + TypeScript
- CSS Modules

**Deployment**:
- Standalone web app initially
- Potential Amplifier module later

---

## 🎨 Core Philosophy

### Preserve Imagination

**Tools should expand possibility space, not constrain it.**
- Offer perspectives, not prescriptions
- Support "what if" thinking
- Delay technical constraints
- Encourage ambition

### Stay Referential

**Tools should help designers think, not think for them.**
- Ask questions before generating
- Offer language and frameworks
- Show implications of choices
- Never decide on their behalf

### Document Thinking

**Capture the journey, not just the destination.**
- Track conversation history
- Preserve decision reasoning
- Show evolution of thought
- Bridge to engineering with context

### Support Collaboration

**Strengthen designer-engineer communication.**
- Clear vision documentation
- Rationale preservation
- Gradual specificity
- Shared understanding

---

## 🚀 Current Status

**Phase**: Architecture & Design Specification ✅

**Completed**:
- ✅ Experience specification (v3.0 - hybrid approach)
- ✅ Backend architecture (collection-based)
- ✅ Philosophy articulation
- ✅ Agent definitions (4 embody-specific agents)
- ✅ API design (6 endpoints)
- ✅ UI/UX patterns

**Next Steps**:
- ⬜ Initialize project structure
- ⬜ Set up backend with FastAPI
- ⬜ Create embody-collection with 4 agents
- ⬜ Implement session management
- ⬜ Build context wizard (frontend)
- ⬜ Implement concept generation endpoint
- ⬜ Build concept gallery UI
- ⬜ Implement refinement loop
- ⬜ Build documentation export

---

## 🎯 Key Differentiators

### vs Traditional Design Tools
- **Not template-driven** - Emerges from your actual design tokens
- **Not prescriptive** - Offers perspectives, doesn't enforce patterns
- **Not one-shot** - Iterative refinement until satisfied

### vs AI Generation Tools
- **Not random** - Concepts based on your stated intent
- **Not black box** - Shows reasoning and journey
- **Not fire-and-forget** - Maintains stateful conversation

### vs Design Documentation Tools
- **Not just recording** - Actively helps think through decisions
- **Not static** - Living exploration that evolves
- **Not isolated** - Connects design thinking to engineering reality

---

## 🤝 Philosophy in Action

### Example Session

```
Designer: [Connects codebase] → 47 tokens extracted

Embody: "What's your focus?"
Designer: "Rebrand - more modern and bold"

Embody: "What matters most?"
Designer: "Bold + Modern + Accessible"

Embody: [Generates 4 concepts]
  • High Contrast Modernism (B&W + electric accents)
  • Geometric Bold (sharp angles, grid)
  • Gradient Modern (vibrant, smooth)
  • Bold Minimalism (space + type)

Designer: 👍 High Contrast, 👎 Gradient, 👁️ Geometric

Embody: [Refines based on feedback]
  • Even Bolder (pure B&W + neon)
  • Softer Edges (rounded, friendlier)
  • Color Emphasis (strategic color) ⭐

Designer: 👍 Color Emphasis → "This feels right"

Embody: [Documents journey]
  • Design brief (for stakeholders)
  • Token specs (for engineers)
  • Implementation guide (step-by-step)
  • Figma export (for validation)
```

**Result**: Clear design direction with full rationale, ready for engineering.

---

## 📝 License

MIT

---

## 🙏 Acknowledgments

- **Amplifier Team** - For the incredible foundation
- **Design Community** - For inspiring better tools

---

**Built with ❤️ and Amplifier Foundation** 🤖

*"Design is forming a point of view about a future state.  
This tool helps designers reach that clarity through guided exploration."*
