# Embody Development Roadmap

> **Phased rollout strategy for building a design system generator with Amplifier**

**Version**: 1.0.0  
**Created**: December 17, 2025 at 15:22 PST  
**Purpose**: Define development phases, priorities, and Amplifier contribution strategy

---

## 🎯 Vision & Strategy

### Core Principle

**Build for Amplifier from day one**. Every component should be designed as a potential contribution back to the Amplifier ecosystem.

**Not**: "An app that uses Amplifier"  
**But**: "Amplifier modules that compose into an app"

### Contribution Strategy

Components developed in Embody fall into three categories:

1. **Amplifier Contributions**: Could be official Amplifier modules/collections
2. **Embody-Specific**: Unique to Embody but following Amplifier patterns
3. **Experimental**: Testing concepts that might inform future Amplifier features

---

## 📅 Development Phases

### Phase 0: Foundation (Current)

**Status**: ✅ Completed  
**Timeline**: Week of Dec 16, 2025

**Deliverables**:
- ✅ Architecture specifications (BACKEND_ARCHITECTURE.md)
- ✅ Experience specifications (EXPERIENCE_SPEC.md)
- ✅ User research and personas (USERS.md)
- ✅ Product vision and philosophy (README.md)
- ✅ Roadmap and contribution strategy (this document)

**Amplifier-Ready Components Identified**:
- `embody-collection` (agents for design generation)
- `amplifier-module-design-tokens` (token extraction/conversion)
- `amplifier-module-embody-ui` (UI orchestration)

---

### Phase 1: MVP - Repo-Based Design Generation

**Goal**: Minimal viable product for Amplifier users with existing codebases

**Timeline**: Weeks 1-4 (Jan 2026)

#### Week 1-2: Backend Foundation

**Build**:
- ✅ Amplifier Foundation integration
- 🔲 Session management (embody-specific)
- 🔲 Token extraction module (Amplifier contribution candidate)
- 🔲 `embody-collection` agents:
  - `context-gatherer.md`
  - `concept-generator.md`
  - `refinement-engine.md`
  - `documentation-builder.md`

**Amplifier Contribution Candidates**:
- `amplifier-module-design-tokens`: Standalone utility for token extraction
- `embody-collection`: Design intelligence agents

**Deliverables**:
- Working backend that can analyze repos
- Design concept generation via agents
- Session state management

---

#### Week 3-4: Minimal UI & Integration

**Build**:
- 🔲 Next.js frontend shell
- 🔲 Repo drop interface
- 🔲 Simple concept gallery (3 cards)
- 🔲 Thumbs up/down feedback
- 🔲 Basic export (CSS variables, Figma tokens)

**Amplifier Contribution Candidates**:
- `amplifier-module-embody-ui`: UI layer that could be reusable

**Deliverables**:
- End-to-end flow: Repo → Concepts → Feedback → Export
- Usable by Amplifier team for dogfooding

---

### Phase 1.5: Dogfood & Iterate

**Goal**: Internal testing with Amplifier team

**Timeline**: Week 5 (Feb 2026)

**Activities**:
- Amplifier team uses Embody for their own projects
- Collect feedback on UX and quality
- Identify bugs and missing features
- Validate Amplifier contribution strategy

**Success Metrics**:
- 5+ Amplifier team members use it
- At least 1 production design system created
- Feedback incorporated into Phase 2 plan

---

### Phase 2: Enhanced Interaction & Context

**Goal**: Better collaboration and richer entry points

**Timeline**: Weeks 6-10 (Feb-Mar 2026)

#### Core Features

**Conversational Mode**:
- 🔲 Follow-up questions after thumbs feedback
- 🔲 "What did you like about this?" prompts
- 🔲 Natural language refinement requests

**Rich Entry Points**:
- 🔲 Guided context wizard (2-3 questions)
- 🔲 Reference image uploads ("make it feel like this")
- 🔲 Design constraint specification
- 🔲 Brand asset integration (logos, colors)

**No-Repo Entry** (P2):
- 🔲 Text description of intended project
- 🔲 Embody generates design without codebase
- 🔲 Design-first workflow enabled

**Advanced Export**:
- 🔲 Tailwind config export
- 🔲 Figma plugin integration
- 🔲 Design documentation generation
- 🔲 Component library scaffolding

**Amplifier Contribution Candidates**:
- Enhanced `embody-collection` agents
- `amplifier-module-design-export`: Export utilities for multiple formats

---

### Phase 3: Advanced Collaboration & Learning

**Goal**: Conceptual manipulation and generator training

**Timeline**: Weeks 11-16 (Mar-Apr 2026)

#### Core Features

