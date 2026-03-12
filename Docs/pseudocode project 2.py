```python

   Class SortResults
	String algorithmName
	Unsortered = []
	sorted = []
	int comparison
	results(algorithmName,Unsortered,sorted,comparison)
	    return algorithmName,Unsortered,sorted,comparison

   Class Sorter <<interface>>
	    return array[]
	getComparison()
	    return comparison
	resetComparison()
	comparisons = 0
   Class PermutationGenerator
	generatePermutations()
# Create an array with values 0 through n-1
    array = new int[n]
    for i = 0 to n-1
        array[i] = i
    
    
#List to store all permutations
    result = new empty List of arrays
    
#Generate permutations using Heap's algorithm
generateHeap(array, n, n, result)
    
    return result
   Class QuickSort
	int comparison
	partition(array, start, end)
	#add start index of an array and end index of an array
		pivotIndex = (first+last) / 2
		pivot = array[pivotIndex]
	#swap pivot with last element
		swap array[pivotIndex] with array[end]
	#i is the last element smaller than the pivot
		i = start
	#loop through the sub array
 		for j = start to end - 1
		   if array[j] <= pivot
			swap array[i] with array [j]
			i = i+1
		return i
	quickSort(array, start, end)
	#partition array and get pivot
		  pivotIndex = partition(array,end,high)

	# Recursively sort the sub-array before the pivot
    			quickSort(array, low, pivotIndex - 1)

        # Recursively sort the sub-array after the pivot
   			 quickSort(array, pivotIndex + 1, end)
		
   Class ShakerSort
	int comparison
	shakerSort()
	#lenght of array
	  n = len(array)
    	  swapped = True
    	  start = 0
    	  end = n-1
#loop for algorithm
    while (swapped == True):
        swapped = False
	#compare 2 elements next to each other
        for i in range(start, end):
            if (a[i] > a[i + 1]):
	#swap if 1st element is bigger than 2nd
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
	#stop nested loop if false
        if (swapped == False):
            break

        swapped = False
	#decrease by 1 on the range
        end = end-1
	#compare elements 
        for i in range(end-1, start-1, -1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
	#increment
        start = start + 1
	   
   Class HeapSort
	int comparison
	heapify(array,i,j)
# Initialize largest as root
	 largest = i          
# left = 2*i + 1
   	 left = 2 * i + 1 
# right = 2*i + 2    
   	 right = 2 * i + 2    

# If left child is larger than root
    	if left < n and arr[left] > arr[largest]:
        largest = left

# If right child is larger than largest so far
   	 if right < n and arr[right] > arr[largest]:
        largest = right

# If largest is not the root
    	if largest != i:
        swap(arr[i], arr[largest])

# Recursively heapify  sub-tree
        heapify(arr, n, largest)
function heapSort(arr):
    n = length(arr)

# Start from the last non-leaf node and heapify each node
    for i = n / 2 - 1 down to 0:
        heapify(arr, n, i)

#extract elements from the heap
    for i = n - 1 down to 1:
#swap the root with the last item
        swap(arr[0], arr[i])

# Call heapify on the reduced heap
        heapify(arr, i, 0)

	   Class MergeSort
	int comparison
	mergeSort(array)
#divide 
	middle = len(array) / 2
	left_sub = merge_sort[middle]
	right_sub = merge_sort[middle]
	return left_sub,right_sub

	merge(leftArr,rightArr)
	merged = []
	leftPointer, rightPointer = 0,0
		while leftPointer < len(leftArr) and rightPointer < len(rightArr)
		if leftArr[leftPoint] <= rightArr[rightPointer]
		merged.append[leftArr[leftPoint]]
		else
 		merged.append[rightArr[rightPointer]]
		
		return merged
```
