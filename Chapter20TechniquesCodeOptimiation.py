
# Optimizing Look-Ups
# This function has time complexity O(n * m)
def connect_books_with_authors(books, authors):
    books_with_authors = []

    for book in books:
        for author in authors:
            if book["author_id"] == author["author_id"]:
                books_with_authors.append({"title":book["title"], "author":author["name"]})
    
    return books_with_authors

# Want to look up the authors at O(1) speed
# End up with time complexity of O(n + m)
def connect_books_with_authors_opt(books, authors):
    books_with_authors = []
    author_hash_table = {}

    for author in authors:
        author_hash_table[author["author_id"]] == author["name"]
    
    for book in books:
        books_with_authors.append({"title": book["title"], "author":author_hash_table[book["author_id"]]})
    
    return books_with_authors

# Two-Sum Problem
# A function that takes in a number array and returns True if 2 numbers add up to 10
# Nested Loop Implementation; Time Complexity O(n^2)
def twoSum(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] + array[j] == 10:
                return True
    return False

# Optimized
def twoSumOpt(array):
    hashTable = {}
    for i in range(len(array)):
        if hashTable.get(10 - array[i], False): # Checking if the hashTable contains the key
            return True

        hashTable[array[i]] = True # If not add it
    
    return False

a = [0,1,2,3,4,5,6,7]
print(twoSumOpt(a))


# Recognizing Patterns
# A pile of coins, two players, each player can take 1 or 2 coins from pile in their turn
# Player who removes the last turn loses
# Means a player can force their opponent to lose the game
# Recursively Implement function that can show if winner based on number of coins within pile
# Since calls two recursive statements in a single line => Exponential Time Complexity O(2^n)
def game_winner(number_of_coins, current_player="you"):
    if number_of_coins <= 0: # Means the opponent took the last coin which defaults current player has won
        return current_player
    
    if current_player == "you":
        next_player = "them"
    elif current_player == "them":
        next_player = "you"
    
    if game_winner(number_of_coins - 1, next_player) == current_player or game_winner(number_of_coins - 2, next_player) == current_player:
        return current_player
    
    else:
        return next_player
# Use memoization to improve speed 
# Can also find a pattern by inputing a bunch of examples and studying the results
# Constant Time Complexity
def game_winner(number_of_coins):
    if (number_of_coins - 1) % 3 == 0:
        return "them"
    else:
        return "you"

# The Sum Swap Problem
# Use pattern recognition and magical look ups together to optimize an algorithm

# Function is given two number arrays of inputs
# The arrays have their own different sums, and the function wants to swap one element
# from each array so that both arrays have the same sum
# If no swap possible returns None

# Can begin with O(n * m) Time Complexity with nested loops
# But can strive to make it O(n + m) Time Complexity
# One Pattern, the larger sum array needs to swap a larger number with a smaller number from the
# smaller sum array
# Each array's sum changes by the same amount
# When swap happens, the sums become the average of the 2 sums before the swap

def sum_swap(array1, array2):
    hashTable = {} # Stores the values of the first array
    sum1 = 0
    sum2 = 0

    # Get the sum of the first array while storing its elements within the hash table with an index
    for index, num in enumerate(array1):
        sum1 += num
        hashTable[num] = index
    
    for num in array2:
        sum2 += num
    
    shiftAmount = (sum1 - sum2)/2

    for index, num in enumerate(array2):
        # First check hash table for number's counterpart within the first array
        # Calculated as the current number + shiftAmount
        if hashTable.get(num + shiftAmount, None):
            return [hashTable[num + shiftAmount], index]
    
    return None

# Greedy Algorithms

# Array Max Algorithm
# Option 1: Nested Loops O(n^2)
# Option 2: Quicksort Ascending Order then return last element O(nlogn)

# Option 3: Greedy Algorithm O(n)
def maxElement(array):
    greatest_number = array[0] # First Number assumed to be the greatest element
    for i in array:
        if i > greatest_number:
            greatest_number = i
    return greatest_number

# Largest Subsection Sum
# Function that accepts an array of numbers and returns the largest sum
# that can be computed from any "subsection" of the array
# Find the largest sum from any length of subsection in a row

# Using a Greedy Algorithm, go through the subsections until hit a sum that becomes less than 0
# Reset the sum back to 0 and go onto the next index to sum up the numbers again
# Linear Time Complexity O(n)
def max_sum(array):
    currentSum = 0
    greatestSum = 0

    for num in array:
        if currentSum + num < 0: # This is when the reset occurs
            currentSum = 0
        else:
            currentSum += num # If no reset, just sums up the numbers within subsection

            if currentSum > greatestSum: # Checks if needs to update the greatest sum variable
                greatestSum = currentSum
    
    return greatestSum

# Greedy Stock Predictions
# Function accepts an array of stock prices and determines whether there are any 3 pieces
# that create an upward trend
# A right hand price is greater than a middle price and left hand price
# Function returns True if there is upward trend of three prices
# False otherwise

# Use greed to grab the lowest and middle and upper prices
# Initially set the middle price variable to infinity
# Single Pass through of array
    # 1. If current price is lower than the lowest price encountered so far, set it to the lowest price
    # 2. If current price is higher than the lowest price but lower than the middle price
        # update middle price to be current price
    # 3. If current price is higher than the lowest and middle price, means we've found a 
        # three-price upward trend
# Linear Time Complexity O(n)
def increasing_triplet(array):
    lowest_price = array[0]
    middle_price = float('inf') # Infinity

    for price in array:
        if price <= lowest_price:
            lowest_price = price

        elif price <= middle_price:
            middle_price = price
        
        else:
            return True
    
    return False

