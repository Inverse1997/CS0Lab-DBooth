"""
Lists and Unittest Lab
Updated By: Daniel Booth
CSCI 110 Lab
Date: 10/17/2023

Read and solve - Pet: https://open.kattis.com/problems/pet 

Algorithm steps:
    1. Create a list to store the total scores of each contestant
    2. Repeat 5 times:
        i. Read the input line
        ii. Split the line into a list of numbers
        iii. Convert the list of strings into a list of ints
        iv. Sum the list of ints
        v. Append the sum to the list of scores
    3. Find the max score in the list of scores
    4. Find the index of the max score in the list of scores
    5. Print the index of the max score + 1 and the max score
"""
from typing import List


def main() -> None:
    """Main function that solves the problem
    """
    # FIXED 1 - Create a list to store the total scores of each contestant
    scores = []
    # FIXED 2 - Repeat step 2-4 5 times
    for _ in range(5):
        # FIXED 2i - Read the input line as a list of integers using get_data function
        data = get_data()
        # FIXED 3 - Find the sum of scores using list_sum function
        total_score = list_sum(data)
        # FIXED 4 - Append the sum to the list of scores
        scores.append(total_score)
    # FIXED 5 - Print the final output calling answer function
    print(answer(scores))


def get_data() -> List[int]:
    """Reads the data from std input and returns it as a list of ints
    Args:
        None
    Returns:
        List[int]: list of ints
    """
    str_nums = input().split()  # list of string numbers
    # FIXED 6: Convert str_nums as list of ints and return it
    return [int(x) for x in str_nums]


def list_sum(numbers: List[int]) -> int:
    """Finds and returns sum of the numbers in the list.
    Args:
        numbers: List[int]: # takes a list of numbers as a parameter

    Returns:
        int: sum of the numbers in the list
    """
    # FIXED 7: Find the sum of the numbers in the list and return it
    ans = sum(numbers)
    return ans


def answer(scores: List[int]) -> str:
    """Find and return the answer as a string.
    Args:
        scores (List[int]): List of 5 contestants scores
    Returns:
        str: index of the max score + 1 and the max score as a string
    """
    max_score = max(scores)
    index = scores.index(max_score)
    # FIXED 8: Return the index+1 and the max number in the list as a string
    return f"{index + 1} {max_score}"


if __name__ == "__main__":
    main()
