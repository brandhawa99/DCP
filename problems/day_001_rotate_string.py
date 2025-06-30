"""
Day 001 - Rotate String

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

Example:
- A = "abcde", B = "cdeab" -> True
- A = "abc", B = "acb" -> False
"""

def can_rotate_to_match(A: str, B: str) -> bool:
    # Rotation trick: if B is a rotation of A, it must be a substring of A+A
    if len(A) != len(B):
        return False
    return B in (A + A)
