
print("---LinearSearchOrdered---")
def LinearSearchOrdered(listArray, searchValue):
    iterations = 0
    for i in listArray:
        iterations += 1
        if i == searchValue:
            print(iterations)
            return True
        elif i > searchValue:
            print(iterations)
            return False
    print(iterations)
    return False

orderedArray = [1,2,5,6,7,8,9,100,102];
print(LinearSearchOrdered(orderedArray, 10))

print("---BinarySearchOrdered---")
def BinarySearchOrdered(listArray, searchValue):
    """First establish lower and upper bounds of where the searchValue could be.
    To start, lower bound is the first value in the listArray, upper bound is last value.
    Begin a loop, inspecting the middlemost value between the first and last bounds.
    Find the midpoint between the lower|upper bounds, then inspect value at midpoint"""

    lowerBound = 0 # First index
    upperBound = len(listArray) - 1 # Last Index

    iterations = 0
    while lowerBound <= upperBound: # Keeps going until lowerBound > upperBound
        iterations += 1

        midpoint = (lowerBound + upperBound) // 2 # This returns the "floor" integer; 5 // 2 = 2
        valueOfMidpoint = listArray[midpoint]

        if searchValue == valueOfMidpoint:
            print(iterations)
            return True
        elif searchValue < valueOfMidpoint: # Checks left side next iteration
            upperBound = midpoint - 1
        elif searchValue > valueOfMidpoint: # Checks right side next iteration
            lowerBound = midpoint + 1
    print(iterations)
    return False

orderedArray2 = [1,2,3,4,7,10,14,16,20,21,25]
print(BinarySearchOrdered(orderedArray2, 3))
print(BinarySearchOrdered([2, 4, 6, 8, 10, 12, 13], 8))