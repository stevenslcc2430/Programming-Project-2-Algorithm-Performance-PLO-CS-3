class Sort:
    def __init__(self):
        #variables
        self.AlgorithmName = ""
        self.unsortArray = [0,1,2,3,4,5,6,7,8]
        self.sortArray = []
        self.comparison = int
    #display results
    def Display(self):
        print("Algorithm used is "+self.AlgorithmName + "/nUnsorted array: "+self.unsortArray+ "/n Sorted array: "+self.sortArray)
