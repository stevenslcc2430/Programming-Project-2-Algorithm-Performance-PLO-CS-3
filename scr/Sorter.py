"""
Team #5

Team Members
- Steven Benjamin
- Alex Gonzalez
- Carlos Recinos

CS-2430-502
Project 2: Algorithm Performance

Sources:
- MergeSort: GeeksforGeeks "Merge Sort in Python"
  https://www.geeksforgeeks.org/python-program-for-merge-sort/
- MergeSort: Programiz "Merge Sort"
  https://www.programiz.com/dsa/merge-sort
- QuickSort: GeeksforGeeks "QuickSort - Python" (Lomuto partition)
  https://www.geeksforgeeks.org/python-program-for-quicksort/
- QuickSort: Programiz "Quicksort" (Lomuto partition)
  https://www.programiz.com/dsa/quick-sort
- ShakerSort: GeeksforGeeks "Python Program for Cocktail Sort"
  https://www.geeksforgeeks.org/python-program-for-cocktail-sort/
- ShakerSort: TutorialsPoint "Python Program for Cocktail Sort"
  https://www.tutorialspoint.com/python-program-for-cocktail-sort
- HeapSort: GeeksforGeeks "Heap Sort - Python"
  https://www.geeksforgeeks.org/python-program-for-heap-sort/
- HeapSort: Programiz "Heap Sort"
  https://www.programiz.com/dsa/heap-sort
"""

from SortResults import Sort


class Sorter(Sort):
    """Base class that all sorting algorithms inherit from.
    Provides comparison getter and reset helpers."""

    def get_comparison(self):
        #return the current comparison count
        return self.comparison

    def reset_comparison(self):
        #set the comparison counter back to zero
        self.comparison = 0


# MERGE SORT
class MergeSort(Sorter):
    def __init__(self):
        super().__init__()
        self.AlgorithmName = "MergeSort"

    def sort(self, arr):
        #public entry point, takes a list, returns sorted copy
        self.reset_comparison()
        result = self._merge_sort(list(arr))
        return result

    def _merge_sort(self, arr):
        #base case
        if len(arr) <= 1:
            return arr
        #split and recurse until base case
        mid = len(arr) // 2
        left_half = self._merge_sort(arr[:mid])
        right_half = self._merge_sort(arr[mid:])
        return self._merge(left_half, right_half)

    def _merge(self, left, right):
        #merge two sorted lists into one sorted list
        #each time we compare left[i] vs right[j] that is one element comparison
        merged = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            #element-to-element comparison
            self.comparison += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        #append remaining elements, no comparisons needed here
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged


# QUICK SORT
class QuickSort(Sorter):
    def __init__(self):
        super().__init__()
        self.AlgorithmName = "QuickSort"

    def sort(self, arr):
        #public entry point, takes a list, returns sorted copy
        self.reset_comparison()
        arr_copy = list(arr)
        self._quick_sort(arr_copy, 0, len(arr_copy) - 1)
        return arr_copy

    def _quick_sort(self, arr, low, high):
        #recursively partition and sort subarrays
        if low < high:
            pivot_index = self._partition(arr, low, high)
            self._quick_sort(arr, low, pivot_index - 1)
            self._quick_sort(arr, pivot_index + 1, high)

    def _partition(self, arr, low, high):
        #partition using the middle element as pivot
        #only count element-to-element comparisons, not index checks
        mid = (low + high) // 2
        pivot = arr[mid]
        #move pivot to the end so it is out of the way
        arr[mid], arr[high] = arr[high], arr[mid]
        store_index = low
        for j in range(low, high):
            #element-to-element comparison
            self.comparison += 1
            if arr[j] <= pivot:
                arr[store_index], arr[j] = arr[j], arr[store_index]
                store_index += 1
        #put the pivot in its final sorted position
        arr[store_index], arr[high] = arr[high], arr[store_index]
        return store_index


# SHAKER SORT (bidirectional bubble sort)
class ShakerSort(Sorter):
    def __init__(self):
        super().__init__()
        self.AlgorithmName = "ShakerSort"

    def sort(self, arr):
        #public entry point, takes a list, returns sorted copy
        self.reset_comparison()
        arr_copy = list(arr)
        self._shaker_sort(arr_copy)
        return arr_copy

    def _shaker_sort(self, arr):
        #alternates between forward and backward bubble passes
        n = len(arr)
        start = 0
        end = n - 1
        swapped = True

        while swapped:
            swapped = False

            #left to right pass: bubble largest unsorted to the right
            for i in range(start, end):
                #element-to-element comparison
                self.comparison += 1
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True

            #if nothing moved then array is sorted
            if not swapped:
                break

            swapped = False
            end -= 1

            #right to left pass: bubble smallest unsorted to the left
            for i in range(end - 1, start - 1, -1):
                #element-to-element comparison
                self.comparison += 1
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True

            start += 1

        return arr


# HEAP SORT
class HeapSort(Sorter):
    def __init__(self):
        super().__init__()
        self.AlgorithmName = "HeapSort"

    def sort(self, arr):
        #public entry point, takes a list, returns sorted copy
        self.reset_comparison()
        arr_copy = list(arr)
        self._heap_sort(arr_copy)
        return arr_copy

    def _heap_sort(self, arr):
        #build a max-heap then repeatedly extract the max
        n = len(arr)
        #build the max-heap from the bottom up
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(arr, n, i)
        #extract elements one at a time
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self._heapify(arr, i, 0)
        return arr

    def _heapify(self, arr, heap_size, root):
        #sift down element at root to restore max-heap property
        #only element-to-element comparisons between array values are counted
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        #compare left child with current largest
        if left < heap_size:
            self.comparison += 1
            if arr[left] > arr[largest]:
                largest = left

        #compare right child with current largest
        if right < heap_size:
            self.comparison += 1
            if arr[right] > arr[largest]:
                largest = right

        #if the root is not the largest, swap and recurse
        if largest != root:
            arr[root], arr[largest] = arr[largest], arr[root]
            self._heapify(arr, heap_size, largest)


# Example usage
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]

    #test merge sort
    ms = MergeSort()
    print("Original:", test_array)
    result = ms.sort(test_array)
    print("MergeSort:", result, "| Comparisons:", ms.get_comparison())

    #test quick sort
    qs = QuickSort()
    result = qs.sort(test_array)
    print("QuickSort:", result, "| Comparisons:", qs.get_comparison())

    #test shaker sort
    sk = ShakerSort()
    result = sk.sort(test_array)
    print("ShakerSort:", result, "| Comparisons:", sk.get_comparison())

    #test heap sort
    hs = HeapSort()
    result = hs.sort(test_array)
    print("HeapSort:", result, "| Comparisons:", hs.get_comparison())
