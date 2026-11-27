"""
Test for Compact Memory skill.
"""

# Import compact_memory directly from the skills/compact-memory directory
import sys
sys.path.insert(0, "/var/lib/alan-portfolio/workspaces/ryan/sentinel-studio-145/skills/compact-memory")
from compact_memory import compact_memory

def test_compact_memory_empty():
    result = compact_memory("")
    assert result == ""

def test_compact_memory_basic():
    input_text = "We need to finish the login feature. It's a crucial requirement."
    expected = "task:We need to finish the login feature"
    expected += "\n"
    expected += "note:It's a crucial requirement."
    result = compact_memory(input_text)
    assert result == expected

def test_compact_memory_multiple_lines():
    input_text = """We need to finish the login feature.\nThe user can log in using username and password.\nIf the credentials are invalid, show an error message."""
    result = compact_memory(input_text)
    # Should produce at least one line
    assert len(result.split(chr(10))) > 0
