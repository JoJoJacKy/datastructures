
# Double each element if a given integer array
# Return a new array or
# "In-Place Modification" - Don't produce a new array, instead modify the original passed in array

def doubleArray(array, index=0):
    if index >= len(array): # Base Case
        return # Ends once the index surpasses the amount of elements within the array
    array[index] *= 2
    doubleArray(array, index + 1)

a = [1,2,3,4,5]
doubleArray(a)
print(a)

# Bottom-Up Approach; Basically same thing as using the classic loop or recursion
# The default parameter i is increased by 1 until it is of size n, and it is multiplied with default parameter product
def factorial(n, i=1, product=1):
    if i > n: # Base Case
        return product
    return factorial(n, i+1, product*i) # product*i is what we want return which is the factorial of n

print(factorial(5))

# Top-Down Approach; Recursion Required
# Examples

def sumTD(array):
    if len(array) == 1: # Base Case
        return array[0]
    return array[0] + sumTD(array[1: len(array)]) # Slicing the remainder of the array
print(sumTD([1,2,3,4,5]))

def reverseString(string):
    if len(string) == 1: # Base Case
        return string[0]
    return reverseString(string[1:len(string)]) + string[0]
print(reverseString("Shalom"))
# Basically goes through the all the subproblems of the original problem until it hits the base case

def countX(string):
    if len(string) == 0: # Base Case where we run out of indexes to check
        return 0
    if string[0] == "x":
        return 1 + countX(string[1:len(string)])
    else:
        return countX(string[1:len(string)])

print(countX("ShalxxlmsoMSOMx"))

# The Staircase Problem
# Person can take 1, 2 or 3 steps at a time
# How many possible "paths" can the person take to reach the top of n given total steps?
def numberOfPaths(n):
    if n < 0: # Base Case
        return 0
    if n == 1 or n == 0: # Base Case
        return 1
    return numberOfPaths(n - 1) + numberOfPaths(n - 2) + numberOfPaths(n - 3)
# The last step is the sum of all the paths of the 3 prior steps
print(numberOfPaths(4))

# CS Dojo Interview Coding Question
# Staircase Problem with predefined step sizes of 1 or 2
def num_ways(n):
    if n == 0 or n == 1:
        return 1
    else:
        return num_ways(n-1) + num_ways(n-2)
# This is inefficient since we repeat certain calculations

# Dynamic Programming Bottom-Up Approach of Staircase Problem
# Using Memoization
def num_ways_bottom_up(n):
    if n == 0 or n == 1:
        return 1
    nums = [None for i in range(n+1)] # Memoization
    nums[0] = 1
    nums[1] = 1
    for i in range(2,n):
        nums[i] = nums[i-1] + nums[i-2]
    return nums[n]

# Staircase problem with predefined step sizes of 1, 3 or 5
def num_ways_135(n):
    if n == 0:
        return 1
    total = 0
    for i in [1,3,5]:
        if n - i >= 0:
            total += num_ways_135(n - i)
    return total
# Inefficient

# Dynamic Programming Bottom-Up Approach with Memoization
def num_ways_135_BU(n):
    if n == 0:
        return 1
    nums = [0 for i in range(n+1)]
    nums[0] = 1
    for i in range(1,n):
        total = 0
        for j in [1,3,5]:
            if i - j >= 0:
                total += nums[i-j]
        nums[i] = total
    return nums[n]

print(num_ways_135_BU(5))
print(num_ways_135(5))


# Anagram Generation
# An anagram is the reordering of all the characters within a string
# The function returns an array of all the anagrams of a given string
# Having the base case of all possible anagrams of a 3 lettered word
# Time Complexity of Factorial: O(n!)
# Factorial Complexity is Extremely slow; Slower than Exponential Complexity O(2^n)

def anagram(string):
    if len(string) == 1: # Base Case with only 1 charactered string
        return [string[0]]

    collection = []
    substring_anagrams = anagram(string[1:len(string)]) # Recursion begins here, until there it hits the base case
    for substring in substring_anagrams: # First Recursion that runs this is when there are 2 letters
        for index in range(len(substring_anagrams) + 1): # Moves the non base case letter in front and back
            temp = substring.split() 
            temp.insert(index, string[0])
            copy = "".join(map(str,temp))
            collection.append(copy) # This adds it to the collection after all the repositionings then returns it
    return collection
