import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# tests/test_day_001.py
from problems.day_001_rotate_string import can_rotate_to_match

def test_rotation_true():
    assert can_rotate_to_match("abcde", "cdeab") == True

def test_rotation_false():
    assert can_rotate_to_match("abc", "acb") == False

def test_empty_strings():
    assert can_rotate_to_match("", "") == True

def test_diff_lengths():
    assert can_rotate_to_match("a", "ab") == False

def test_same_string():
    assert can_rotate_to_match("abc", "abc") == True
