
# Basic Recursive Countdown Program

def Countdown(number):
    print(number)
    if number == 0: # Base Case
        return
    else:
        Countdown(number - 1)

#Countdown(10)
# A Base Case is required for the recursive function 
# This is where the function will no longer recurse

def factorial(number):
    if number == 1 or number == 0: # Base Case
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(4))

# File System Traversal with Recursion
# The os.walk generates a Tree Recursively
import os 
os.getcwd()

def FindCwdDirectories():
    for dirpath, dirnames, filenames in os.walk(os.getcwd()): # getcwd() returns 3 elemented tuples
        print(
            f"Root: {dirpath}\n"
            f"Sub-Directories: {dirnames}\n"
            f"Files: {filenames}\n\n"
        )

FindCwdDirectories()

# Exercise 1
# The Base Case is when low <= high

# Exercise 2
# Stack Overflow, due to infinite recursion

# Exercise 3
# Recursively Sum up all the numbers between low and high
def sum(low, high):
    if high == low:
        return low
    return high + sum(low, high - 1)
print(sum(1,10))

# Exercise 4
def sumNumsOfArray(array):
    for i in array:
        if isinstance(i, int):
            print(i)
        else:
            sumNumsOfArray(i)

sumNumsOfArray([ 1,
2,
3,
[4, 5, 6],
7,
[8,
[9, 10, 11,
[12, 13, 14]
]
],
[15, 16, 17, 18, 19,
[20, 21, 22,
[23, 24, 25,
[26, 27, 29]
], 30, 31
], 32
], 33
]
)


# CS Dojo
# Dynamic Programming

def fibonacci(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    return result

# This works but inefficient since it has to repeat computations when each recursive
# computation takes place
# O(2^n) Exponential Complexity

# Use an array to memoize computations

def fib(n, memoize):
    if memoize[n] != None: # Doesnt recompute the value of fibonacci at n
        return memoize[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    memoize[n] = result
    return result

# Need to initialize memoize array prior to calling the fib function
# Complexity O(2n + 1) * O(1) => Linear O(n)


# Buttom Up Approach to Dynamic Programming
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottomUp = [None for i in range(n)]
    bottomUp[0] = 1
    bottomUp[1] = 1
    for i in range(2,n):
        bottomUp[i] = bottomUp[i-1] + bottomUp[i-2]
    return bottomUp

print(fib_bottom_up(10))
