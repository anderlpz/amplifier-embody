# Embody Users & Jobs to be Done

> **Everyone is a designer. Embody helps you express your design perspective with professional quality.**

**Version**: 1.0.0  
**Created**: December 17, 2025 at 15:12 PST  
**Purpose**: Define who uses Embody, what they bring, and how they interact with the system

---

## 🎯 Core Philosophy

**Everyone is a designer** (has purpose, planning, intention behind their work), but most people **can't fully express their design vision** with professional execution.

**Design definition**: "Purpose, planning, or intention that exists or is thought to exist behind an action, fact, or material object."

By this definition:
- The engineer building a CLI tool has design intent (how it should feel to use)
- The product manager creating a dashboard has design perspective (what story it should tell)
- The entrepreneur building a startup has design vision (how the brand should communicate)

**Embody's role**: Help anyone express their design perspective with professional quality through AI design intelligence.

---

## 👥 User Spectrum

Embody is for **ALL users** (not either/or):

### Non-Designers (Primary Focus)

**Amplifier users who need design but aren't designers:**
- Engineers building tools, apps, websites
- Product managers defining interfaces
- Entrepreneurs creating brands
- Researchers presenting data
- Anyone building something that needs design

**What they bring**:
- Clear vision for what they're building
- Expertise in their problem domain
- Perspective on how it should feel
- Often: incomplete design vocabulary to express it

**What they need**:
- Professional design execution
- Help articulating their design perspective
- Confidence their design communicates well
- Speed without compromising quality

### Designers (Also Benefit)

**Professional designers using Amplifier:**
- Want to work faster
- Need to explore more options quickly
- Benefit from AI design intelligence
- Can focus on higher-level decisions

**Parallel**: Engineers use AI engineering tools (like GitHub Copilot) to work faster and get better results. Designers use Embody the same way.

**What they bring**:
- Design expertise and vocabulary
- Clear aesthetic preferences
- Refined taste and judgment
- Higher expectations for quality

**What they need**:
- Speed in exploration and iteration
- AI partner that understands design
- Professional execution at scale
- Tool that respects their expertise

### The Spectrum

```
Non-Designer ←──────────────────────────────→ Designer
│                     │                     │
"I need design"   "I have taste,        "I'm a pro,
                   need execution"        need speed"

All benefit from:
• Design intelligence that understands their vision
• Professional quality execution
• Fast iteration and exploration
• Generator that learns their perspective
```

---

## 💼 Jobs to be Done

### Primary Jobs

#### 1. "I need a design system but I'm not a designer"

**User**: Amplifier user building a product  
**Context**: Has a working codebase, needs professional design  
**Hiring Embody to**: Create a professional design system from their existing work

**Success looks like**:
- Design system that feels authentic to their product
- Professional quality they couldn't achieve alone
- Fast enough to maintain momentum
- Understanding of why it works (not black box)

#### 2. "I want my design to communicate my perspective"

**User**: Builder with strong vision but limited design execution skills  
**Context**: Knows what they want it to feel like, can't execute it  
**Hiring Embody to**: Translate their perspective into professional design

**Success looks like**:
- Design feels like theirs, not generic
- Captures the essence of what they were imagining
- Elevated beyond what they could do alone
- Others recognize their vision in the result

#### 3. "I need to explore design directions quickly"

**User**: Designer or non-designer early in a project  
**Context**: Not sure what direction to take, need to see options  
**Hiring Embody to**: Generate professional options to react to

**Success looks like**:
- Multiple high-quality directions to choose from
- Fast enough to maintain creative flow
- Each option is professionally executed
- Clear differences between approaches

#### 4. "My design needs to evolve with my product"

**User**: Builder iterating on their product  
**Context**: Product has changed, design needs to adapt  
**Hiring Embody to**: Regenerate design system that reflects current state

**Success looks like**:
- Design stays aligned with product evolution
- Consistency maintained across iterations
- Fast enough to keep pace with development
- Generator learns and improves over time

### Secondary Jobs

#### 5. "I want to understand design better"

**User**: Non-designer wanting to improve design literacy  
**Hiring Embody to**: Learn design principles through interaction

**Success looks like**:
- Understanding why certain choices work
- Building design vocabulary over time
- More confident in design decisions
- Referential learning (not prescriptive)

