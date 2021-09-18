
# Bubble Sort
def bubbleSort(listo):
    unsortedUntilIndex = len(listo) - 1 # Keeps track of the right most index that hasn't been sorted yet
    sorted = False # Flag
    comparisons = 0
    swaps = 0
    while not sorted:
        sorted = True # If the last iteration does not change this to false the loop breaks off; Assumes array is sorted until we encounter a needed swap
        for i in range(unsortedUntilIndex):
            comparisons += 1
            if listo[i] > listo[i+1]: # Checks if the previous element is greater than the next element
                swaps += 1
                listo[i], listo[i+1] = listo[i+1], listo[i] # This is where the values are swapped
                sorted = False # Keeps the loop running 
        unsortedUntilIndex -= 1 # After a pass through, goes down the index of the given list
    print(comparisons)
    print(swaps)
    return listo

print(bubbleSort([20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]))
# If in descending order, same amount of swaps and comparisons (Worst Case)

# Quadratic Complexity O(n^2) example
def hasDuplicateValue(listArray):
    steps = 0
    indexUntilCompletelyChecked = len(listArray) - 1
    for i in range(indexUntilCompletelyChecked):
        for j in range(indexUntilCompletelyChecked):
            steps += 1
            if (i != j and listArray[i] == listArray[j]):
                return True
    return False

worstCaseNoDuplicates = [0,1,2,3,4,5,6,7,8,9,10]
hasDuplicateValue(worstCaseNoDuplicates)
# Worse case is that the given list has no duplicates thus has to loop through the whole listArray twice
# n*n = n^2

print("------------------")
print("------------------")

# Linear Solution to previous example
# Linear Complexity O(n)
# Returns True if there is an existing value within the given listArray parameter
def hasDuplicateLinear(listArray):
    counter = 0
    existingNumbers = []
    lastIndex = len(listArray) - 1
    for i in range(lastIndex):
        counter += 1
        if existingNumbers[listArray[i]] == 1:
            return counter
        else:
            existingNumbers[listArray[i]] = 1
    return counter
# The existing numbers is creating an array that has a 1 at the index which is an element of the listArray
# Every iteration checks to see if there exists a 1 at the number of the index
# This coding example works with JavaScript
# This example is using a Memory over Time Technique

print("--Exercises--")

# Exercise 3
# Find Complexity; Returns the greatest product of any pair of two numbers within a given array
def greatestProduct(listArray):
    greatestProductSoFar = listArray[0] * listArray[1]

    for iCounter, iValue in enumerate(listArray):
        for jCounter, jValue in enumerate(listArray):
            if iCounter != jCounter and iValue * jValue > greatestProductSoFar:
                greatestProductSoFar = iValue * jValue
    
    return greatestProductSoFar
# Complexity is Quadratic Complexity O(n^2)
print(greatestProduct([10,2,3,4,5,6,6,2,11]))

# Exercise 4
# Change this Quadratic Complexity O(n^2) function to a Linear Complexity O(n) function
def greatestNumber(listArray):
    for i in listArray: # Loops through list once
        isIValueTheGreatest = True # Assumes that the i is the greatest

        for j in listArray: # Loop through list again to compare each value to the i
            if j > i:
                isIValueTheGreatest = False
        
        if isIValueTheGreatest: # Basically if isIValueTheGreatest remains True, it is greatest value and returns i
            return i

def greatestNumberLinear(listArray):
    currentGreatestNumber = 0
    for i in listArray:
        if i > currentGreatestNumber:
            currentGreatestNumber = i
    return currentGreatestNumber

greatestNumsList = [1,2,3,4,5,6,6,5,4,3,100,2,3,5,5]
print(greatestNumber(greatestNumsList))
print(greatestNumberLinear(greatestNumsList))