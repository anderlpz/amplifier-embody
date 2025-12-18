# Contributing to Amplifier Ecosystem

> **Module extraction, testing, and contribution strategy for Embody components**

**Version**: 1.0.0  
**Created**: December 17, 2025 at 15:24 PST  
**Purpose**: Guide for extracting Embody components and contributing them back to Amplifier

---

## 🎯 Philosophy

**We build for Amplifier from day one.**

Every component in Embody is designed with the Amplifier ecosystem in mind. Our goal is not just to use Amplifier, but to **give back** by contributing tested, production-ready modules and collections that benefit all Amplifier users.

### Core Principles

1. **Amplifier-First Architecture**: Every component follows Amplifier patterns
2. **Modularity**: Components work independently when possible
3. **Quality Standards**: Contributions meet or exceed Amplifier quality bar
4. **Documentation**: Every contribution is thoroughly documented
5. **Testing**: Comprehensive test coverage before contribution
6. **Community Value**: Contributions solve problems beyond Embody

---

## 📦 Contribution Candidates

### Identified Components

See [BACKEND_ARCHITECTURE.md](./BACKEND_ARCHITECTURE.md#-amplifier-contribution-strategy) for detailed descriptions. Summary:

**High Priority** (Phase 1):
- `amplifier-module-design-tokens`: Token extraction and conversion
- `embody-collection`: Design intelligence agents

**Medium Priority** (Phase 2):
- `amplifier-module-design-export`: Multi-format export utilities

**Lower Priority** (Phase 3-4):
- `amplifier-module-embody-ui`: UI components for design tools
- `amplifier-collection-design-education`: Educational design agents

---

## 🔄 Contribution Workflow

### Phase 1: Development in Embody

**Location**: Develop within `amplifier-embody` repository

```
amplifier-embody/
├── .embody/collections/embody/          # Agent collections
├── backend/                             # Embody backend
├── app/                                 # Embody UI
└── modules/                             # Module development area
    ├── design-tokens/                   # Develop modules here
    ├── design-export/
    └── embody-ui/
```

**During this phase**:
- Build features as part of Embody
- Test within Embody's context
- Iterate based on real usage
- Dogfood with Amplifier team
- Validate design and API decisions

**Why develop here first?**
- Real-world validation
- Faster iteration
- Clear use cases
- Production testing

---

### Phase 2: Prepare for Extraction

**Before extracting**, ensure the component:

#### 1. Is Self-Contained

```python
# ✅ Good: Clear dependencies, minimal coupling
class DesignTokenExtractor:
    """Extract design tokens from code files."""
    
    def __init__(self, file_patterns: list[str]):
        self.patterns = file_patterns
    
    def extract(self, repo_path: Path) -> DesignTokens:
        """Extract tokens from repository."""
        # Self-contained logic
        pass

# ❌ Bad: Tightly coupled to Embody internals
class DesignTokenExtractor:
    def __init__(self, embody_session, embody_ui_state):
        self.session = embody_session  # Embody-specific
        self.ui = embody_ui_state      # Embody-specific
```

#### 2. Has Clear Interfaces

```python
# ✅ Good: Clear input/output types
@dataclass
class DesignTokens:
    colors: dict[str, str]
    typography: dict[str, Any]
    spacing: dict[str, str]
    effects: dict[str, Any]

def extract_tokens(repo_path: Path) -> DesignTokens:
    """Clear interface, typed inputs/outputs."""
    pass

# ❌ Bad: Unclear interface, loose types
def do_stuff(thing) -> dict:
    """What does this return? What is 'thing'?"""
    pass
```

#### 3. Is Documented

Every public function/class needs:
- Docstring explaining purpose
- Parameter descriptions
- Return value descriptions
- Usage examples
- Edge case handling

```python
def extract_tokens(repo_path: Path) -> DesignTokens:
    """
    Extract design tokens from a repository.
    
    Parses CSS, SCSS, Tailwind config, and CSS-in-JS files to extract
    colors, typography, spacing, and effects tokens.
    
    Args:
        repo_path: Path to repository root directory
        
    Returns:
        DesignTokens containing extracted token categories
        
    Raises:
        ValueError: If repo_path doesn't exist
        TokenExtractionError: If no parseable files found
        
    Example:
        ```python
        tokens = extract_tokens(Path("/path/to/repo"))
        print(f"Found {len(tokens.colors)} color tokens")
        ```
    """
    pass
```

#### 4. Has Comprehensive Tests

```python
# tests/test_token_extraction.py
import pytest
from pathlib import Path
from design_tokens import extract_tokens

class TestTokenExtraction:
    """Test design token extraction."""
    
    def test_extracts_css_variables(self, tmp_path):
        """Should extract CSS custom properties."""
        css_file = tmp_path / "styles.css"
        css_file.write_text(":root { --color-primary: #007bff; }")
        
        tokens = extract_tokens(tmp_path)
        
        assert "primary" in tokens.colors
        assert tokens.colors["primary"] == "#007bff"
    
    def test_handles_missing_repo(self):
        """Should raise ValueError for non-existent path."""
        with pytest.raises(ValueError):
            extract_tokens(Path("/nonexistent"))
    
    def test_handles_empty_repo(self, tmp_path):
        """Should return empty tokens for repo with no design files."""
        tokens = extract_tokens(tmp_path)
        
        assert len(tokens.colors) == 0
        assert len(tokens.typography) == 0
```

**Test Coverage Requirements**:
- Unit tests: > 80% coverage
- Integration tests: Key workflows
- Edge cases: Error handling, empty inputs, invalid data
- Documentation: Examples that actually work

---

### Phase 3: Extract to Standalone Repository

**Create new repository** following Amplifier conventions:

```bash
# Example: amplifier-module-design-tokens
mkdir amplifier-module-design-tokens
cd amplifier-module-design-tokens

# Initialize with standard structure
.
├── README.md                    # Comprehensive documentation
├── pyproject.toml              # Python dependencies
├── LICENSE                     # MIT (match Amplifier)
├── .gitignore
├── src/
│   └── amplifier_design_tokens/
│       ├── __init__.py
│       ├── extractor.py        # Core extraction logic
│       ├── parser.py           # File parsing
│       ├── converter.py        # Format conversion
│       └── types.py            # Data models
├── tests/
│   ├── __init__.py
│   ├── test_extractor.py
│   ├── test_parser.py
│   ├── test_converter.py
│   └── fixtures/               # Test data
└── docs/
    ├── usage.md
    ├── api.md
    └── examples/
```

**Copy code from Embody**, removing Embody-specific dependencies:

```python
# Before (in Embody)
from embody.backend.session import EmbodySession
from embody.backend.utils import log_to_embody

def extract_tokens(session: EmbodySession, repo_path: Path):
    log_to_embody(session, "Extracting tokens...")
    # ...

# After (standalone)
import logging

logger = logging.getLogger(__name__)

def extract_tokens(repo_path: Path) -> DesignTokens:
    logger.info(f"Extracting tokens from {repo_path}")
    # ...
```

---

### Phase 4: Documentation

#### README.md Template

```markdown
# amplifier-module-design-tokens

Extract and convert design tokens from codebases.

## Installation

```bash
pip install amplifier-module-design-tokens
```

## Quick Start

```python
from amplifier_design_tokens import extract_tokens

tokens = extract_tokens("/path/to/repo")
print(f"Found {len(tokens.colors)} colors")
```

## Features

- Extract tokens from CSS, SCSS, Tailwind, CSS-in-JS
- Convert between formats (Figma, CSS variables, Tailwind)
- Token analysis and classification
- Support for custom token patterns

## Usage

### Basic Extraction

[Detailed examples...]

### Format Conversion

[Detailed examples...]

### Custom Patterns

[Detailed examples...]

## API Reference

See [docs/api.md](./docs/api.md)

## Contributing

[Contribution guidelines]

## License

MIT
```

#### pyproject.toml

```toml
[project]
name = "amplifier-module-design-tokens"
version = "0.1.0"
description = "Extract and convert design tokens from codebases"
authors = [
    {name = "Embody Team", email = "embody@example.com"}
]
requires-python = ">=3.11"
license = {text = "MIT"}
readme = "README.md"

dependencies = [
    "pydantic>=2.0.0",
    # Minimal dependencies
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "black>=23.0.0",
    "mypy>=1.0.0",
    "ruff>=0.0.280",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]

[tool.coverage.run]
source = ["src"]
omit = ["*/tests/*"]

[tool.coverage.report]
fail_under = 80
```

---

### Phase 5: Testing Standalone

**Test outside Embody context**:

```bash
# Clone standalone repo
git clone git@github.com:yourorg/amplifier-module-design-tokens.git
cd amplifier-module-design-tokens

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest tests/ -v --cov=src

# Test in fresh Python environment
python3 -m venv test_env
source test_env/bin/activate
pip install .

# Try usage example from README
python examples/basic_usage.py
```

**Test in different Amplifier project**:

```yaml
# .amplifier/profiles/test.md in different project
tools:
  - module: design-tokens
    source: git+https://github.com/yourorg/amplifier-module-design-tokens@main

# Verify it works without Embody
```

---

### Phase 6: Contribution Submission

#### Pre-submission Checklist

**Code Quality**:
- [ ] All tests passing
- [ ] Test coverage > 80%
- [ ] No linting errors (ruff, mypy)
- [ ] Code formatted (black)
- [ ] No Embody-specific dependencies

**Documentation**:
- [ ] README.md complete with examples
- [ ] API documentation generated
- [ ] Usage examples tested
- [ ] CHANGELOG.md initialized
- [ ] LICENSE file (MIT)

**Amplifier Integration**:
- [ ] Works as standalone module
- [ ] Follows Amplifier naming conventions
- [ ] Compatible with Amplifier Foundation
- [ ] Tested in non-Embody Amplifier project

**Community Value**:
- [ ] Solves problem beyond Embody
- [ ] Clear use cases documented
- [ ] Potential users identified
- [ ] Comparison with alternatives (if any)

#### Submission Process

1. **Open Discussion** (before PR):
   ```markdown
   **Title**: Proposal: amplifier-module-design-tokens
   
   **Summary**: Module for extracting design tokens from codebases
   
   **Motivation**: 
   - Many Amplifier projects need design context
   - Currently no standard way to extract tokens
   - Useful for code analysis, docs, migrations
   
   **Proposed API**:
   [Code examples]
   
   **Use Cases**:
   1. Embody: Design system generation
   2. Documentation: Auto-generate design docs
   3. Migration: Extract tokens for redesigns
   
   **Questions for Community**:
   - API design feedback?
   - Missing features?
   - Naming conventions?
   ```

2. **Address Feedback**: Iterate on design based on discussion

3. **Submit PR** to Amplifier ecosystem repo (or follow contribution process)

4. **Code Review**: Address reviewer feedback

5. **Documentation Review**: Ensure docs are clear

6. **Acceptance**: Module officially published

7. **Update Embody**: Switch to official module

---

## 🧪 Testing Strategy

### Unit Tests

**Test each function in isolation**:

```python
def test_parse_css_variable():
    """Test CSS variable parsing."""
    css = ":root { --color-primary: #007bff; }"
    result = parse_css_variables(css)
    assert result == {"primary": "#007bff"}

def test_parse_invalid_css():
    """Test handling of malformed CSS."""
    css = ":root { --color-primary #007bff }"  # Missing colon
    with pytest.raises(ParseError):
        parse_css_variables(css)
```

### Integration Tests

**Test complete workflows**:

```python
def test_extract_and_convert_workflow(tmp_path):
    """Test full extraction and conversion workflow."""
    # Setup: Create test repo
    css_file = tmp_path / "styles.css"
    css_file.write_text(":root { --color-primary: #007bff; }")
    
    # Extract
    tokens = extract_tokens(tmp_path)
    
    # Convert
    figma = convert_to_figma(tokens)
    css = convert_to_css(tokens)
    tailwind = convert_to_tailwind(tokens)
    
    # Verify all formats
    assert "primary" in figma["colors"]
    assert "--color-primary" in css
    assert "primary" in tailwind["theme"]["colors"]
```

### Edge Case Tests

**Test error conditions and boundaries**:

```python
def test_handles_empty_files():
    """Empty files should return empty tokens."""
    
def test_handles_binary_files():
    """Binary files should be skipped gracefully."""
    
def test_handles_very_large_repos():
    """Should handle repos with 10k+ files."""
    
def test_handles_circular_imports():
    """CSS with circular @imports should not hang."""
```

### Performance Tests

**For modules that process large data**:

```python
import time

def test_extraction_performance():
    """Extraction should complete in reasonable time."""
    large_repo = create_test_repo_with_1000_files()
    
    start = time.time()
    tokens = extract_tokens(large_repo)
    duration = time.time() - start
    
    assert duration < 5.0  # Should complete in < 5 seconds
```

---

## 📚 Documentation Standards

### Docstring Format

Use Google-style docstrings:

```python
def convert_to_figma(tokens: DesignTokens) -> dict:
    """
    Convert design tokens to Figma tokens JSON format.
    
    Transforms extracted design tokens into the format expected by
    Figma's token plugin. Handles colors, typography, spacing, and effects.
    
    Args:
        tokens: Extracted design tokens to convert
        
    Returns:
        Dictionary in Figma tokens JSON format
        
    Raises:
        ConversionError: If tokens contain unsupported types
        
    Example:
        >>> tokens = extract_tokens("/path/to/repo")
        >>> figma_json = convert_to_figma(tokens)
        >>> print(figma_json["colors"]["primary"])
        {"value": "#007bff", "type": "color"}
        
    See Also:
        - convert_to_css: Convert to CSS variables
        - convert_to_tailwind: Convert to Tailwind config
    """
    pass
```

### README Sections

Every README should include:

1. **One-line description**
2. **Installation instructions**
3. **Quick start example** (< 10 lines)
4. **Features list**
5. **Detailed usage examples**
6. **API reference** (or link to docs)
7. **Contributing guidelines**
8. **License**

### Usage Examples

Provide examples for:
- Basic usage (happy path)
- Common customizations
- Error handling
- Integration with Amplifier
- Advanced use cases

---

## 🏗️ Module Architecture Patterns

### Pattern 1: Pure Utility Module

**Example**: `amplifier-module-design-tokens`

**Characteristics**:
- No Amplifier-specific dependencies
- Standalone Python package
- Used via direct import
- Can be used outside Amplifier

**Structure**:
```python
# Pure functions, clear interfaces
def extract_tokens(repo_path: Path) -> DesignTokens:
    """Standalone utility function."""
    pass

# No Amplifier coupling
# No session state
# No UI dependencies
```

**Integration with Amplifier**:
```yaml
# Profile references it, but module is independent
tools:
  - module: design-tokens
    source: git+https://github.com/microsoft/amplifier-module-design-tokens@main
```

---

### Pattern 2: Amplifier-Native Module

**Example**: `amplifier-module-embody-ui`

**Characteristics**:
- Designed for Amplifier Foundation
- Uses Amplifier abstractions
- Session-aware
- Follows Amplifier patterns

**Structure**:
```python
from amplifier.foundation import Module, Capability

class EmbodyUIModule(Module):
    """Amplifier-native module."""
    
    async def mount(self, session: Session):
        """Mount capabilities into session."""
        session.register_capability("ui.show_concepts", self.show_concepts)
    
    async def show_concepts(self, concepts: list[Concept]):
        """Capability implementation."""
        pass
```

---

### Pattern 3: Agent Collection

**Example**: `embody-collection`

**Characteristics**:
- Collection of agent prompts
- Follows collection.md format
- Loaded via Amplifier profiles
- No code, just agents

**Structure**:
```
embody-collection/
├── collection.md                # Metadata
└── agents/
    ├── context-gatherer.md      # Agent prompts
    ├── concept-generator.md
    ├── refinement-engine.md
    └── documentation-builder.md
```

**No code to test** - validate by using agents in real sessions.

---

## 🔍 Code Review Checklist

Before submitting for contribution review:

### Architecture
- [ ] Component is self-contained
- [ ] Clear separation of concerns
- [ ] Minimal external dependencies
- [ ] Follows single responsibility principle
- [ ] No tight coupling to Embody

### Code Quality
- [ ] Type hints on all functions
- [ ] Docstrings on all public APIs
- [ ] Error handling for edge cases
- [ ] Logging for debugging
- [ ] No hard-coded paths/values

### Testing
- [ ] Unit tests for all functions
- [ ] Integration tests for workflows
- [ ] Edge case tests
- [ ] Test coverage > 80%
- [ ] All tests passing

### Documentation
- [ ] README with examples
- [ ] API documentation
- [ ] Usage examples that work
- [ ] CHANGELOG.md
- [ ] LICENSE file

### Amplifier Integration
- [ ] Works standalone
- [ ] Follows naming conventions
- [ ] Compatible with Foundation
- [ ] Profile integration documented

### Community Value
- [ ] Clear use cases
- [ ] Solves general problem
- [ ] Potential users identified
- [ ] Comparison with alternatives

---

## 🚀 Post-Contribution

### After Acceptance

1. **Announce** in Amplifier community
2. **Update Embody** to use official module
3. **Monitor usage** and gather feedback
4. **Maintain** with bug fixes and improvements
5. **Support** community users

### Maintenance Responsibilities

**As module maintainer**:
- Respond to issues promptly
- Review and merge PRs
- Release updates regularly
- Keep documentation current
- Coordinate with Amplifier team

### Versioning

Follow semantic versioning:
- **Major**: Breaking changes
- **Minor**: New features (backward compatible)
- **Patch**: Bug fixes

```toml
# Version bump examples
0.1.0 → 0.1.1  # Bug fix
0.1.1 → 0.2.0  # New feature
0.2.0 → 1.0.0  # Breaking change / stable release
```

---

## 📊 Success Metrics

### For Each Contribution

**Adoption**:
- Number of projects using the module
- GitHub stars/forks
- Community feedback

**Quality**:
- Test coverage maintained > 80%
- No critical bugs reported
- Positive code review feedback

**Documentation**:
- Users can get started without help
- API is clear from docs
- Examples work out of the box

**Community Value**:
- Used beyond Embody
- Solves real problems
- Inspires other contributions

---

## 🤝 Community Engagement

### Communication Channels

- **GitHub Discussions**: Design discussions, proposals
- **Pull Requests**: Code contributions
- **Issues**: Bug reports, feature requests
- **Amplifier Discord**: Quick questions, community chat

### Best Practices

**When proposing**:
- Start with discussion, not code
- Explain motivation and use cases
- Show examples of intended usage
- Ask for feedback early

**When contributing**:
- Follow code review feedback
- Be patient with review process
- Update based on community input
- Document decisions in commits

**After acceptance**:
- Be responsive to issues
- Support community users
- Collaborate with other maintainers
- Share learnings

---

## 📖 Examples

### Example 1: amplifier-module-design-tokens

See [ROADMAP.md](./ROADMAP.md#immediate-contributions-phase-1) for full details.

**Development Path**:
1. Built in `amplifier-embody/modules/design-tokens/`
2. Tested within Embody for Phase 1
3. Extracted to `amplifier-module-design-tokens/`
4. Submitted to Amplifier ecosystem
5. Embody switches to official module

**Timeline**: Phase 1 (Week 1-4)

---

### Example 2: embody-collection

See [ROADMAP.md](./ROADMAP.md#immediate-contributions-phase-1) for full details.

**Development Path**:
1. Built in `.embody/collections/embody/`
2. Validated through real usage in Phase 1
3. Extracted to `amplifier-collection-embody/`
4. Submitted to Amplifier collections
5. Embody references official collection

**Timeline**: Phase 1 (Week 1-4)

---

## 🎯 Summary

**Key Principles**:
1. Build for Amplifier from day one
2. Test thoroughly before extracting
3. Document comprehensively
4. Provide clear value to community
5. Maintain after contribution

**Process**:
1. Develop in Embody
2. Prepare for extraction
3. Extract to standalone
4. Test outside Embody
5. Submit contribution
6. Maintain and support

**Success**:
- Modules adopted beyond Embody
- High quality maintained
- Community benefits
- Amplifier ecosystem grows

---

**Questions?**
- See [BACKEND_ARCHITECTURE.md](./BACKEND_ARCHITECTURE.md#-amplifier-contribution-strategy)
- See [ROADMAP.md](./ROADMAP.md#-amplifier-contribution-roadmap)
- Open a discussion in Amplifier community

---

**Built with [Amplifier](https://github.com/microsoft/amplifier)** 🤖

*Every component designed to give back to the ecosystem that makes it possible.*
