# Average of even elements given an array of ints
def averageOfEvens(listArray):
    sumEvens = 0
    countOfEvens = 0

    for i in listArray: # At least n steps since iterates over n elements
        if i % 2 == 0: # Comparison
            sumEvens += i # Modify
            countOfEvens += 1 # Modify 
    
    return sumEvens / countOfEvens

print(averageOfEvens([1,2,3,4,5,6,7,45,3,2,1,3,4]))
# Analyzing 
# More steps performed for evens than odds => 3n
# 2 Steps before the loop and a final step after => 3
# Overall: Linear Complexity O(3n + 3) => O(n)

# Word Builder
# Returns an array of 2 letter combos of every element in the array
# Takes in an array of strings
def wordBuilder(listArray):
    collection = []

    for i in range(len(listArray)):
        for j in range(len(listArray)):
            if (i != j): # Comparison
                collection.append(listArray[i] + listArray[j]) # Insertion

    return collection
# Analyzing
# Loop with a nested loop where both iterate over all the elements => n^2
# 2 steps within inner loop
# Overall Quadratic Complexity O(n^2)


# Array Sample
def sample(listArray):
    first = listArray[0]
    middle = listArray[int(len(listArray) / 2)]
    last = listArray[-1]

    return [first, middle, last]

# This function takes the same number of steps regardless of how many n elements there are
# The number of steps is constant thus Linear Complexity O(n)


# Average Celsius Reading
# Need to convert to Celsius from fahrenheit and find Average as well
# Complexity is Linear Complexity O(2n) => O(n)
def averageCelsius(fahrenheitReadings):
    celsiusNumbers = []

    # Converts each reading to Celsius and adds to the celsiusNumbers Array
    for i in fahrenheitReadings:
        celsiusConversion = (i - 32) / 1.8
        celsiusNumbers.add(celsiusConversion)
    
    celsiusSum = 0
    for i in celsiusNumbers:
        celsiusSum += i
    
    return celsiusSum / len(celsiusNumbers)

# Clothing Labels
# string Array input Parameter
# Creates text for every possible label needed
# Labels contain the item name + size (1-5)
def markInventory(clothingItemsArray):
    clothingOptions = []

    for item in clothingItemsArray: 
        for size in range(1,6): # This is a nested loop however is not affect by the size of n elements; Runs 5x
            clothingOptions.append(item + " Size: " + str(size))
    return clothingOptions
# Linear Complexity O(5n) => O(n)


# Count The Ones
# Accepts array of arrays
    # Inner Array accepts 1s and 0s
    # Function returns how many 1s there are
def countOnes(outerArray):
    count = 0

    for innerArray in outerArray:
        for i in innerArray:
            if i == 1:
                count += 1
    
    return count
# Linear Complexity O(n)
# Outer loop only iterations over inner arrays
# Inner loop is iterating over actual numbers
# Inner loop only runs for as many numbers as there are in total
# Even though this has nested loops, we're just iterating over how many elements there are in total
    # within the inner arrays

# Palindrome Checker
# Checks if words are the same when reversed
def isPalindrome(aString):
    leftIndex = 0
    rightIndex = len(aString) - 1

    # Iterate over string until reach center of string
    while (leftIndex < len(aString) / 2):
        if aString[leftIndex] != aString[rightIndex]:
            return False
        
        leftIndex += 1
        rightIndex -= 1
    
    return True
# Linear Complexity O(n/2) => O(n)

print(isPalindrome("aaoogooaa"))

# Get All The Products
# Returns an array where the elements are products of the elements in given input parameter array
# index 0 element multiplies with all the indices to the right and adds them to the new array
# Move over to index 1 and then repeat...
    # Array of 4 elements: New Array is 3 + 2 + 1 elements long
def twoNumberProducts(listArray):
    products = []
    for i in range(len(listArray)): # Ran (n - 1)x
        for j in range(i + 1, len(listArray)): # The inner loop is 1 less than Outer loop
            products.append(listArray[i] * listArray[j])
    return products
    
print(twoNumberProducts([1,2,3,4,5]))

# This method has n + (n - 1) + (n - 2) + ... + 1 steps
# Computes to n^2 / 2
# Thus has Quadratic Complexity O(n^2)


# Dealing with Multiple Datasets
# Compute the product of every number from one array by every number of a second array
# Returns an array of products
def twoNumberProducts(array1, array2):
    products = []

    for i in range(len(array1)):
        for j in range(len(array2)):
            products.append(array1[i] * array2[j])
    
    return products