**Conceptual Manipulation**:
- 🔲 "Show me Rolex + Chipotle" blending
- 🔲 "Remove Chipotle" concept subtraction
- 🔲 Mix-and-match between concepts
- 🔲 Hypothetical explorations ("20% more bold")

**Generator Training**:
- 🔲 Persistent generator state across sessions
- 🔲 "Remember my aesthetic" feature
- 🔲 Generator export/import for reuse
- 🔲 Cross-project aesthetic consistency

**Learning Features**:
- 🔲 Design rationale explanations
- 🔲 "Why this works" educational overlays
- 🔲 Design principle suggestions
- 🔲 Accessibility guidance

**Multi-Context Generation**:
- 🔲 Generate for web + mobile + print simultaneously
- 🔲 Responsive design system generation
- 🔲 Dark mode automatic generation
- 🔲 Platform-specific variations

**Amplifier Contribution Candidates**:
- `amplifier-collection-design-education`: Educational design agents
- Enhanced `embody-collection` with advanced manipulation

---

### Phase 4: Team Collaboration & Scale

**Goal**: Multi-user workflows and organizational scale

**Timeline**: Weeks 17-24 (Apr-Jun 2026)

#### Core Features

**Team Features**:
- 🔲 Shared sessions (multiple users, one generator)
- 🔲 Voting on concepts (team consensus)
- 🔲 Comments and annotations
- 🔲 Async collaboration (leave feedback, return to results)

**Organization Features**:
- 🔲 Org-wide aesthetic guidelines
- 🔲 Brand consistency enforcement
- 🔲 Generator templates for teams
- 🔲 Reusable design constraints

**Integration**:
- 🔲 GitHub integration (design PRs)
- 🔲 Figma two-way sync
- 🔲 Component library generation
- 🔲 CI/CD design system updates

**Amplifier Module Packaging**:
- 🔲 Package Embody as `amplifier-module-embody`
- 🔲 Installable via Amplifier profiles
- 🔲 Use within any Amplifier session
- 🔲 Contribute tested modules back to Amplifier

---

## 🎁 Amplifier Contribution Roadmap

### Immediate Contributions (Phase 1)

**`amplifier-module-design-tokens`**:
- **Purpose**: Extract and convert design tokens from codebases
- **Functionality**:
  - Parse CSS, SCSS, Tailwind config, CSS-in-JS
  - Extract colors, typography, spacing, effects
  - Convert between formats (Figma tokens, CSS variables, Tailwind)
- **Why valuable**: Useful for any Amplifier project needing design context
- **Contribution timeline**: End of Phase 1 (Week 4)

**`embody-collection`**:
- **Purpose**: Design intelligence agents for generation and refinement
- **Agents**:
  - `context-gatherer`: Parse design intent into constraints
  - `concept-generator`: Generate design system variations
  - `refinement-engine`: Train generator based on feedback
  - `documentation-builder`: Export systems with documentation
- **Why valuable**: Design intelligence for all Amplifier users
- **Contribution timeline**: End of Phase 1 (Week 4)

---

### Future Contributions (Phase 2-3)

**`amplifier-module-design-export`**:
- **Purpose**: Export design systems to multiple formats
- **Formats**: Figma, CSS, Tailwind, styled-components, Chakra UI
- **Why valuable**: Standard export utilities for design tooling
- **Contribution timeline**: Phase 2 (Week 10)

**`amplifier-collection-design-education`**:
- **Purpose**: Educational agents that explain design principles
- **Why valuable**: Helps all users learn design while working
- **Contribution timeline**: Phase 3 (Week 16)

**`amplifier-module-embody-ui`**:
- **Purpose**: UI orchestration layer for design tools
- **Why valuable**: Reusable UI patterns for design-focused Amplifier apps
- **Contribution timeline**: Phase 4 (Week 20)

---

## 📊 Success Metrics by Phase

### Phase 1: MVP
- ✅ End-to-end flow works (repo → design)
- ✅ Amplifier team can use it
- ✅ At least 1 module ready for contribution review
- ✅ Time to first design: < 5 minutes

### Phase 2: Enhanced
- ✅ Conversational refinement works
- ✅ Non-repo entry point validated
- ✅ 2+ modules contributed to Amplifier
- ✅ 10+ users outside Amplifier team

### Phase 3: Advanced
- ✅ Conceptual manipulation works
- ✅ Generator training persists across sessions
- ✅ Educational features reduce design questions
- ✅ 50+ users

### Phase 4: Scale
- ✅ Team collaboration works
- ✅ Embody packaged as Amplifier module
- ✅ All reusable components contributed
- ✅ 200+ users

---

## 🏗️ Technical Architecture Alignment

### Amplifier-First Principles

**Every component developed follows Amplifier patterns**:

