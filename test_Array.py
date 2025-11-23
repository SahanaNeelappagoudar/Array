import subprocess
import sys

def test_main():
    # Run: python Array.py "10 40 70"
    result = subprocess.run(
        [sys.executable, "Array.py", "10 40 70"],
        capture_output=True,
        text=True
    )

    output = result.stdout

    # Check expected values
    assert "120" in output     # sum
    assert "40.0" in output    # average
    assert "70" in output      # maximum
    assert "10" in output      # minimum