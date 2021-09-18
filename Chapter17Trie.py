
# Trie Implementation
class TrieNode:
    def __init__(self):
        self.children = {} # Keys are english characters and values are instances of other TrieNodes
        # Each Node has this empty hash table
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # Prefix Search Implementation
    def search(self, word): # Input parameter is a string word/prefix we're searching for
        currentNode = self.root

        for char in word:
            if currentNode.children.get(char): # If current node has child key with current character
                currentNode = currentNode.children[char] # Following the child node
            
            else:
                return None # If current character isn't found among the current node's children, search word must not be in Trie

        return currentNode # Returns the last char that would assist the autocomplete feature
    
    def displayeachNode(self, node=None):
        currentNode = node or self.root
        for key, childNode in currentNode.children.items():
            print(key)
            if key != "*":
                self.displayeachNode(childNode)

    # Insertion Code Implementation
    def insert(self, word):
        currentNode = self.root

        for char in word:
            if currentNode.children.get(char): # If current node has child key with current character
                currentNode = currentNode.children[char] # Follow the child node
            else: # If current character DNE we add that character as a new node
                newNode = TrieNode()
                currentNode.children[char] = newNode

                currentNode = newNode # Follow the new node
        
        currentNode.children["*"] = None # After inserting the entire word into the Trie, add a * key-value at the end to the 
                                         # current node's hash table
    
    def collectAllWords(self, node=None, word="", words=[]):
        """This method accepts 3 arguments.
            node is the node whose descendants we're collecting words from
            word begins as an empty string and add characters to it as we move through the Trie
            words begins as an empty array and by the end of the function will contain all the words from the Trie"""
        # Recall default value of node is None
        currentNode = node or self.root # First calling is iterates over the child nodes of the root node
        
        for key, childNode in currentNode.children.items(): # Iteration through all the currentNode's children
            if key == "*":
                words.append(word)
            else: # Recursively call this function on the child nodes until end of the word is reached
                self.collectAllWords(childNode, word + key, words) # The word is created within the parameters 
        return words # As words is returned up the call stacks, it keeps the appended words
    
    def autocomplete(self, prefix): # Basic Autocomplete
        currentNode = self.search(prefix)
        if not currentNode: # If current node is NOT None
            return None
        return self.collectAllWords(currentNode) # runs when we call a node that has a None Child Node (End of a Word)

    def autocorrect(self, word):
        tempWord = ""
        potentialWords = []
        for character in word:
            tempWord += character
            currentNode = self.search(tempWord)
            if not currentNode:
                continue
            else:
                potentialWords += (self.collectAllWords(currentNode))

        for i in potentialWords:
            if i == word:
                return i

    def autocorrectSolution(self, word):
        currentNode = self.root
        # Need to keep track how much of the user's word found
        wordFoundSoFar = ""

        for char in word:
            if currentNode.children.get(char):
                wordFoundSoFar += char # If it exists within the Trie, Add it to the wordFoundSoFar variable
                currentNode = currentNode.children.get(char) # Follows the Child Node
            else:
                # If the current character isnt found among the current node's children, collect all the suffixes that descend from the current node
                # and get the first one. Concatenate the suffix with the prefix we've found so far to suggest the word the user meant
                # to type in
                return wordFoundSoFar + self.collectAllWords(currentNode)[0]
        
        return word # If the user's word is found within the Trie, just return the word
        

# The words array is allowed to be passed up and down the call stack since it remains the same object in memory
# even when new values are added to it
# This concept applies to Hash Tables as well
# (Memoization Technic)

# This doesn't work for strings since when a string is modified, a whole new string is created

# Exercise 1
# tag, tan, tank, tap, today, total, we, well, went

# Exercise 2

# Exercise 3
# Completed

# Exercise 4
