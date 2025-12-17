"""
Profile Loader

Loads and compiles Amplifier profile to mount plan.
"""

from pathlib import Path
from typing import Dict, Any


def load_embody_profile(profile_name: str = "default") -> Dict[str, Any]:
    """
    Load embody profile and compile to mount plan
    
    Args:
        profile_name: Profile name (default: "default")
        
    Returns:
        Mount plan ready for AmplifierSession initialization
        
    Raises:
        FileNotFoundError: If profile file doesn't exist
        ValueError: If profile is malformed
    """
    from amplifier.profiles import ProfileLoader, compile_profile_to_mount_plan
    from amplifier.agents import AgentLoader
    from amplifier.module_resolution import StandardModuleSourceResolver
    
    # Profile directory
    profile_dir = Path(".embody/profiles")
    if not profile_dir.exists():
        raise FileNotFoundError(
            f"Profile directory not found: {profile_dir}\n"
            "Ensure .embody/profiles/ exists with profile files."
        )
    
    # Load profile
    profile_loader = ProfileLoader([profile_dir])
    
    try:
        profile = profile_loader.load_profile(profile_name)
    except Exception as e:
        raise ValueError(f"Failed to load profile '{profile_name}': {e}")
    
    # Create agent resolver
    agent_resolver = StandardModuleSourceResolver(
        workspace_dir=Path(".embody/modules")
    )
    
    # Create agent loader with resolver
    agent_loader = AgentLoader(resolver=agent_resolver)
    
    # Compile profile to mount plan with agent discovery
    try:
        mount_plan = compile_profile_to_mount_plan(
            profile,
            agent_loader=agent_loader
        )
    except Exception as e:
        raise ValueError(f"Failed to compile profile to mount plan: {e}")
    
    return mount_plan
