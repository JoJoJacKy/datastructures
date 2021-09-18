
# Insertion Sort
# Quadratic Complexity O(n^2)
def insertionSort(listArray):
    for index in range(1, len(listArray)): # Left side of Gap considered "Sorted"
        compareValue = listArray[index] # The Gap Value that we compare all the elements to the left of this gap
        position = index - 1 # First element to the left of the gap

        while position >= 0:
            if listArray[position] > compareValue: # Checking the index before the compared value
                listArray[position + 1] = listArray[position] # Shifts the value to the gap
                position -= 1 # looks more left now
            else: 
                break # Breaks when runs into a value not greater than the temp value
        
        listArray[position + 1] = compareValue # Moves the temp value into the gap (Position would be modified which is the index of the Gap)
    return listArray

print(insertionSort([9,8,7,6,5,4,3,2,1]))

# Practical Example
def intersection(firstArray, secondArray):
    result = []

    for iIndex in range(len(firstArray)): # Comparison
        for jIndex in range(len(secondArray)): # Comparison
            if firstArray[iIndex] == secondArray[jIndex]: # Insertion
                result.append(firstArray[iIndex])
                break # Saves time within the inner loop
    
    return result

print(intersection([1,2,3,4,5,6,9], [3,2,1,5,6,7,8,9,10,10,10,9]))

# Exercise 3
# Bool function; Checks whether an array of numbers contains a pair of two numbers that add up to 10
# Checking if the sum of 10 exists between any 2 elements that exists within the input parameter array
def twoSum(listArray):
    for i in range(len(listArray)):
        for j in range(len(listArray)):
            if (i != j and listArray[i] + listArray[j] == 10):
                return True
    return False

print(twoSum([3,2,1,10,5,6,15,2,2,1,6]))
# Worst Case: Sum of 10 between 2 elements DNE; Quadratic Complexity O(n^2)
# Average Case: Sum is found within first few iterations of the outer loop
# Best Case: First 2 elements sum is 10

# Exercise 4
# Returns true if capital character 'X' exists within a string
def containsX(aString):
    foundX = False
    for i in range(len(aString)):
        if aString[i] == "X":
            return True
    return False

print(containsX("uifnaeifnIXijfeaoifj"))
# Worst Case: X DNG within string; Linear Complexity O(n)
# Average Case: X exists around middle of String
# Best Case: X is the first character of the string