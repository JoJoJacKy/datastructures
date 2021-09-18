
# Selection Sort
# Find the smallest element and add them to the sorted part of the list
def selectionSort(listArray):
    steps = 0
    lastIndex = len(listArray) - 1
    for i in range(lastIndex):
        steps += 1
        lowestNumberIndex = i # Takes initial index element as lowest value
        
        j = i + 1
        while j <= lastIndex: # The Comparions
            steps += 1
            if listArray[j] < listArray[lowestNumberIndex]: # Compares the lowestvalue
                lowestNumberIndex = j # Updates the lowest index element if encountered
            j += 1
        
        if (lowestNumberIndex != i): # The Swaps
            listArray[i], listArray[lowestNumberIndex] = listArray[lowestNumberIndex], listArray[i]


    print(steps)
    return listArray

print(selectionSort([6,5,4,1,4,3,2,2,3,2,1]))

# Practical Example of Same Algorithm Comparisons
# These Algorithms accomplish the same task
# Version 1: Complexity O(2.5n) => O(n)
def print_numbers_v1(upperLimit):
    number = 2
    while number <= upperLimit:
        if number % 2 == 0:
            print(number)
        number += 1

# Version 2: Complexity O(n/2) => O(n)
def print_numbers_v2(upperLimit):
    number = 2
    while number <= upperLimit:
        print(number)

        number += 2

# Exercise 3
# Returns the sum of all numbers of an array after the numbers have been doubled
# Linear Complexity O(n) from O(2n)
def doubleThenSum(listArray):
    doubledArray = []
    for i in listArray:
        doubled = i * 2
        doubledArray.append(doubled)
    
    doubledSums = 0
    for i in doubledArray:
        doubledSums += i
    
    return doubledSums

# Exercise 4
# Accepts an array of strings and prints each string in multiple cases
# Linear Complexity O(n) after dropping constants from O(3n)
def multiCases(stringList):
    for i in stringList:
        print(i.upper())
        print(i.lower())
        print(i.capitalize())

# Exercise 5
# Iterates over an array of numbers, for each even index, prints the sum of that number 
# plus every number in the array
# Quadratic Complexity O(n^2) after O(n^2 / 2)
def everyOther(listArray):
    for iCount, iValue in enumerate(listArray): # This loop is ran half the time
        if iCount % 2 == 0:
            for i in listArray:
                print(iValue + i)

