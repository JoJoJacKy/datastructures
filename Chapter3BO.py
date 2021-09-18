
things = ["apples", "baboons", "cribs", "dulcimers"]

for thing in things:
    print(f"Here's a thing: {thing}")
# This is Complexity of O(n); n elements


def is_prime(number): # Goes from 2 all the way up to the number
    for i in range(2,number): # range() produces a collection
        if number % i == 0: # Needs to return 1 for number to be a prime
            return False
    return True
# This function has a Complexity of O(n)
# Goes through a for loop that is affected by the length of the provided number

# Exercise 1
def IsLeapYear(year):
    return (year % 100 == 0) or (year % 400 == 0) or (year % 4 == 0)
# Bool that returns True if a leap year; False otherwise
# This just checks at worst case 3 things to see if our input is true or false
# Thus is of Constant Complexity O(1)

# Exercise 2
def arraySum(listArray):
    sums = 0
    for i in listArray:
        sums += i
    return sums
# This has to iterate through the whole given listArray
# Thus Linear Comlexity O(n)

# Exercise 3
# Following function returns the square on the chessboard that is required to place a certain number of grains
def ChessBoardSpace(numberOfGrains):
    chessBoardSpaces = 1
    placedGrains = 1

    while (placedGrains < numberOfGrains):
        placedGrains *= 2 # Doubles the number of grains each space
        chessBoardSpaces += 1
    
    return chessBoardSpaces

print(ChessBoardSpace(20))
# Everytime the input doubles, the amount of spaces taken increases by 1
# Thus is of Logarithmic Complexity O(logn) since for every doubled data, the steps required to finish the algorithm is 
    # increases by 1 step

# Exercise 4
# This function takes in a list of strings, returns the strings that only start with "a"
def SelectAStrings(stringArray):
    aArray = []
    for stringA in stringArray:
        if stringA[0] == "a":
            aArray.append(stringA)
    return aArray

listOfStrings = ["a", "beee", "ceee", "aaeatr", "eefafaefae", "aAAA", "beafAEgA", "AAA"]
print(SelectAStrings(listOfStrings))
# Since it has to iterate the entire given n string, and then add n elements to the new list O(n+n) = O(2n) -> O(n)
# this would be of Linear Complexity O(n)

# Exercise 5
# Returns the median of an ordered array thats passed in 
def medianOrdered(orderedArray):
    middle = len(orderedArray) // 2

    # If the array has even amount of elements
    if len(orderedArray) % 2 == 0:
        return (orderedArray[middle - 1] + orderedArray[middle]) / 2
    else:
        return orderedArray[middle]

print(medianOrdered([1,2,3,4,5,6,7]))
# This is Complexity of O(1) since N is a fixed sized, but for this algorithm worst case is 2 steps
# This algorithm will take the same number of steps regardless of the size of the input parameter list