# Basically the recursions here is that when the collection is returned, the 3rd element in the string 
# Is repositioned, and each reposition is an anagram, until no more repositionings remain
# Then its returned, now the 4th element in the string is repositioned... etc
# Repeated after all the elements have been repositioned
print(anagram("abc"))

# Exercise 1
# Function that accepts an array of strings and returns the total number of characters 
# across all the strings
# Top Down Approach, basically slowly cutting down the original problem into a small base case
def totalCharacters(stringArray):
    if len(stringArray) == 1:
        return len(stringArray[0])
    return len(stringArray[0]) + totalCharacters(stringArray[1:len(stringArray)])

print(totalCharacters(["ab", "c", "def", "ghij"]))

# Exercise 2
# Function accepts an array of numbers and returns a new array containing just the evens
def evens(numbersArray):
    if len(numbersArray) == 1:
        if numbersArray[0] % 2 == 0:
            return [numbersArray[0]] # Returns a list with single element so that we can concatonate the lists

    if numbersArray[0] % 2 == 0:
        return [numbersArray[0]] + evens(numbersArray[1:len(numbersArray)])
    else:
        return evens(numbersArray[1:len(numbersArray)])
    
print(evens([2,8,2,3,4,5,6,7,8]))

# Exercise 3
# Triangular Numbers: 1, 3, 6, 10, 15, 21, ... (Nth number in the pattern + Previous Numbers)
# Input Nth number in pattern and returns the proper value at that index
def triangularNth(N, i=1, value=1):
    if i > N - 1:
        return value
    i += 1
    return triangularNth(N, i, value + i)

print(triangularNth(7))

# Exercise 4
# Function input is a string and returns first index that contains character "x"
# Top Down Approach
def firstX(string, index=0):
    if string[0] == "x":
        return index
    return firstX(string[1:len(string)], index + 1)
print(firstX("abcdefghijklmnopqrstuvwxyz"))

# Exercise 5
# Unique Paths
# Function accepts a number of rows and a number of columns and calculates the number of possible
# "shortest" paths from upper-leftmost and lower-rightmost square
# Can only move to right or down
def uniquePaths(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return uniquePaths(rows - 1, columns) + uniquePaths(rows, columns - 1)
# Breaking down the problem into subproblems until we hit the base case

print(uniquePaths(5,5))


# Print Children
tree = {
    "Name":"John",
    "Children":[
        {
            "Name":"Suzie",
            "Children":[]
        },
        {
            "Name":"Zoe",
            "Children":[
                {
                    "Name":"Kyler",
                    "Children":[]
                },
                {
                    "Name":"Sophia",
                    "Children":[]
                }
            ]
        }
    ]
}

# Walks the tree with recursion
# Doesn't matter how DEEP this tree is
def printChildren(tree):
    if len(tree["Children"]) == 0:
        return
    for child in tree["Children"]:
        print(child["Name"])
        printChildren(child)

printChildren(tree)


# Top Down Recursion approach:
# Base Case
# Something that makes the input smaller that gets to the base case
# After the base case is reached, the function that is called within itself
# begins to return up the stacks returning the values that will be used in the 
# previous call stacks

# Can have multiple base cases

# Partitioning 
def count_partitions(n, m):
    if n == 0:
        return 1
    elif m == 0 or n < 0:
        return 0
    else:
        return count_partitions(n - m, m) + count_partitions(n, m - 1)

# Towers of Hanoi
# Function takes in n disks, starting rod (int) and ending rod (int)
# Returns a sequence of steps to move n disks
# from the start rod to the end rod
# Can use a helper funtion that prints out the moves

# Keys steps to Recursive Problem Solving
# f(n) be a recursive function
# 1. Show f(1) works (Base Case)
# 2. Assume f(n - 1) works
# 3. Show f(n) works using f(n - 1)

# Base Case: Can just move that one disk from Start Rod to End Rod

def hanoi(n, start, end):
    """
    Prints the list of steps required to move n disks from the start rod to the end rod
    >>> hanoi(2,1,3) returns 1 -> 2; 1 -> 3; 2 -> 3 
    """
    if n == 1:
        printMove(start, end)
    else:
        other = 6 - (start + end) # Other is the remaining rod
        hanoi(n - 1, start, other)
        printMove(start, end)
        hanoi(n - 1, other, end)

def printMove(start, end):
    """
    Prints a move in the correct format
    >>> printMove(1,3) returns 1 -> 3
    """
    print(start, "->", end)

hanoi(5,1,3)