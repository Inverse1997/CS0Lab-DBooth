"""Moduel to test important function in pet.py.
By: Daniel Booth
Date: 10/17/2023
CsciLab
"""

import pet


def test_answer() -> None:
    """Tests answer function."""
    ans = pet.answer([10, 20, 11, 15, 13])
    expected = "2 20"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


def test_answer2() -> None:
    """Tests answer function."""
    ans = pet.answer([6, 10, 8, 4, 15])
    expected = "5 15"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# FIXED 1: add a test case function to test answer function
def test_answer3() -> None:
    """Tests answer function."""
    ans = pet.answer([5, 9, 12, 7, 6])
    expected = "3 12"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# FIXED 2: add a test case function to test answer function
def test_answer4() -> None:
    """Tests answer function."""
    ans = pet.answer([3, 3, 3, 3, 3])
    expected = "1 3"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


def test_list_sum() -> None:
    """Tests list_sum function."""
    ans = pet.list_sum([6, 7, 8, 10])
    expected = 31
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


def test_list_sum2() -> None:
    """Tests list_sum function."""
    ans = pet.list_sum([2, 3, 4, 5])
    expected = 14
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# FIXED 3: add a test case function to test list_sum function
def test_list_sum3() -> None:
    """Tests list_sum function."""
    ans = pet.list_sum([6, 4, 3, 2 ])
    expected = 15
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# FIXED 4: add a test case function to test list_sum function
def test_list_sum4() -> None:
    """Tests list_sum function."""
    ans = pet.list_sum([7, 3, 4, 9])
    expected = 23
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
