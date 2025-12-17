"""
Token Extractor

Extracts design tokens from repository code.
"""

from pathlib import Path
from typing import Dict, Any
import json
import re


async def extract_tokens_from_repo(repo_path: str) -> Dict[str, Any]:
    """
    Extract design tokens from repository
    
    Scans for:
    - CSS variables (--color-primary, etc.)
    - Tailwind config (tailwind.config.js/ts)
    - Design token files (tokens.json, design-tokens.json, etc.)
    - Style Dictionary files
    
    Args:
        repo_path: Path to repository root
        
    Returns:
        {
            "colors": {...},
            "typography": {...},
            "spacing": {...},
            "effects": {...},
            "behaviors": {...},
            "source_files": [...]
        }
    """
    repo_path_obj = Path(repo_path)
    
    if not repo_path_obj.exists():
        return _empty_tokens_result(f"Repository path does not exist: {repo_path}")
    
    tokens = {
        "colors": {},
        "typography": {},
        "spacing": {},
        "effects": {},
        "behaviors": {},
        "source_files": []
    }
    
    # Try to find token files
    token_files = _find_token_files(repo_path_obj)
    
    for token_file in token_files:
        tokens["source_files"].append(str(token_file.relative_to(repo_path_obj)))
        file_tokens = _extract_from_file(token_file)
        _merge_tokens(tokens, file_tokens)
    
    # If no tokens found, return empty but valid structure
    if not tokens["source_files"]:
        return _empty_tokens_result("No design token files found")
    
    return tokens


def _empty_tokens_result(message: str) -> Dict[str, Any]:
    """Return empty tokens structure with message"""
    return {
        "colors": {},
        "typography": {},
        "spacing": {},
        "effects": {},
        "behaviors": {},
        "source_files": [],
        "note": message
    }


def _find_token_files(repo_path: Path) -> list[Path]:
    """Find potential token files in repository"""
    token_files = []
    
    # Common token file patterns
    patterns = [
        "tokens.json",
        "design-tokens.json",
        "**/tokens.json",
        "**/design-tokens.json",
        "tailwind.config.js",
        "tailwind.config.ts",
        "**/tailwind.config.js",
        "**/tailwind.config.ts",
        "**/*.tokens.json",
        "variables.css",
        "**/variables.css",
        "**/:root.css",
    ]
    
    for pattern in patterns:
        token_files.extend(repo_path.glob(pattern))
    
    # Deduplicate and limit
    seen = set()
    unique_files = []
    for f in token_files:
        if f not in seen and f.is_file():
            seen.add(f)
            unique_files.append(f)
            if len(unique_files) >= 10:  # Limit to 10 files
                break
    
    return unique_files


def _extract_from_file(file_path: Path) -> Dict[str, Any]:
    """Extract tokens from a single file"""
    tokens = {
        "colors": {},
        "typography": {},
        "spacing": {},
        "effects": {},
        "behaviors": {}
    }
    
    try:
        content = file_path.read_text(encoding="utf-8")
        
        if file_path.suffix == ".json":
            tokens = _extract_from_json(content)
        elif file_path.suffix in [".css", ".scss", ".sass"]:
            tokens = _extract_from_css(content)
        elif file_path.suffix in [".js", ".ts"]:
            tokens = _extract_from_js_config(content)
    except Exception as e:
        # Non-blocking - log but continue
        print(f"Warning: Failed to extract from {file_path}: {e}")
    
    return tokens


def _extract_from_json(content: str) -> Dict[str, Any]:
    """Extract tokens from JSON file"""
    try:
        data = json.loads(content)
        
        # Handle Style Dictionary format
        if isinstance(data, dict):
            return {
                "colors": data.get("color", data.get("colors", {})),
                "typography": data.get("typography", data.get("font", {})),
                "spacing": data.get("spacing", data.get("space", {})),
                "effects": data.get("effects", data.get("shadow", {})),
                "behaviors": data.get("behaviors", data.get("animation", {}))
            }
    except json.JSONDecodeError:
        pass
    
    return {}


def _extract_from_css(content: str) -> Dict[str, Any]:
    """Extract CSS variables from CSS file"""
    tokens = {
        "colors": {},
        "typography": {},
        "spacing": {},
        "effects": {},
        "behaviors": {}
    }
    
    # Find CSS variable declarations
    # Pattern: --variable-name: value;
    pattern = r'--([a-zA-Z0-9-_]+):\s*([^;]+);'
    matches = re.findall(pattern, content)
    
    for name, value in matches:
        value = value.strip()
        
        # Categorize by variable name
        if any(x in name for x in ["color", "bg", "text", "border"]):
            tokens["colors"][name] = value
        elif any(x in name for x in ["font", "text", "family", "size", "weight", "line-height"]):
            tokens["typography"][name] = value
        elif any(x in name for x in ["spacing", "space", "margin", "padding", "gap"]):
            tokens["spacing"][name] = value
        elif any(x in name for x in ["shadow", "radius", "border-radius", "blur"]):
            tokens["effects"][name] = value
        elif any(x in name for x in ["transition", "duration", "timing", "animation"]):
            tokens["behaviors"][name] = value
    
    return tokens


def _extract_from_js_config(content: str) -> Dict[str, Any]:
    """Extract tokens from JavaScript/TypeScript config (Tailwind, etc.)"""
    tokens = {
        "colors": {},
        "typography": {},
        "spacing": {},
        "effects": {},
        "behaviors": {}
    }
    
    # This is a simplified extraction
    # In a full implementation, you'd parse the JS AST
    # For now, just look for obvious patterns
    
    # Try to find theme.extend or theme definitions
    if "colors:" in content or "colors :" in content:
        # Extract color definitions (simplified)
        color_block = re.search(r'colors:\s*\{([^}]+)\}', content, re.DOTALL)
        if color_block:
            tokens["colors"]["_raw"] = color_block.group(1).strip()
    
    if "fontSize:" in content or "fontSize :" in content:
        font_block = re.search(r'fontSize:\s*\{([^}]+)\}', content, re.DOTALL)
        if font_block:
            tokens["typography"]["_raw"] = font_block.group(1).strip()
    
    if "spacing:" in content or "spacing :" in content:
        spacing_block = re.search(r'spacing:\s*\{([^}]+)\}', content, re.DOTALL)
        if spacing_block:
            tokens["spacing"]["_raw"] = spacing_block.group(1).strip()
    
    return tokens


def _merge_tokens(target: Dict[str, Any], source: Dict[str, Any]) -> None:
    """Merge source tokens into target"""
    for category in ["colors", "typography", "spacing", "effects", "behaviors"]:
        if category in source:
            target[category].update(source[category])