#### 6. "I need design variations for different contexts"

**User**: Builder deploying across multiple platforms/contexts  
**Hiring Embody to**: Generate consistent variations for different use cases

**Success looks like**:
- Same aesthetic, different applications
- Maintains coherence across contexts
- Fast generation of variations
- Reusable generator constraints

#### 7. "I want to design before I build" **(P2 - Future)**

**User**: Amplifier user with an idea but no code yet  
**Context**: Starting from scratch, wants to explore design first  
**Hiring Embody to**: Help visualize and design before writing any code

**Success looks like**:
- Design exploration without needing a codebase
- Clear design direction before development starts
- Design system ready when they start coding
- Design-first approach enabled

**Note**: This use case requires additional entry points (text description, sketches, references) beyond repo analysis. Planned for Phase 2.

---

## 🚪 Entry Points (What Users Bring)

### No Repo: Just an Idea **(P2 - Future)**

**What they bring**: Description of what they want to build  
**What happens**:
1. User describes their idea (text, sketches, references)
2. Embody asks clarifying questions
3. Generates design explorations based on description
4. Design system ready before any code is written

**Use case**: "I want to design before I build"

**Example flow**:
```
User: "I want to build a collaborative todo app for remote teams"
Embody: "Got it! What feeling should it have? Any reference apps you like?"
User: "Professional but friendly, like Notion + Slack"
Embody: "Here are 3 design directions for your team todo app..."
```

**Status**: Planned for Phase 2. Requires additional context gathering beyond repo analysis.

---

### Minimal Entry: Just a Repo

**What they bring**: Git repository URL or local path  
**What happens**: 
1. Embody analyzes the repo
2. Determines what it is (e.g., "looks like a todo app")
3. Extracts existing tokens/patterns
4. Generates 3 initial design options

**Use case**: "I just want to see what's possible"

**Example flow**:
```
User: [Drops repo link]
Embody: "I analyzed your todo app. Here are 3 design directions..."
User: [Picks one or asks for more]
```

### Guided Entry: Answer Questions

**What they bring**: Repo + responses to context questions  
**What happens**:
1. Embody asks 2-3 focused questions
2. Goal: "What are you building this for?"
3. Qualities: "What should it feel like?"
4. Constraints: "Any guardrails?"
5. Generates contextual options

**Use case**: "I have a vision, need help articulating it"

**Example flow**:
```
User: [Drops repo + answers questions]
Embody: "Got it! Building a todo app for teams that should feel 
         modern and collaborative. Here are 3 approaches..."
```

### Rich Entry: Full Context

**What they bring**: Repo + detailed context + reference examples  
**What happens**:
1. Embody has maximum context
2. Can generate highly tailored options
3. Understands nuanced requirements
4. First round is more refined

**Use case**: "I know exactly what I want, need professional execution"

### Anywhere In Between

**The spectrum is continuous** - users can provide as much or as little context as they want:
- Just a repo
- Repo + goal
- Repo + goal + constraints
- Repo + full context + examples + constraints

Embody adapts to what it receives.

---

## 🎨 Interaction Modes

### Simple Mode: Thumbs & Signals

**For**: Users who want fast decisions  
**Interaction**: 👍/👎 on generated options

**What the system learns**:
- Which directions resonate
- What qualities to prioritize
- What to avoid

**Example**:
```
Embody: [Shows 3 options]
User: 👍 Option A, 👎 Option C
Embody: "You liked the bold contrast approach. Here are 3 variations..."
User: 👍 Variation 2
Embody: "This direction is working. Should we finalize or explore more?"
```

**Time to decision**: 2-3 minutes

### Conversational Mode: Follow-up Questions

**For**: Users who want to collaborate more  
**Interaction**: Thumbs + simple text responses

**What the system learns**:
- Specific aspects they like/dislike
- Nuanced preferences
- Context for decisions

**Example**:
```
Embody: [Shows 3 options]
User: 👍 Option A, 👎 Option C
Embody: "What did you like about A?"
User: "The contrast, but the colors feel too intense"
Embody: "Got it - bold contrast with softer colors. Generating..."
```

**Time to decision**: 5-10 minutes

### Advanced Mode: Conceptual Manipulation

