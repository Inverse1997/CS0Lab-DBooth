"""
File I/O Lab
By: Daniel Booth

CSCI 110
Date: Nov. 16 2023

Program prompts user to enter name of the file that contains 10 integers.
It opens, reads and stores the numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
Program will then print the sorted lists to an output file along with the 
largest and smallest values in the list.

NOTE: All fixme's are each worth 10 points except for the FIXME1 which is worth 20 points
"""
from typing import List

totalInts = 10


def readData() -> List[int]:
    """Read data from a file.

    Returns:
        List[int]: List of integers
    """
    intList = [10,5,100,99,101,89,99,37,43,123]
    # FIXED (20 points):
    # Prompt user to input file name
    file_name = input('Enter the name of the file that contains 10 integers: ')
    
    try:
        # open the file; read each number one line at a time;
        with open(file_name, 'r') as file:
            for line in file:
                intList.append(int(line.strip()))
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except ValueError:
        print(f"Error: Invalid content in '{file_name}'. Make sure the file contains valid integers.")
    
    # close the file
    # return the intList
    return intList


def sortListInAscendingOrder(lstInts: List[int]):
    """Sort the provided list in ascending order.

    Args:
        lstInts (List[int]): the list to be sorted.
    """
    # FIXED
    # sort lstInts list in ascending order
    lstInts.sort()


def sortListInDescendingOrder(lstInts: List[int]):
    """Sort the provided list in descending order.

    Args:
        lstInts (List[int]): the list to be sorted.
    """
    # FIXED
    # sort lstInts in descending order
    lstInts.sort(reverse=True)


def printList(printFile, lstInts: List[int]):
    for n in lstInts:
        # FIXED
        # write each value one line at a time to file
        # handled by printFile object.
        printFile.write(str(n) + '\n')
    printFile.write('\n')


def main():
    integers = []  # list to store integers
    integers = readData()
    outputFileName = input('Enter a file to write output to: ')
    printFile = open(outputFileName, 'w')
    printFile.write("Numbers entered:\n")
    printList(printFile, integers)
    # sort numbers
    sortListInAscendingOrder(integers)
    printFile.write("\nNumbers sorted in ascending order:\n")
    printList(printFile, integers)

    # FIXED
    # Call sortListInDescendingOrder function
    sortListInDescendingOrder(integers)

    # FIXED
    # Write the sorted list in descending order to the output file
    printFile.write("\nNumbers sorted in descending order:\n")
    printList(printFile, integers)

    # FIXED
    # Print the largest number to the output file
    if integers:
        printFile.write("\nLargest number: " + str(integers[0]) + '\n')

    # FIXED
    # Print the smallest number to the output file
    if integers:
        printFile.write("Smallest number: " + str(integers[-1]) + '\n')

    printFile.close()
    print('Done executing the program! Check the output file for results.')


# FIXED
# Call main function if this module is run as the main module
if __name__ == "__main__":
    main()
