"""
Team #5

Team Members
- Steven Benjamin
- Alex Gonzalez
- Carlos Recinos

CS-2430-502
Project 2: Algorithm Performance
"""


class Sort:
    """Holds the data for one sorting experiment run."""

    def __init__(self):
        #name of the sorting algorithm used
        self.AlgorithmName = ""
        #the input array before sorting
        self.unsortArray = []
        #the array after sorting
        self.sortArray = []
        #total element-to-element comparisons counted during the sort
        self.comparison = 0

    def display(self):
        #print a summary of this sort run to the console
        print("Algorithm: " + self.AlgorithmName)
        print("Unsorted:  " + str(self.unsortArray))
        print("Sorted:    " + str(self.sortArray))
        print("Comparisons: " + str(self.comparison))
