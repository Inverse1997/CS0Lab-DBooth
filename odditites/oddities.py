"""
Loops and Unittest Lab
Updated By: Daniel Booth
CSCI 110 Lab
Date: 10/10/23
"""

def odd_even(number: int) -> str:
    """Checks if the number is odd or even

    Args:
        number (int): number to check odd or even

    Returns:
        str: 'odd' if the number is odd, 'even' otherwise
    """
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'

def main() -> None:
    """Main function that solves the problem
    """
    N = read_int_data()
    
    for _ in range(N):
        num = read_int_data()
        result = answer(num)
        print(result)

def read_int_data() -> int:
    """Reads the data from std input and returns it

    Returns:
        int: data read from std input as an int
    """
    data = int(input())
    return int(data)

def answer(num: int) -> str:
    """Creates the final answer and returns it given the number

    Args:
        num (int): number to check odd or even

    Returns:
        str: A string indicating whether the number is odd or even
    """
    ans = odd_even(num)
    return f'{num} is {ans}'

if __name__ == "__main__":
    main()
