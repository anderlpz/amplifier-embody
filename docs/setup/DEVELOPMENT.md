# Development Guide

## Setup

### Backend

```bash
cd backend
uv sync

# Or with pip
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
```

### Frontend

```bash
cd frontend
pnpm install
```

### Environment Variables

Create `.env` in project root:

```env
ANTHROPIC_API_KEY=sk-ant-...
```

## Running Locally

### Backend

```bash
cd backend
uvicorn backend.service:app --reload --port 8000
```

Backend runs at: http://localhost:8000

### Frontend

```bash
cd frontend
pnpm dev
```

Frontend runs at: http://localhost:3456

## Project Structure

```
amplifier-embody/
├── backend/                      # FastAPI backend
│   ├── service.py                # Main API service
│   ├── session_manager.py        # Session lifecycle
│   ├── foundation_integration.py # Amplifier wrapper
│   ├── agents/                   # (placeholder - agents in collections)
│   └── exporters/                # Token exporters
│       ├── figma_tokens.py
│       ├── css_variables.py
│       └── tailwind_config.py
│
├── frontend/                     # Next.js frontend
│   ├── app/                      # App router
│   │   ├── page.tsx              # Home page
│   │   └── api/                  # API routes (proxy)
│   ├── components/
│   │   ├── ContextWizard/
│   │   ├── ConceptGallery/
│   │   ├── FeedbackPanel/
│   │   └── DocumentationBuilder/
│   └── lib/
│       └── embody-client.ts      # API client
│
├── .embody/                      # Amplifier configuration
│   ├── profiles/                 # Profile bundles
│   │   └── default.md
│   ├── collections/              # Agent collections
│   │   └── embody/               # Embody-specific agents
│   │       ├── collection.md
│   │       └── agents/
│   │           ├── context-gatherer.md
│   │           ├── concept-generator.md
│   │           ├── refinement-engine.md
│   │           └── documentation-builder.md
│   ├── modules/                  # Downloaded modules (gitignored)
│   └── sessions/                 # Session data (gitignored)
│
├── docs/
│   ├── DEVELOPMENT.md            # This file
│   ├── API.md                    # API documentation
│   └── AGENTS.md                 # Agent development guide
│
├── EXPERIENCE_SPEC.md            # UX specification
├── BACKEND_ARCHITECTURE.md       # Technical architecture
└── README.md                     # Project overview
```

## Development Workflow

### 1. Create a Session

```bash
curl -X POST http://localhost:8000/api/sessions/create \
  -H "Content-Type: application/json" \
  -d '{"repo_path": "/path/to/your/project"}'
```

Returns:
```json
{
  "session_id": "abc-123-def",
  "tokens": {
    "colors": {...},
    "typography": {...}
  }
}
```

### 2. Gather Context

```bash
curl -X POST http://localhost:8000/api/sessions/abc-123-def/gather-context \
  -H "Content-Type: application/json" \
  -d '{
    "goal": "Rebrand - more modern feel",
    "qualities": ["bold", "modern", "accessible"],
    "constraints": []
  }'
```

### 3. Generate Concepts

```bash
curl -X POST http://localhost:8000/api/sessions/abc-123-def/generate-concepts
```

### 4. Provide Feedback & Refine

```bash
curl -X POST http://localhost:8000/api/sessions/abc-123-def/refine \
  -H "Content-Type: application/json" \
  -d '{
    "feedback": {
      "liked": ["concept-a"],
      "disliked": ["concept-c"]
    }
  }'
```

### 5. Finalize

```bash
curl -X POST http://localhost:8000/api/sessions/abc-123-def/finalize \
  -H "Content-Type: application/json" \
  -d '{"selected_concept_id": "concept-a-variation-2"}'
```

## Adding New Agents

See [docs/AGENTS.md](./AGENTS.md) for agent development guide.

## Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
pnpm test
```

## Debugging

### Backend Logging

Set log level in `.env`:
```env
LOG_LEVEL=DEBUG
```

### Frontend DevTools

React DevTools and Next.js debug mode available in browser.

### Amplifier Debugging

Add to profile:
```yaml
providers:
  - module: provider-anthropic
    config:
      debug: true  # Enable Amplifier debug logging
```

## Common Issues

### "Profile directory not found"
```bash
mkdir -p .embody/profiles
cp .embody/profiles/default.md.example .embody/profiles/default.md
```

### "ANTHROPIC_API_KEY not set"
Add to `.env` file in project root.

### "Module download failed"
Check git sources in profile are accessible.

## Contributing

See main [README.md](../README.md) for contribution guidelines.
