# All of these depend on the situation at hand
# Depends no what we need to prioritze to be efficient
# Minimal acceptable speed and space needs

# Time Complexity Quadratic O(n^2)
# Space Complexity Constant O(1)
# Memory Efficient
def hasDuplicateValueV1(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] == array[j]:
                return True
    return False


# Time Complexity Linear O(n)
# Space Complexity Linear O(n)
# Time Efficient
def hasDuplicateValueV2(array):
    existingValues = {}
    for i in range(len(array)):
        if not existingValues.get(i, False): # Adds values not within the hash table
            existingValues[array[i]] = True # True means acknowledging that the value exist
        else:
            return True

# Time Complexity O(nlogn)
# Quicksort takes up Space Complexity O(logn)
# Balanced Space and Time Efficiency
def hasDuplicateValueV3(array):
    array.sort() # Most likely based on Quicksort

    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            return True
    
    return False


# Hidden Cost of Recursion

# This recursive function has a Space Complexity of O(n)
def recurse(n): # A Countdown function
    if n < 0:
        return
    print(n)
    return recurse(n - 1)
# n = 100 implies would need to store 100 function calls within the call stack

# This function does the exact same thing as recurse but does not take up any extra memory
def loopOverRecurse(n):
    while n >= 0:
        print(n)
        n -= 1

# Exercise 1
# Describe Space Complexity of the function
# Space Complexity of O(n^2)
def wordBuilder(array):
    collection = []

    for i in range(len(array)):
        for j in range(len(array)):
            if (i != j):
                collection.append(array[i] + array[j])
    
    return collection

# Exercise 2
# Space Complexity O(n)

# Exercise 3

# Exercise 4
# 1. Time Complexity: O(n) | Space Complexity: O(n) 
# 2. O(n) | O(1)
# 3. O(n) | O(n)
