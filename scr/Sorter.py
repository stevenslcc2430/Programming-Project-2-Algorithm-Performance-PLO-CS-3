from SortResults import Sort
class Sorter(Sort):
    #returns comparisons
    def getComparison(self):
        return print("Comparison value is " + str(self.comparison))
    #reset to 0
    def resetComparison(self):
        self.comparison = 0
        return print("Comparison has been set to " + str(self.comparison))

class mergeSort(Sorter):
    def __init__(self):
        super().__init__()  # Call parent class constructor
        self.comparison = 0

    def merge_sort(self, arr):
        #base case
        if len(arr) <= 1:
            return arr
        #split and call in merge function until base case happens
        mid = len(arr) // 2
        left_half = self.merge_sort(arr[:mid])
        right_half = self.merge_sort(arr[mid:])

        return self.merge(left_half, right_half)

    def merge(self, left, right):
        #Merge two sorted arrays
        sorted_list = []
        i = j = 0
        #while loop to combine
        while i < len(left) and j < len(right):
            self.comparison += 1
            ##if left is less than right then left first else put right
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        return sorted_list
if __name__ == "__main__":
    #random test stuff/example can delete if you want
    test = Sorter()
    test.getComparison()
    #test output of array
    print(test.unsortArray)
    sort = mergeSort()
    #test array or random values
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nOriginal array: {test_array}")
    sorted_array = sort.merge_sort(test_array.copy())
    print(f"Sorted array:   {sorted_array}")
    sort.getComparison()
    #test array that is in class
    sort.resetComparison()
    print(f"\nOriginal array: {sort.unsortArray}")
    sorted = sort.merge_sort(test.unsortArray)
    print(f"Sorted array:   {sorted}")
    sort.getComparison()