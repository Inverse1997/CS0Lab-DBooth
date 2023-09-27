"""
Conditional Logic Lab
Updated By: FIXME
CSCI 110 Lab
Date: FIXME

Read and solve the Kattis problem: https://open.kattis.com/problems/twostones 

Algorithm Steps:
  1. Read the number of stones
  2. Check if the number of stones is odd or even
  3. Check oddity of the number of stones
  4. Print the winner
    4.a. If the number is odd, Alice wins.
    4.b. Otherwise, Bob wins.
"""

import sys


def main():
    """Main function that solves the problem
    """
    # FIXME 1: read the number of stones
    # FIXME 2: call answer function passing the number of stones as an argument
    # FIXME 3: print the answer as shown in the sample output
    pass
    numberofstones = input()
    
    print(stones)




def odd_even(number: int):
    """Checks if the number is odd or even

    Args:
        number (int): number to check odd or even

    Returns:
        str: 'odd' if the number is odd, 'even' otherwise
    """
    # FIXED 4
    #ans = odd_even
    if(number%2 == 1):
        ans = "bob"
    else:
        ans = "alice"
    return ans


def answer(stone: int):
    """Creates the final answer and returns it given the number of stones

    Args:
        stone (int): number of stones

    Returns:
        str: 'Alice' if the number of stones is odd, 'Bob' otherwise
    """

if __name__ == "__main__":
    main()  # call main function
