from SortResults import Sort
class Sorter(Sort):
    #returns comparisons
    def getComparison(self):
        return print("Comparison value is " + str(self.comparison))
    #reset to 0
    def resetComparison(self):
        self.comparison = 0
        return print("Comparison has been set to " + str(self.comparison))
    #testing methods/example usage
if __name__ == "__main__":
    test = Sorter()
    test.comparison = 5
    test.getComparison()
    test.resetComparison()