**For**: Users who want deep exploration  
**Interaction**: Conceptual questions and blending

**Examples**:

**Concept Removal**:
```
User: "Show me Rolex + Chipotle"
Embody: [Generates design with those aesthetics]
User: "Now remove Chipotle"
Embody: [Adjusts to pure Rolex aesthetic]
```

**Blending**:
```
User: "Mix the colors from Option A with the typography from Option B"
Embody: [Generates blended approach]
```

**Hypotheticals**:
```
User: "What if this was for a different audience?"
User: "How would this look in dark mode?"
User: "Show me this but 20% more bold"
```

**Time to decision**: 15-30 minutes (but deeper exploration)

---

## 🎭 User Archetypes

### The Builder

**Profile**: Engineer/maker building a product  
**Design skill**: Low to medium  
**What they bring**: Working code, clear product vision  
**What they need**: Professional design that doesn't slow them down

**Entry point**: Drop repo  
**Interaction mode**: Simple (thumbs)  
**Success metric**: "My product looks professional now"

**Example**: Solo developer building a SaaS tool

---

### The Visionary

**Profile**: Product person or entrepreneur with strong perspective  
**Design skill**: Medium (has taste, limited execution)  
**What they bring**: Clear vision, strong opinions, limited design vocabulary  
**What they need**: Help articulating their vision professionally

**Entry point**: Guided (answer questions)  
**Interaction mode**: Conversational  
**Success metric**: "This captures what I was imagining"

**Example**: Startup founder who knows the "vibe" but can't design it

---

### The Explorer

**Profile**: Anyone early in their design process  
**Design skill**: Varies  
**What they bring**: Uncertainty, need to see options  
**What they need**: Multiple directions to react to

**Entry point**: Minimal or guided  
**Interaction mode**: Simple → Conversational  
**Success metric**: "Now I know what direction I want"

**Example**: Team starting a rebrand, unsure of direction

---

### The Collaborator

**Profile**: Designer or sophisticated non-designer  
**Design skill**: Medium to high  
**What they bring**: Design vocabulary, nuanced preferences  
**What they need**: AI partner that understands design deeply

**Entry point**: Rich context  
**Interaction mode**: Advanced (conceptual)  
**Success metric**: "This elevated my thinking"

**Example**: Designer using AI to explore faster

---

### The Maintainer

**Profile**: Builder with existing design that needs to evolve  
**Design skill**: Varies  
**What they bring**: Existing design system, need to update/extend  
**What they need**: Consistent evolution of their design

**Entry point**: Drop repo (with existing design)  
**Interaction mode**: Simple → Conversational  
**Success metric**: "New features match our design perfectly"

**Example**: Team adding features to established product

---

## 🔄 User Journey Patterns

### Pattern 1: Quick Win

**User**: Builder who needs design now  
**Journey**:
```
1. Drop repo (30 seconds)
2. Embody analyzes + generates 3 options (15 seconds)
3. User picks one with 👍 (10 seconds)
4. Minor refinement (1-2 minutes)
5. Export and integrate (2 minutes)

Total: ~5 minutes
```

**Outcome**: Professional design system, ready to use

---

### Pattern 2: Discovery

**User**: Visionary exploring directions  
**Journey**:
```
1. Drop repo + answer questions (2 minutes)
2. Embody generates 3 options (15 seconds)
3. User explores with 👍/👎/details (3 minutes)
4. Refinement rounds (2-3 iterations, 10 minutes)
5. "This feels right" - finalize (2 minutes)

Total: ~20 minutes
```

**Outcome**: Design that captures their vision

---

### Pattern 3: Collaboration

**User**: Designer or advanced user  
**Journey**:
```
1. Rich context + examples (5 minutes)
2. Embody generates 4 options (20 seconds)
3. Deep exploration with conceptual questions (15 minutes)
4. Mix and match approaches (10 minutes)
5. Refinement with nuanced feedback (10 minutes)
6. Export with full documentation (5 minutes)

Total: ~45 minutes
```

**Outcome**: Highly refined design with documented rationale

---

### Pattern 4: Evolution