1. **Module-based**: Each feature is an Amplifier module
2. **Profile-driven**: Configuration via Amplifier profiles
3. **Collection-based**: Agents organized in collections
4. **Foundation-native**: Uses Amplifier Foundation primitives
5. **Composable**: Modules work independently or together

### Repository Structure

```
amplifier-embody/                    # Main app repository
├── .embody/
│   ├── profiles/
│   │   └── default.md              # Embody profile
│   └── collections/
│       └── embody/                 # embody-collection (contribution candidate)
│           ├── collection.md
│           └── agents/
│               ├── context-gatherer.md
│               ├── concept-generator.md
│               ├── refinement-engine.md
│               └── documentation-builder.md
├── backend/
│   └── service.py                  # FastAPI service
├── app/                            # Next.js frontend
└── modules/                        # Module development area
    ├── design-tokens/              # amplifier-module-design-tokens
    ├── design-export/              # amplifier-module-design-export
    └── embody-ui/                  # amplifier-module-embody-ui

Separate repositories for contributions:
├── amplifier-module-design-tokens/ # Standalone repo
├── amplifier-module-design-export/ # Standalone repo
└── amplifier-collection-embody/    # Standalone repo
```

### Contribution Workflow

**For each module/collection**:
1. Develop in `amplifier-embody/modules/`
2. Test thoroughly within Embody
3. Extract to standalone repository
4. Follow Amplifier contribution guidelines
5. Submit PR to Amplifier ecosystem
6. Once accepted, reference official module in Embody

---

## 🎓 Learning & Validation

### Dogfooding Strategy

**Phase 1**: Amplifier team uses Embody internally  
**Phase 2**: Amplifier community early access  
**Phase 3**: Public beta with feedback loop  
**Phase 4**: General availability

### Feedback Loops

**Weekly**:
- User session recordings review
- Bug triage and prioritization
- Feature request evaluation

**Bi-weekly**:
- Amplifier team sync (contribution alignment)
- Design quality review
- Module extraction planning

**Monthly**:
- Roadmap adjustment based on learnings
- Contribution readiness assessment
- Community showcase and demos

---

## ⚠️ Risks & Mitigations

### Risk 1: Contribution Rejection

**Risk**: Modules don't meet Amplifier standards  
**Mitigation**: 
- Weekly alignment with Amplifier team
- Follow Amplifier contribution guidelines from day 1
- Test modules in multiple contexts before contribution

### Risk 2: Premature Optimization

**Risk**: Building too much before validating  
**Mitigation**:
- Strict phase gating (no Phase 2 until Phase 1 validated)
- Dogfood at every phase
- Measure real usage, not assumptions

### Risk 3: Scope Creep

**Risk**: Adding features that don't serve core mission  
**Mitigation**:
- Every feature must serve "express design with quality"
- Amplifier contribution test: "Would this be valuable elsewhere?"
- User job validation: "Which job does this serve?"

### Risk 4: Quality vs Speed

**Risk**: Rushing features reduces design quality  
**Mitigation**:
- Use Embody to design Embody (meta validation)
- Design intelligence reviews every feature
- No shipped feature below 9/10 quality bar

---

## 🔮 Future Exploration (Beyond Phase 4)

### Potential Features

**AI Design Critic**:
- Automated design review
- Accessibility audit
- Best practice validation

**Design System Evolution**:
- Automatic migrations (v1 → v2)
- Deprecation management
- Component usage analytics

**Real-time Collaboration**:
- Live co-design sessions
- Multiplayer design exploration
- Shared generator training

**Platform Expansion**:
- Mobile app design
- Print design systems
- Motion design generation

### Research Areas

**Generator Architecture**:
- How do we encode taste mathematically?
- What makes a "good" design system?
- How do we measure coherence?

**Design Intelligence**:
- What design principles can be automated?
- How do we balance AI assistance vs creative control?
- When should AI suggest vs execute?

---

## 📈 Long-term Vision

**Year 1**: Embody is the go-to design tool for Amplifier users  
**Year 2**: Embody modules are standard parts of Amplifier ecosystem  
**Year 3**: Design intelligence is as common as code intelligence

**Ultimate Goal**: **Everyone can express their design perspective with professional quality, just like Amplifier helps everyone build with engineering quality.**

---

## 🤝 Contributing

See [CONTRIBUTING_TO_AMPLIFIER.md](./CONTRIBUTING_TO_AMPLIFIER.md) for detailed information on:
- Module extraction process
- Contribution guidelines
- Testing requirements
- Documentation standards

---

## 📞 Contact & Feedback

**Embody Team**: [TBD]  
**Amplifier Team Sync**: Weekly Fridays  
**Community**: [Amplifier Discord/Discussions]

---

**Built with [Amplifier](https://github.com/microsoft/amplifier)** 🤖

*Every component designed to give back to the ecosystem that makes it possible.*
