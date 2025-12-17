"""
State Persistence

Serialize/deserialize session state to JSON.
"""

from pathlib import Path
from typing import Dict, Any
import json


def get_session_dir(session_id: str) -> Path:
    """
    Get session directory path
    
    Args:
        session_id: Session identifier
        
    Returns:
        Path to session directory
    """
    sessions_dir = Path(".embody/sessions")
    sessions_dir.mkdir(parents=True, exist_ok=True)
    
    session_dir = sessions_dir / session_id
    session_dir.mkdir(parents=True, exist_ok=True)
    
    return session_dir


def save_session_state(session_id: str, state: Dict[str, Any]) -> None:
    """
    Persist session state to disk
    
    Args:
        session_id: Session identifier
        state: State dictionary to persist
        
    Raises:
        IOError: If unable to write state file
    """
    session_dir = get_session_dir(session_id)
    state_file = session_dir / "state.json"
    
    try:
        # Write with pretty formatting for human readability
        with state_file.open("w", encoding="utf-8") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)
    except Exception as e:
        raise IOError(f"Failed to save session state for {session_id}: {e}")


def load_session_state(session_id: str) -> Dict[str, Any]:
    """
    Load session state from disk
    
    Args:
        session_id: Session identifier
        
    Returns:
        State dictionary
        
    Raises:
        FileNotFoundError: If state file doesn't exist
        ValueError: If state file is malformed
    """
    session_dir = get_session_dir(session_id)
    state_file = session_dir / "state.json"
    
    if not state_file.exists():
        raise FileNotFoundError(f"Session state not found for {session_id}")
    
    try:
        with state_file.open("r", encoding="utf-8") as f:
            state = json.load(f)
        return state
    except json.JSONDecodeError as e:
        raise ValueError(f"Malformed session state for {session_id}: {e}")
    except Exception as e:
        raise IOError(f"Failed to load session state for {session_id}: {e}")


def session_exists(session_id: str) -> bool:
    """
    Check if session exists on disk
    
    Args:
        session_id: Session identifier
        
    Returns:
        True if session state file exists
    """
    session_dir = Path(".embody/sessions") / session_id
    state_file = session_dir / "state.json"
    return state_file.exists()