**User**: Maintainer updating existing design  
**Journey**:
```
1. Drop repo with existing design (30 seconds)
2. "I need to add dark mode" (10 seconds)
3. Embody generates dark mode variations (15 seconds)
4. Quick feedback and refinement (3 minutes)
5. Export updated tokens (1 minute)

Total: ~5 minutes
```

**Outcome**: Consistent evolution of existing design

---

## 🎓 Learning & Growth

### For Non-Designers

**Embody teaches design through interaction**:

**Vocabulary building**:
- System uses design terminology in context
- Explains choices in accessible language
- Shows rather than tells

**Pattern recognition**:
- User sees what works across iterations
- Builds intuition for design decisions
- Learns by doing, not studying

**Confidence building**:
- Success in early iterations builds momentum
- User learns they CAN have good design taste
- Reduces intimidation around design

**Referential learning**:
- System doesn't prescribe "the right way"
- Shows implications of choices
- Respects user's judgment and vision

### For Designers

**Embody accelerates design work**:

**Speed**:
- Explore more options in less time
- AI handles execution details
- Focus on high-level decisions

**Intelligence**:
- AI partner that understands design
- Elevates thinking through collaboration
- Catches edge cases and implications

**Documentation**:
- System captures design rationale automatically
- Easier handoff to engineering
- Design decisions preserved

---

## 🤝 Collaboration Model

### What User Brings

**Vision & Expertise**:
- Purpose behind what they're building
- Understanding of their users/context
- Perspective on how it should feel
- Domain expertise (their product/industry)

**Authority**:
- They are the expert in what they're trying to accomplish
- Final decisions are always theirs
- System suggests, user decides

### What Design Intelligence Brings

**Professional Craft**:
- Design best practices and patterns
- Accessibility and usability principles
- Visual hierarchy and composition
- Typography and color theory

**Execution**:
- Professional quality output
- Consistent systems thinking
- Technical design knowledge
- Fills gaps in design understanding

**Referential Support**:
- Shows implications of choices
- Offers perspectives, not prescriptions
- Helps externalize and examine ideas
- Supports thinking, doesn't replace it

### Together

**Co-creation**:
- Generator learns user's perspective
- Design intelligence ensures professional execution
- User discovers and articulates their vision
- Result feels authentically theirs, professionally done

**The Output**:
- Embodies the user's perspective
- Elevated by design intelligence
- Professionally executed
- Ready for implementation

---

## 📊 Success Metrics by User Type

### The Builder

- ✅ Time to professional design: < 10 minutes
- ✅ Confidence: "I can ship this"
- ✅ Quality: Passes basic design review
- ✅ Integration: Works with their code

### The Visionary

- ✅ Authenticity: "This feels like my vision"
- ✅ Communication: Others understand the direction
- ✅ Confidence: Ready to present to stakeholders
- ✅ Quality: Professional execution of their taste

### The Explorer

- ✅ Clarity: "Now I know what I want"
- ✅ Options: Saw diverse, high-quality directions
- ✅ Speed: Maintained creative momentum
- ✅ Decision: Confident in chosen direction

### The Collaborator

- ✅ Depth: "This elevated my thinking"
- ✅ Speed: Explored more in less time
- ✅ Quality: AI met their high standards
- ✅ Partnership: Felt like collaborating with expert

### The Maintainer

- ✅ Consistency: New design matches existing
- ✅ Speed: Kept pace with product evolution
- ✅ Quality: Professional additions
- ✅ System: Generator learned their aesthetic

---

## 🎯 Key Insights

### Universal Truths

1. **Everyone is a designer** - they have design intent, just not always execution ability
2. **Design intelligence for all** - like engineers use AI engineering tools, everyone benefits from AI design tools
3. **Perspective over prescription** - system helps express YOUR vision, not impose generic design
4. **Referential, not replacement** - supports thinking, doesn't replace it
5. **Collaboration, not automation** - co-creation between human vision and AI craft

### Why This Works

**For non-designers**: Access to professional design without learning to be a designer  
**For designers**: Speed and intelligence to work at higher velocity  
**For everyone**: Helps express design perspective with quality

### The Promise

**Embody doesn't replace designers. It makes everyone capable of expressing their design perspective with professional quality.**

---

**Built with [Amplifier](https://github.com/microsoft/amplifier)** 🤖

*Everyone is a designer. Embody helps you prove it.*
