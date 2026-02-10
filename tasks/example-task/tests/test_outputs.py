"""
Tests that verify the Go program has been compiled properly and runs.
"""
import subprocess
import os


def test_hello_executable_exists():
    """Test that the compiled executable exists."""
    assert os.path.exists("/app/hello"), "Compiled 'hello' executable should exist in /app"


def test_hello_is_executable():
    """Test that hello is executable."""
    assert os.access("/app/hello", os.X_OK), "'hello' should be executable"


def test_hello_output():
    """Test that the program outputs 'Hello, World!'"""
    result = subprocess.run(["/app/hello"], capture_output=True, text=True)
    assert result.returncode == 0, f"Program should exit with code 0, got {result.returncode}"
    assert result.stdout.strip() == "Hello, World!", f"Expected 'Hello, World!', got '{result.stdout.strip()}'"
