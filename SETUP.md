# Quick Setup Guide

## Prerequisites

- Python 3.11+
- Node.js 18+
- pnpm (or npm)
- Anthropic API key

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/anderlpz/amplifier-embody.git
cd amplifier-embody
```

### 2. Set up environment

```bash
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

### 3. Install backend dependencies

```bash
cd backend
uv sync  # Recommended
# OR
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e .
cd ..
```

### 4. Install frontend dependencies

```bash
cd frontend
pnpm install
cd ..
```

## Running

### Start Backend (Terminal 1)

```bash
cd backend
uvicorn backend.service:app --reload --port 8000
```

Backend runs at: http://localhost:8000

### Start Frontend (Terminal 2)

```bash
cd frontend
pnpm dev
```

Frontend runs at: http://localhost:3456

## First Use

1. Open http://localhost:3456
2. Connect a repository with design tokens
3. Answer 2-3 context questions
4. Explore 4 generated design concepts
5. Provide feedback (👍/👎)
6. Refine until satisfied
7. Export documentation for engineering

## Troubleshooting

### "ANTHROPIC_API_KEY not set"
Make sure `.env` file exists in project root with your API key.

### "Module not found"
First run downloads Amplifier modules from git. This takes ~60 seconds.

### "Profile directory not found"
The `.embody/profiles/default.md` should exist. Check if git cloned all files.

## Next Steps

See [docs/DEVELOPMENT.md](./docs/DEVELOPMENT.md) for detailed development guide.
