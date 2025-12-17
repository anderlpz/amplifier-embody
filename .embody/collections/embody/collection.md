---
collection:
  name: embody-collection
  version: 1.0.0
  description: Embody-specific agents for design system exploration workflows
  author: Embody Team
---

# Embody Collection

This collection contains agents specifically designed for Embody's design system exploration workflow.

## Agents

### context-gatherer
Parses designer intent from brief wizard inputs, infers implicit needs, and provides generation guidance.

### concept-generator
Creates 4 distinct design concepts based on parsed intent and current design tokens.

### refinement-engine
Evolves concepts iteratively based on designer feedback (👍/👎), building on what works.

### documentation-builder
Captures the complete design journey for engineering handoff, preserving rationale and decision history.

## Philosophy

These agents embody the principle: **Design is forming a point of view about a future state.**

They help designers:
- Externalize their perspective
- Explore multiple approaches
- Refine through feedback
- Document the journey

## Integration

Used with Amplifier Foundation's task tool:
```
Use the task tool with agent: embody-collection:context-gatherer
```
