# 🎨 Embody

> **A design system generator that embodies perspective into taste**

**Version**: 1.0.0  
**Status**: Architecture & Design Phase  
**Created**: December 17, 2025 at 14:44 PST  
**Built with**: [Amplifier Foundation](https://github.com/microsoft/amplifier-foundation)

---

## 🎯 What is Embody?

**Embody is a design system generator.** The output is a design system, but the **product is the generator itself.**

This distinction is critical: we're not building a design system library or a token set. We're building **the thing that generates design systems** based on your perspective.

### The Generator Philosophy

> **Design is the act of forming a point of view about a future state, not the act of assembling its implementation.**

Embody embodies this philosophy by:
- **Encoding taste** - Your perspective becomes the generative constraints
- **Producing coherent variations** - Every output feels like it came from the same place
- **Enabling iteration** - Refine the generator, regenerate the system
- **Maintaining recognizability** - Like Rolex or Chipotle: customization within constraints

### Why "Generator" Matters

When we say "design system," people think: tokens, components, documentation.  
When we say "generator," we imply:
- **Upstream thinking** - Input → constraints → output
- **Iteration** - Regenerate with different contexts
- **Taste** - It's producing a point of view, not just artifacts
- **Customization** - But within a coherent system

**Think Chipotle**: You're customizing your burrito, but you're not inventing a new cuisine. You choose ingredients within constraints, and the result is still recognizably Chipotle.

**Think Rolex**: Choices exist (dial color, bracelet style), but the crown stays where it belongs. Constraints ensure the output remains recognizably Rolex.

**Embody works the same way**: You customize within your encoded taste, and every generated variation maintains your recognizable perspective.

### How the Generator Works

**Input**: Your design perspective (goals, qualities, constraints)  
**Process**: AI-powered generation with iterative refinement  
**Output**: A coherent design system that embodies your perspective

```
1. Define Your Perspective (60 seconds)
   What's your goal? What qualities matter?
   → These become the generator's constraints
   
2. Generator Creates Variations (AI-powered)
   4 distinct interpretations of your perspective
   → Each explores a different approach
   
3. Refine the Generator (👍/👎 feedback)
   Your reactions tune the generation logic
   → Not random—learning what "tastes right" to you
   
4. Iterate Until Coherent (2-4 rounds)
   Generator evolves to produce your aesthetic
   → Result: A design system that feels recognizably "yours"
   
5. Export the System
   Tokens, components, documentation, usage guidance
   → The artifact + the story of how you got there
```

**Key Insight**: You're not picking from pre-made options. You're **training a generator to understand your taste**, then using it to produce a coherent design system.

---

## 📚 Documentation

- **[EXPERIENCE_SPEC.md](./docs/specs/EXPERIENCE_SPEC.md)** - Complete user experience specification (v3.0)
  - Hybrid approach philosophy
  - User flows and interactions
  - UI component breakdown and design system
  - Success metrics
  
- **[BACKEND_ARCHITECTURE.md](./docs/specs/BACKEND_ARCHITECTURE.md)** - Technical architecture
  - Amplifier Foundation integration
  - Collection-based agent system
  - Session management and API design
  - Amplifier contribution strategy

- **[USERS.md](./docs/research/USERS.md)** - User research & personas
  - User spectrum (non-designers → designers)
  - Jobs to be done
  - Entry points and interaction modes
  
- **[ROADMAP.md](./docs/planning/ROADMAP.md)** - Development roadmap
  - Phased rollout strategy
  - Amplifier contribution timeline
  - Success metrics by phase

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

### The Generator is the Product

**The artifact (design system) is the output. The generator is what you're building.**

When you refine concepts through feedback, you're not just picking designs—you're teaching the generator to understand your aesthetic. The generator encodes your taste and produces coherent variations.

### Taste Within Constraints

**Infinite freedom produces incoherence. Constraints produce recognizability.**

Like Chipotle's burrito line or Rolex's watch configurator:
- You have choices (ingredients, dial color)
- But not infinite freedom (no sushi at Chipotle, no crown relocation on Rolex)
- The result is **recognizably from that system**

Embody works the same way: it generates variations that all feel like they came from your perspective.

### Iteration as Refinement

**You're not picking "the one." You're refining the generator until outputs feel right.**

Each feedback round tunes the generation logic:
- 👍 "More like this" → Generator learns what resonates
- 👎 "Not this direction" → Generator learns what to avoid
- After 2-4 rounds → Generator consistently produces your aesthetic

### Coherent, Not Generic

**The output should reflect a point of view, not be a least-common-denominator compromise.**

Generic design systems lack character. Embody helps you:
- **Encode your perspective** into generation constraints
- **Produce taste** not just tokens
- **Maintain coherence** across all generated variations
- **Stay recognizable** even with customization

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

### Generator vs Library

**Traditional Design System** (Library approach):
- Here's a set of tokens and components
- Use them as-is or customize manually
- One static artifact

**Embody** (Generator approach):
- Here's a system that generates design systems
- Train it with your perspective
- Regenerate for different contexts while maintaining your taste

### Constrained Customization

**Infinite Freedom** → Incoherent outputs  
**No Freedom** → Generic, lifeless systems  
**Embody** → Customization within taste constraints

Like ordering at Chipotle or configuring a Rolex:
- You feel like you're customizing
- But you're working within a coherent system
- The result is recognizably from that brand

### Perspective as Input

**Traditional tools**: "What do you want it to look like?"  
**Embody**: "What's your design perspective?" → Generator learns your taste → Produces coherent variations

You're not describing the artifact. You're defining the generator's constraints.

---

## 🤝 The Generator in Action

### Example Session

```
Designer: [Connects codebase] → 47 tokens extracted

Embody: "What's your design perspective?"
Designer: "Rebrand - more modern and bold"

Embody: "What qualities define your aesthetic?"
Designer: "Bold + Modern + Accessible"

[Generator initialized with these constraints]

Embody: [Generator produces 4 variations]
  • High Contrast Modernism (B&W + electric accents)
  • Geometric Bold (sharp angles, grid)
  • Gradient Modern (vibrant, smooth)
  • Bold Minimalism (space + type)

Designer: 👍 High Contrast, 👎 Gradient, 👁️ Geometric

[Generator learns: prioritize contrast, avoid gradients]

Embody: [Generator produces refined variations]
  • Even Bolder (pure B&W + neon)
  • Softer Edges (rounded, friendlier)
  • Color Emphasis (strategic color) ⭐

Designer: 👍 Color Emphasis → "This feels right"

[Generator now tuned to produce this aesthetic consistently]

Embody: [Exports the generated system]
  • Design system (tokens, components, docs)
  • Generator constraints (for regeneration)
  • Journey documentation (the "why")
  • Multiple export formats (Figma, CSS, Tailwind)
```

**Result**: A design system that embodies your perspective, plus the generator tuned to produce more in the same aesthetic.

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
