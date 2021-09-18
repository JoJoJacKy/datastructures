
# Dictionaries in Python are Hash Tables

# Simple Thesaurus
thesaurus = {"ooga":"booga"}
thesaurus["bad"] = "evil"
thesaurus["cab"] = "taxi"
thesaurus["ace"] = "star"

for key in thesaurus.keys():
    print(thesaurus[key]) # Prints out the values of each key

Doggos = [
    {"Name":"Fido", "Breed":"Pug", "Age":3, "Gender":"Male"},
    {"Name":"Bunion", "Breed":"Tarrier", "Age":11, "Gender":"Male"},
    {"Name":"Ooga", "Breed":"Pitubll", "Age":2, "Gender":"Female"},
]

# Array Subset
# Determining if one array is a subset of another
arr1 = ["a", "b", "c", "d", "e", "f"]
arr2 = ["b","d", "f"] # This is a subset of arr1

arr3 = ["e", "f", "g"] # This is NOT a subset of arr1

# Function that uses Hash Table to Determine whether smaller array is subset
# O(n) Complexity
# Uses a Hash Table as an Index
def hashSubset(array1, array2):
    if len(array1) < len(array2):
        smallerArray = array1
        largerArray = array2
    else:
        smallerArray = array2
        largerArray = array1
    
    hashTable = {} # Creating an empty hash table, then add each item of the largerArray as a key with True as its value

    for i in largerArray: # Allows for O(1) lookups of these items
        hashTable[i] = True # Adding the elements within the hash table as keys
    
    for i in smallerArray:
        if not hashTable.get(i, False): # If !True = False so doesn't run if element of subset contained within superset
            return False # Immediately returns false if key element DNE in SuperSet
    
    return True # Implies all the elements of subset are contained within superset

print(hashSubset(arr1, arr2))

# Exercise 1
# Function that returns an array that is the intersection of two given arrays
# [1,2,3,4] and [1,2] = [1,2]
# O(n) complexity

def interSectionFunc(array1, array2):
    if len(array1) > len(array2):
        largerArray = array1
        smallerArray = array2
    else:
        largerArray = array2
        smallerArray = array1
    
    hashIndex = {}

    for i in largerArray:
        hashIndex[i] = True
    
    interSectedArray = []
    for i in smallerArray:
        if hashIndex.get(i, False):
            interSectedArray.append(i)
    return interSectedArray

print(interSectionFunc([6,7,0], [2,3,4,8,0]))

# Exercise 2
# Inputs an array of strings, returns first duplicate value it finds

def duplicateFinder(array):
    hashingIndex = {}
    for i in array: # Adds to dictionary if it DNE within the dictionary
        if not hashingIndex.get(i, False): # Doesn't run if Key already exists within the dictionary
            hashingIndex[i] = True
        else:
            return i
    return None

print(duplicateFinder([1,2,3,4,4]))

# Exercise 3
# Inputs a string that contains all the letters of the alphabet and returns the missing letter
def singleLetterReturner(stringer):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    hashAlphabetTable = {}
    for i in alphabet:
        hashAlphabetTable[i] = 0
    
    for i in stringer:
        hashAlphabetTable[i] += 1
    
    for key, value in hashAlphabetTable.items():
        if value == 0:
            return key
    
    return None

print(singleLetterReturner("the quick brown box jumps over a lazy dog"))

# Exercise 4
# Inputs a string, returns the first non-duplicated character in the string

def firstNonDuplicate(stringer):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    hashAlpha = {}
    for i in alphabet:
        hashAlpha[i] = 0
    
    for i in stringer:
        hashAlpha[i] += 1
    
    for j in stringer:
        if hashAlpha[j] == 1:
            return j
    return None

print(firstNonDuplicate("minimum"))

