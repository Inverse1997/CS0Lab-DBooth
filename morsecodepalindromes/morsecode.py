"""
 Updated By: Daniel Booth
 CSCI 110 Lab
 Date: 11/1/2023
"""
# Solution for Kattis problem - Morse Code Palindromes - https://open.kattis.com/problems/morsecodepalindromes

# Given English text, the program finds if the corresponding Morse code is a palindrome.

# Algorithm steps:
# 1. Create a dictionary to map alphabets and numbers to Morse code
# 2. Read the input English string
# 3. Convert the string into uppercase English string
# 4. Convert the English string into Morse Code string using the dictionary
# 5. Check if the Morse Code string is a palindrome
#    i. Print 1 if it's a palindrome
#    ii. Otherwise, print 0

import sys

# Create English to Morse Code dictionary
engToMorse = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    # FIXME 1: Map the digits to their corresponding Morse code
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'
}


def is_palindrome(morse_code: str) -> int:
    """Returns 1 if the Morse code string is a palindrome; 0 Otherwise.

    Args:
        morse_code (str): Morse code palindrome string

    Returns:
        int: 1 or 0
    """
    # FIXME 2: If the Morse code string is empty, return 0
    if not morse_code:
        return 0
    # Otherwise use the algorithm:
    # 1. Reverse the Morse code string and store it in a variable
    reversed_morse_code = morse_code[::-1]
    # 2. If the Morse code equals the reversed string, it is a palindrome and return 1
    if morse_code == reversed_morse_code:
        return 1
    # 3. Return 0 otherwise
    return 0


def convert_to_morse(english: str) -> str:
    """The function converts the given English text into corresponding Morse code

    Args:
        english (str): English text converted into uppercase

    Returns:
        str: Morse code
    """
    morse_code = ''
    # Algorithm steps:
    # For each character in English,
    #   find the Morse code of the character using engToMorse dictionary
    #   concatenate Morse code to morse_code variable if the key exists
    #   ignore the key/character if it doesn't exist in the dictionary
    for char in english:
        if char in engToMorse:
            morse_code += engToMorse[char]
    # FIXME 3: Implement the above algorithm
    return morse_code


def solve() -> None:
    # Read/input English text as a line
    english = input()
    # FIXME 4: Convert English into uppercase
    upper_english = english.upper()
    print(upper_english, file=sys.stderr)
    morse_code = convert_to_morse(upper_english)
    # FIXME 5: Call is_palindrome passing the proper argument and print the result
    result = is_palindrome(morse_code)
    print(result)

if __name__ == '__main__':
    solve()
