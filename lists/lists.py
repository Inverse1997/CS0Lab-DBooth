"""
 Daniel Booth
 CSCI 110
 Date: 11/1/2023
 #Description:
 This Python script prompts the user to enter a phrase and provides various properties about the phrase.
"""
import sys

def isReversible(phrase):
    # Function to determine whether the given phrase is the same forward and backward, i.e., reversible or not.
    length = len(phrase)  # Get the length of the phrase
    reversible = True  # Let's assume every phrase is reversible!
    j = length - 1  # Right index
    for i in range(0, length, 1):  # Start at 0, end at length-1, step to increment is 1
        # Algorithm steps:
        # 1. Go through each character
        #    a. Ignore all the non-alphabetic characters on both ends of the phrase
        # 2. Compare the corresponding characters from the left and right of the phrase
        # 3. If a single pair is not equal, the phrase is NOT reversible
        # 4. Else, if all the pairs are the same, the word is reversible
        if not phrase[i].isalpha():
            continue
        while not phrase[j].isalpha():
            j -= 1
            if j < 0:  # If passed the first letter; return False or not reversible
                return True

        if phrase[i] != phrase[j]:
            reversible = False
            break
        j -= 1

    return reversible

def hasLowerCase(phrase):
    for i in range(len(phrase)):
        if phrase[i].islower():
            return True
    return False

def hasUpperCase(phrase):
    for ch in phrase:
        if ch.isupper():
            return True
    return False

def hasDigit(phrase):
    # Fixed: Return True if the phrase has at least 1 digit, False otherwise
    for ch in phrase:
        if ch.isdigit():
            return True
    return False

def hasSymbol(phrase):
    # Fixed: Return True if the phrase has at least one of these symbols: ~!@#$%
    # Return False otherwise
    symbols = "~!@#$%"
    for ch in phrase:
        if ch in symbols:
            return True
    return False

def main():
    print("Program tells various properties of a given phrase")

    while True:
        phrase = input("Enter a word or phrase: ")

        if isReversible(phrase):
            print("{} is reversible!".format(phrase))
        else:
            print("{} is not reversible!".format(phrase))

        # Fixed: Print if the phrase has an upper case character by calling the proper function
        if hasUpperCase(phrase):
            print('{} has an upper case character.'.format(phrase))
        else:
            print('{} does not have an upper case character.'.format(phrase))

        # Fixed: Print if the phrase has a lower case character by calling the proper function
        if hasLowerCase(phrase):
            print('{} has a lower case character.'.format(phrase))
        else:
            print('{} does not have a lower case character.'.format(phrase))

        # Fixed: Print if the phrase has a digit by calling the proper function
        if hasDigit(phrase):
            print('{} has a digit.'.format(phrase))
        else:
            print('{} does not have a digit.'.format(phrase))

        # Fixed: Print if the phrase has a symbol by calling the proper function
        if hasSymbol(phrase):
            print('{} has a symbol.'.format(phrase))
        else:
            print('{} does not have a symbol.'.format(phrase))

        ans = input('Want to continue? [y/n]: ')
        ans = ans.lower()
        # Continue if the user enters yes or Yes or y or anything that starts with y
        if ans.startswith('y'):
            continue
        else:
            print('Goodbye!')
            break

def test():
    print('Running unit test cases...')
    assert isReversible('race car!') == True
    assert isReversible('jeep!') == False
    assert hasLowerCase('Welcome!') == True
    assert hasLowerCase('ABC235!') == False
    assert hasUpperCase('WELcome!!') == True
    assert hasUpperCase('$!#%#@asdfdsf') == False
    assert hasDigit('22424ADSFDS') == True
    assert hasDigit('asdfdsfWASDFASDG') == False
    assert hasSymbol('!@$DAD$%') == True
    assert hasSymbol('asdfASF3424') == False
    print('All test cases passed!')

if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        test()
    else:
        main()
