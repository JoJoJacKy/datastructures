
# Code Implementation of Partitioning
class SortableArray:
    
    def __init__(self, array):
        self.array = array
    
    def partition(self, leftPointer, rightPointer):
        # Choose right most element as pivot
        # Take note of pivot index
        pivotIndex = rightPointer
        pivot = self.array[pivotIndex - 1] # Element value of Pivot

        # Start right pointer to left of pivot index
        rightPointer -= 1

        while True:

            # Move left pointer to the right as long as it points to value less than pivot
            while self.array[leftPointer] < pivot:
                leftPointer += 1
            
            # Move right pointer to the left as long as it points to value greater than pivot
            while self.array[rightPointer] > pivot:
                rightPointer -= 1
            
            # This is where both pointers have stopped, need to check if left pointer has reached or surpassed right pointer
            # If it has, break out of loop to swap pivot

            if leftPointer >= rightPointer:
                break

            else: # Swapping values
                self.array[leftPointer], self.array[rightPointer] = self.array[rightPointer], self.array[leftPointer]
                leftPointer += 1
        
        # Now swap value of left pointer with pivot
        self.array[leftPointer], self.array[pivotIndex - 1] = self.array[pivotIndex - 1], self.array[leftPointer]
        return leftPointer # Returns index where the pivot is swapped to

    def quicksort(self, leftIndex, rightIndex):
        if rightIndex - leftIndex <= 0:
            return # The Do Nothing Base Case
    
        pivotIndex = self.partition(leftIndex, rightIndex) # Partitions the entire array

        self.quicksort(leftIndex, pivotIndex - 1) # Quicksort called on the subarray left of pivot
        self.quicksort(pivotIndex + 1, rightIndex) # Quicksort called on the subarray right of pivot

    # Quickselect
    def quickselect(self, kthLowestValue, leftIndex, rightIndex):
        if rightIndex - leftIndex <= 0:
            return self.array[leftIndex]
        
        pivotIndex = self.partition(leftIndex, rightIndex)

        # Check if what we're looking for is to the left of the pivot
        if kthLowestValue < pivotIndex:
            self.quickselect(kthLowestValue, leftIndex, pivotIndex - 1)
        
        # If not on left then look in the right of the index
        elif kthLowestValue > pivotIndex:
            self.quickselect(kthLowestValue, pivotIndex + 1, rightIndex)

        else:
            # if kthLowestvalue == pivotIndex
            # if after partition, pivot position is the same as the kth lowest value, we've found the value we want
            return self.array[pivotIndex]

    
array = [0,8,3,4,5,6,1]
sortingClass = SortableArray(array)
sortingClass.quicksort(0, len(array))
print(sortingClass.array)


# Sorting before checking for duplicates
# This is to overcome the memory consumption and make an algorithm O(nlogn) over O(n^2)
def hasDuplicateValue(array):
    # Presort the array
    array.sort()
    for i in range(len(array) - 1):
        if array[i] == array[i+1]:
            return True
    return False

dupesArray = [1,2,3,4,3,2,1,2,3]
print(hasDuplicateValue(dupesArray))
# Efficiency
# Sorting Array is O(nlogn)
# Iterate over n steps O(n)
# Overall Complexity O(nlogn) + O(n) => O(nlogn) (Keep the highest order)

# Exercise 1
# Function input is an array of positive numbers
# Returns the greatest product of any three numbers

def greatestProduct3(array):
    array.sort()
    return array[-1] * array[-2] * array[-3]
print(greatestProduct3([2,3,4,5,1,2,3,4,5,3,4,5,8,8,6,5,4,3,1]))

# Exercise 2
# Function finds the "Missing Number" from an array of integers
# Input array has 1 number missing, should be from 0 up to array legnth index

# Inefficient O(n^2) Implementation
def findMissingNumberBAD(array):
    for i in range(0,len(array)):
        if not i in array:
            return i
    return None # If all numbers are present

print(findMissingNumberBAD([6,5,4,2,1,0]))

def findMissingNumber(array):
    array.sort()
    for i in range(0,len(array)):
        if not i == array[i]:
            return i
    return None
print(findMissingNumber([6,5,4,2,1,0]))

# Exercise 3
# Create 3 different implementations of a function that finds the greatest number within an array
# Write O(n^2), O(nlogn), and O(n) functions

def greatestNumQuad(array):
    greatestNum = None
    for i in array:
        for j in array:
            if j > i:
                greatestNum = j
    return greatestNum

testArray = [1,34,4,3,2,4,5,6,6,5,43,3]
print(greatestNumQuad(testArray))

def greatestNumnlogn(array):
    array.sort()
    return array[-1]
print(greatestNumnlogn(testArray))

def greatestNumn(array):
    greatestNum = array[0]
    for i in array:
        if i > greatestNum:
            greatestNum = i
    return greatestNum
print(greatestNumn(testArray))