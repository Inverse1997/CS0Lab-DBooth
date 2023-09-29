"""
Conditional Logic Lab
Updated By: Daniel Booth
CSCI 110 Lab
Date: 09/27/2023

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
    number_of_stones = int(input("enter the number of stones: "))
    ans = answer(number_of_stones)
    print(ans)
    # FIXED 1: read the number of stones
    # FIXED 2: call answer function passing the number of stones as an argument
    # FIXED 3: print the answer as shown in the sample output
 
                           
def odd_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


"""Checks if the number is odd or even

    Args:
        number (int): number to check odd or even

    Returns:
        str: 'odd' if the number is odd, 'even' otherwise
    """
    # FIXED 4: if the number divided by 2 has 0 remainder, return 'even'
    # otherwise, return 'odd'
def answer(stone):
    even_or_odd = odd_even(stone)
    if even_or_odd == "odd":
        return "alice"
    else:
        return "bob"

"""Creates the final answer and returns it given the number of stones

    Args:
        stone (int): number of stones

    Returns:
        str: 'Alice' if the number of stones is odd, 'Bob' otherwise
    """
if __name__ == "__main__":

    main()  # call main function