# As long as the pointer reaches a number greater than the middle price at the end
# returns True as the 3 Trend is present

# The Anagram Checker
# Function whose inputs are 2 strings and determines whether they are anagrams of one another
# If create anagrams of one string and compare them to the other string
    # Would be a function of Time Complexity O(n!)

# However, iterating through both strings one would be Time Complexity O(n + m)

# This is an O(n * m) implementation 
def areAnagrams(firstString, secondString):
    secondStringArray = list(secondString) # Converting to an array since strings are immutable

    for i in range(0, len(firstString)):
        if len(secondStringArray) == 0:
            return False
        
        for j in range(0, len(secondStringArray)):
            if firstString[i] == secondStringArray[j]:
                del secondStringArray[j] # Can delete elements within lists
                break
    return len(secondStringArray) == 0

# Can sort the arrays to get a Time Complexity O(nlogn + mlogm)
# areAnagram algorithm that converts the strings into hash tables
# and tallies the count of each type of character
def areAnagramsOpt(firstString, secondString):
    firstWordHashTable = {}
    secondWordHashTable = {}

    # Create a hash table out of first string
    for char in firstString:
        if firstWordHashTable.get(char):
            firstWordHashTable[char] += 1
        else:
            firstWordHashTable[char] = 1
    
    # Create a hash table for the second string
    for char in secondString:
        if secondWordHashTable.get(char):
            secondWordHashTable[char] += 1
        else:
            secondWordHashTable[char] = 1
    
    return firstWordHashTable == secondWordHashTable

# Group Sorting
# Given an array of strings and want to sort the groups of data inside
# Don't care about the order of the groups
# Just the data within the groups
# Use a hash table to add the elements from the array onto the hash table
# Then create a new array and repopulate it with the currect number of each string
# Linear Time Complexity O(n) | Space Complexity O(n)
def group_array(array):
    hash_table = {}
    new_array = []

    # Store the tallies of each string within the hash table
    for value in array:
        if hash_table.get(value): # Check if the value exists within the hash table
            hash_table[value] += 1 # If it does, tally up the key
        else:
            hash_table[value] = 1 # If not, add the key to the hash table
    
    # Now iterate over the hash table and populate a new array with the currect number of each string
    for key, count in hash_table.items(): # Iterate over all the items (Key-Value Pairs) of the hash table
        for i in range(count):
            new_array.append(key)
    
    return new_array

testArray = ["a", "c", "d", "b", "b", "c", "a", "d", "c", "b", "a", "d"]
print(group_array(testArray))


# Exercise 1
basketball_players = [
{"first_name": "Jill", "last_name": "Huang", "team": "Gators"},
{"first_name": "Janko", "last_name": "Barton", "team": "Sharks"},
{"first_name": "Wanda", "last_name": "Vakulskas", "team": "Sharks"},
{"first_name": "Jill", "last_name": "Moloney", "team": "Gators"},
{"first_name": "Luuk", "last_name": "Watkins", "team": "Gators"}
]
football_players = [
{"first_name": "Hanzla", "last_name": "Radosti", "team": "32ers"},
{"first_name": "Tina", "last_name": "Watkins", "team": "Barleycorns"},
{"first_name": "Alex", "last_name": "Patel", "team": "32ers"},
{"first_name": "Jill", "last_name": "Huang", "team": "Barleycorns"},
{"first_name": "Wanda", "last_name": "Vakulskas", "team": "Barleycorns"}
]
# Input 2 arrays, returns an array of the players who play in both sprots
# Make sure its O(n + m) Time Complexity
def multipleSports(firstArray, secondArray):
    bigNames = {}
    bigNamesReturnArray = []
    for i in firstArray:
        if bigNames.get(i["first_name"]):
            bigNames[i["first_name"]] += 1
        else:
            bigNames[i["first_name"]] = 1
    for i in secondArray:
        if bigNames.get(i["first_name"]):
            bigNames[i["first_name"]] += 1
        else:
            bigNames[i["first_name"]] = 1
    
    for name, counter in bigNames.items():
        if counter > 1:
            bigNamesReturnArray.append(name)
        else:
            continue
    return bigNamesReturnArray

print(multipleSports(basketball_players, football_players))

# Exercise 2
# Function that accepts an array of natural numbers, from 0 up to n
# However the array will be missing one number
# Must return the missing one

missingArray = [2, 3, 4, 6, 1, 0] # Must return 0
missingArray2 = [8, 2, 3, 9, 4, 7, 5, 1, 0] # Must return 0
# Function must be Linear Time Complexity of O(n)
def returnMissingInteger(array):
    hashTable = {}
    for i in array:
        hashTable[i] = True
    for j in range(len(array)):
        if not hashTable.get(j+1):
            return j + 1
    if not hashTable.get(0):
        return 0
    return None
print(returnMissingInteger(missingArray2))

# Exercise 3
# Function that calculates the greatest profit that could be made from a single "buy"
# transaction followed by a single "sell" transaction
priceArray = [10, 7, 5, 8, 11, 2, 6]
# Means day 1, close at 10$, day 2 close at 7$ etc
# So max profit means, buy at 5$ (Day 4) and sell at 11$ (Day 6)
# Wants Linear Time Complexity
#def maximizeSellBuy(array):
    
    #for day, price in enumerate(array):


# Exercise 4
# Function accepts an array of numbers and computes the highest product of any of the two numbers
# Within the array.
numsArray = [5, -10, -6, 9, 4]
def greatestProduct(array):
    negatives = []
    positives = []

    for i in array:
        if i >= 0:
            positives.append(i)
        else:
            negatives.append(i)
    
    greatestProdNum = 0


# Exercise 5
