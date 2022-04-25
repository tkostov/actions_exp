"""
Docstring for the test functions.
Line 2.
"""
import sys

sys.path.append("../src")
from src.main import some

# comment


def test_some():
    """
    Test of the function.
    test_some _summary_
    """
    assert some("input") is None
