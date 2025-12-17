---
profile:
  name: embody-default
  version: 1.0.0
  description: Design system exploration profile with cross-domain intelligence

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
      auto_compact: true

providers:
  - module: provider-anthropic
    source: git+https://github.com/microsoft/amplifier-module-provider-anthropic@main
    config:
      default_model: claude-sonnet-4-20250514
      debug: false

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

hooks: []
---

# Embody Default Profile

This profile configures Claude Sonnet with cross-domain intelligence for design system exploration.

## Collections Available

**developer-expertise**: zen-architect, modular-builder, researcher, bug-hunter  
**design-intelligence**: design-system-architect, component-designer, art-director  
**foundation**: explorer, session-finder  
**embody-collection**: context-gatherer, concept-generator, refinement-engine, documentation-builder

## Usage

API key is read from the `ANTHROPIC_API_KEY` environment variable.
