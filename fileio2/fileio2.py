
"""
File I/O Lab with Dictionary

Update By: Daniel Booth

CSCI 110
Date: nov. 24

Program finds the frequency of words in a given text document and print top 10 most
common words using dictionary and tuple data structures.
"""
import pathlib

def readText():
    """
    opens a file reads its contents and
    creates a histogram of words based on frequency using a dictionary data structure
    """
    fileOk = False
    fin = None
    hist = {}

    while not fileOk:
        fileName = input('Enter input text file => ')
        my_path = pathlib.Path(__file__).parent.resolve()
        filePath = my_path / fileName  # Using pathlib to create a correct path
        try:
            fin = open(filePath, 'r')
            fileOk = True
        except Exception as ex:
            print('Exception occurred: ', ex)

    lines = fin.readlines()
    for line in lines:
        line = line.strip().lower()
        if line:
            words = line.split()
            for word in words:
                hist[word] = hist.get(word, 0) + 1
    return hist


def reverseHistogramList(histDict):
    """
    given someDict,  returns a list of tuples in descending order based
    on the frequency of each word in histDict
    """
    reverseList = []
    for key, val in histDict.items():
        # FIXME5
        # append tuple with values in (val, key) order into reverseList list
        reverseList.append((val, key))

    # FIXME6
    # Sort the list reverseList in reverse order
    reverseList.sort(reverse=True)
    return reverseList


def main():
    histogram = readText()
    # FIXME7 - Comment the following statement out when done
    print(histogram)  # see the output to understand what's going on so far

    aList = reverseHistogramList(histogram)
    # FIXME8 – print the top 10 words with the highest frequencies stored in aList
    print("Top 10 words with the highest frequencies:")
    for i in range(10):
        print(f"{aList[i][1]}: {aList[i][0]}")


if __name__ == "__main__":
    main()