# Complexity is determined by the sizes of the 2 different arrays that can vary in size
# Complexity is expressed as O(n*m)
# When working with 2 different datasets, need to express that there are different datasets being worked with


# Password Cracker
# Parameter is an integer that determines the size of the password string would be created by brute force
# Goes through all 26 letters:
    # input 3 -> aaa, aab, aac, ..., zzx, zzy, zzz
# Would be an extremely slow algorithm
# Complexity Breakdown
    # 26 letters
    # Input 3 would lead to 26*26*26 => 26^3
# Exponential Complexity O(2^n) (Extremely Slow)

# Exercise 1
# Function returns True if given array is a 100-Sum Array
    # First and Last numbers add up to 100
    # Second and Second-to-last numbers add up to 100... etc
    # Only works with an even amount of elements
def oneHunnetSum(listArray):
    leftIndex = 0
    rightIndex = len(listArray) - 1

    while leftIndex < len(listArray) / 2: # Only Iterates up to half of the elements in the array
        if listArray[leftIndex] + listArray[rightIndex] != 100:
            return False
        
        leftIndex += 1
        rightIndex -= 1
    
    return True
# Linear Complexity O(n)
print(oneHunnetSum([99,90,10,1]))


# Exercise 2
# Function merges 2 sorted arrays together to create a new sorted array containing values from both arrays
def merge(array1, array2):
    newArray = []
    array1pointer = 0
    array2pointer = 0

    while array1pointer < len(array1) or array2pointer < len(array2):

        # Check if already reached the end of the first array
        if not array1[array1pointer]: # Say if NOT empty
            newArray.append(array2[array2pointer])
            array2pointer += 1
        
        elif not array2[array2pointer]:
            newArray.append(array1[array1pointer])
            array1pointer += 1
        
        elif array1[array1pointer] < array2[array2pointer]:
            newArray.append(array1[array1pointer])
            array1pointer += 1
        
        else:
            newArray.append(array2[array2pointer])
            array2pointer += 1
        
    return newArray
# This would work with JavaScript



# Exercise 3
# Find a Needle in a hay stack
# Seaching a string within another string
    # string1 = "aa"
    # string2 = "afnafnaafoafmoeg"
    # Would look for a string of the size of string1 that equals a substring in string2
def findNeedle(needleString, haystackString):
    needleIndex = 0
    haystackIndex = 0

    while haystackIndex < len(haystackString) - 1:
        if needleString[needleIndex] == haystackString[haystackIndex]:
            foundNeedle = True
        
        while needleIndex < len(needleString) - 1:
            if needleString[needleIndex] != haystackString[haystackIndex + needleIndex]:
                foundNeedle = False
            needleIndex += 1
        
        if foundNeedle:
            return True
        
        haystackIndex += 1
    
    return False

print(findNeedle("al", "shalom"))
# Complexity O(n*m)


# Exercise 4
# Returns the greatest product of three numbers from a given array
def largestProduct(listArray):
    largestProductSoFar = listArray[0] * listArray[1] * listArray[2]
    i = 0

    while i < len(listArray):
        j = i + 1
        while j < len(listArray):
            k = j + 1
            while k < len(listArray):
                if listArray[i] * listArray[j] * listArray[k] > largestProductSoFar:
                    largestProductSoFar = listArray[i] * listArray[j] * listArray[k]
                k += 1
            j += 1
        i += 1
    
    return largestProductSoFar
# Complexity would be O(n^3)
print(largestProduct([1,2,3,1,5,6,1,7]))


# Exercise 5
# Returns a single element from an array
# Removes top half then bottom half then top half...until 1 element remains

def pickResume(resumes):
    eliminate = "top"

    while len(resumes) > 1:
        if eliminate == "top":
            resumes = resumes[int(len(resumes) / 2): len(resumes) - 1]
            eliminate = "bottom"
        elif eliminate == "bottom":
            resumes = resumes[0: int(len(resumes) / 2)]
            eliminate = "top"
    
    return resumes[0]
# Linear Complexity O(logn) since each loop elimates half of the remain elements
# Remember everytime the data is doubled the algorithm time increases by 1 step
print(pickResume(["Adam", "Eve", "ShalomMan", "Reaps", "Tanks", "War", " OOF", "CRINGE"]))
