
# Recursive function that finds the greatest number from an array
def greatestNumber(array):
    if len(array) == 1: # Base Case
        return array[0]
    
    if array[0] > greatestNumber(array[1:len(array)]):
        return array[0]
    else:
        return greatestNumber(array[1:len(array)])

# Each recursive call is the comparison of a single number: array[0]
# To the greatest number from the remained of the array
# This is inefficient
# The recursive call that hits the base case is recalled twice with 2 elements
# Gets worse as we increase the number of total elements
# With 4 elements, the base case is called 15 times
# Exponential Complexity O(2^n) (Every data element added doubles the steps)
print(greatestNumber([1,2,3,4]))

# Fixing the time complexity for Big O
def greatestNumberFixed(array):
    if len(array) == 1:
        return array[0]
    # The greatest number is calculated and stored in a variable
    greatest_remainder = greatestNumberFixed(array[1:len(array)])

    if array[0] > greatest_remainder:
        return array[0]
    else:
        return greatest_remainder
# Linear Complexity O(n)
print(greatestNumberFixed([1,2,3,4]))

# Fibonacci Sequence
def fib(n):
    if n == 0 or n == 1: # Base Case
        return n
    return fib(n - 2) + fib(n - 1) # Returns the sum of the previous two fibonacci numbers

# Simple, HOWEVER there are two recursive calls at same time
# Can easily lead to Exponential Complexity
# Case of overlapping subproblems

# Optimizing the Fibonacci Sequence Function
# Dynamic Programming through Memoization
# Use a default 2nd parameter that is a hash table
# Input is the index of the number within the Fibonacci Sequence
def fibMemoization(n, memo={}):
    if n == 0 or n == 1: # Base Case
        return n
    # Check if fib(n) previously computed and within hash table
    if not memo.get(n): # Does the calculation if fib(n) DNE within hash table
        memo[n] = fibMemoization(n - 2, memo) + fibMemoization(n - 1, memo)
    return memo[n] # If it exists, just grab that calculated number

print(fibMemoization(10))
# Linear Complexity O(2n - 1) => O(n)

# Bottom-Up Fibonacci Sequence Function
def fibBU(n):
    if n == 0:
        return n
    a = 0 # 0th Fib Element
    b = 1 # 1st Fib Element
    for i in range(1,n):
        temp = a
        a = b # a shifts up to b's spot
        b = temp + a # This is b shifting up to the next Fib element... etc
    return b
# a and b just keep track of the elements within the Fibonacci Sequence
# Linear Complexity O(n) since only takes steps from 1 to n
print(fibBU(10))


# Exercise 1
# Fix function so that it does not make unnecassary recursive calls
def addUntil100(array):
    print("RECURSION")
    if len(array) == 0: # Base Case
        return 0
    nextNum = addUntil100(array[1:len(array)]) # Just made sure the recursive call was made once and added value to a variable
    if array[0] + nextNum > 100:
        return nextNum
    else:
        return array[0] + nextNum

sol = addUntil100([20,20,20,30,30,30,30])
print(sol)

# Exercise 2
# Golumn Sequence Function: Calculates the nth value of this sequence
# Use Memoization to fix efficiency
def golumn(n, memo={}):
    if n == 1:
        return 1
    if not memo.get(n):
        memo[n] = 1 + golumn(n - golumn(golumn(n - 1, memo), memo), memo)
    return memo[n]

print(golumn(5))

# Exercise 3
# Improve Efficiency of the Unique Paths Solution with Memoization
def unique_paths(rows, columns, memo={}):
    if rows == 1 or columns == 1:
        return 1
    if not memo.get((rows, columns)): # Used a Tuple to store as a key within the dictionary
        memo[(rows, columns)] = unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)
    return memo[(rows, columns)]

answer = unique_paths(3,3)
print(answer)
