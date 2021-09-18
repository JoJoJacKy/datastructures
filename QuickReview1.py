# Recursion and Recursive Patterns

# Recursion occurs when something is defined in terms of itself

def factiorial(n):
    if n == 0:
        return 1
    return n * factiorial(n-1)

A = factiorial(5)
print(A)

def walk_list(L, f): # function f returns a bool 
    if L == []:
        return None
    if f(L[0]): # Checks the first indexed element of the list to see if it satisfies the condition
        return L[0]
    return walk_list(L[1:], f) # If element doesn't satisfy the function condition then skips to next element

walked = walk_list([1,2,3,4], lambda x: x > 2)
print(walked)

def walk_list_filter(L, f):
    """Walk a list, returning a list of items that satisfy the condition f.
    This implementation uses the stack to hold intermediate results,
    and completes construction of the return list upon return of the 
    recursive call"""

    if L == []:
        return []
    if f(L[0]):
        # The following waits to build and then return the list until
        # after the recursive call comes back with a sub-result
        return [L[0]] + walk_list_filter(L[1:], f)
    else:
        return walk_list_filter(L[1:],f)

# The first indexed element is checked to see if it satisfies the given function
# If it does, it keeps it ready
# If the first element doesn't satisfy the condition it skips the first index element
# And passes in the new modified list minus the checked element
walking = walk_list_filter([1,2,3,4,5], lambda x: x % 2 == 1)
print(walking)

a = [1,2]
b = [3,4]
c = a + b # Adds the list into a new list combined
print(c)

# Walking Filter that returns a list but with a helper method
# (Tail Recursion)
def walk_list_filter2(L, f, so_far=None):
    """Walk a list, returning a list of items that satisfy the condition f.
    This implementation uses an explicity 'so_far' variable that holds the return
    value as it is being built up incrementally on each call.
    
    Example: >>> walk_list_filter2([1,2,3,4], lambda x: x % 2 == 1)
    returns [1,3]
    """
    so_far = so_far if so_far is not None else [] # If so_far is None, so_far = []; If so_far is a list, then it is equal to the list
    if L == []: # Once there are no more elements in the list L, returns so_far
        return so_far
    if f(L[0]): # If the first indexed element condition is met, appends the element to the so_far list
        so_far.append(L[0])
    return walk_list_filter2(L[1:], f, so_far)

TwoFast2Walking = walk_list_filter2([1,2,3,4,5,6,7,8,9], lambda x: x % 2 == 1)
print(TwoFast2Walking)
print("-------")
a = 2
b = 1
x = a if a % 2 == 0 else "not even"
y = b if b % 2 == 0 else "not even"
print(x)
print(y)

# Recursive Walkers for Trees
# Our simple tree structure is a simple nested list structure
# A node in the tree is represented as a list with the first element being the node value
# The first node is parent of the rest of the children nodes
# Every parent node is the first element of the list, every other child node is a list
tree1 = [13, [7, [1, [2], [3], [2, [3]]]], [8, [99], [16, [77, [1]]], [42]]]
# 13 is parent of 7 and 8
    # 8 is parent of 99, 16, 42
        # 16 parent of 77

# Representing the tree
# 13
    # 7
    # 8
        # 99
        # 16
            # 77
        # 43

def tree_max(tree):
    """Walks a tree, returns the maximum value in the assumed non-empty tree.
    Example: tree_max([13, [7], [8, [99], [16, [77]], [42]]])
        returns 99"""
    value = tree[0]
    children = tree[1:]
    if not children: # The base case; Runs when children is an empty list (!false = true)
        return value
    return max(value, max(tree_max(child) for child in children))

a = [1]
print(a[1:]) # This is creating a new list that is empty, it is accessing elements that DNE
if a: # This runs if a is not empty; If a is empty, this is false
    print("Not empty")
if not a[1:]: # This is an empty list
    print("empty list")

print(tree_max(tree1))
print("TREEEEEEEEEEEEEEEEEEEEEE")
def depth_tree(tree):
    """Walks a tree, returns the depth of the tree. (How many layers deep the tree is).
    """
    if tree == []: # Base case
        return 0

    children = tree[1:]
    if not children: # Another Base Case
        return 1
    return max(1 + depth_tree(child) for child in children) # The child in children are all the children nodes of the first node (First node passed in was the parent node)

print(depth_tree(tree1))

# Builder/Maker Function that recusrively creates a tree structure
# Balances the tree from left to right by the number of nodes in each branch

def make_tree(L):
    """Makes and returns a binary tree corresponding to the list. The tree is 'binary' in the sense
    that the number of left and right branches are balanced as much as possible, but no condition is
    imposed on the left/right values under each node in the tree."""

    n = len(L)
    if n == 0: # Base Case
        return []
    
    value = L[0]
    if n == 1: # Another Base Case - No Children
        return [value] # Returns a list with a single element
    elif n == 2: # Another Base Case - One Child
        return [value, [L[1]]] # Returns a list with 2 elements, 1 element being a child of the first
    
    split = n // 2
    left = make_tree(L[1:split+1]) # Recursion on left half of the children
    right = make_tree(L[split+1:]) # Recursion on the right half of the children

    return [value, left, right] # Combines and returns

tree2 = make_tree([1,2,3,4,5,6,7])
print(tree2)

def show_tree(tree, level=0):
    """Return a formatted string representation to visualize a tree"""
    spaces = '  '
    if not tree:
        return ""
    value = tree[0]
    children = tree[1:]
    result = spaces*level + str(value) + '\n'
    for child in children:
        result += show_tree(child, level + 1)
    return result

print("tree1:", tree1, "\n", show_tree(tree1))

# Recursive Directed Graphs (Digraphs)
# Represented as a Dictionary with Node Names as Keys
    # Each key has a list holding the node value and a list of children node names
    # A special name 'root' is the root of the graph

# 'root' is the root node of the graph
# Each node key contains a list value where in the list
    # First index is the value of the node,
    # Second index is a list of names of its children nodes
graph1 = {'root': [13, ['A', 'B']],
            'A' : [77, ['B', 'C']],
            'B' : [88, []],
            'C' : [-32, ['D']],
            'D' : [42, []]}

# Walking Digraphs with no cycles
def graph_max(graph):
    """Walk a graph starting from 'root', returns the maximum value in a (non-empty) graph.
    First, we'll assume there are no cycles in the graph.
    """

    def node_max(node_name): # The names of the nodes are automatically passed in
        value = graph[node_name][0] # Integer Value of the Node 
        children = graph[node_name][1] # List of the children of the node
        if children: # Runs if the children list is NOT EMPTY
            # return max(int, max(collection of ints))
            return max(value, max(node_max(child) for child in children)) # The 2nd parameter produces a collection that max() picks the max value from
        return value # Once there are no more children, just returns the value of the named node
    
    return node_max('root') # First Recursive Call runs the node_max function

print(graph_max(graph1))
print( list(i+1 for i in[1,2,3,4,5]) )
# i for i in [1,2,3,4,5] This returns a collection
# This is List Comprehension

# Walking Digraphs with cycles present
graphWithCycles = {'root' : [13, ['A', 'B']],
                    'A' : [77, ['B', 'C']],
                    'B' : [88, []],
                    'C' : [-32, ['D']],
                    'D' : [42, ['A']]} # D leads back to A

def graph_max2(graph):
    """Walk a graph starting from 'root', returns the maximum value in a non-empty graph.
    Now, however, there might be cycles, so need to be careful not to get stuck in them!"""
    visited = set()

    def node_max(node_name):
        visited.add(node_name)
        value = graph[node_name][0]
        children = graph[node_name][1]
        new_children = [c for c in children if c not in visited] # Adds c to the list if it DNE in visited
        if new_children: # Runs as long new_children a non empty list
            return max(value, max(node_max(child) for child in new_children))
        return value
    return node_max('root')

listOfNums = [1,2,3,4,5,6,7,8,9,10,11,12]
listOfEvens = [evenNum for evenNum in listOfNums if evenNum % 2 == 0]
# List Comprehension
# [expression with i (for i in collection) CONDITION with i] 
# The Condition is not required
print(listOfEvens)

print(graph_max2(graphWithCycles))

# Circular Lists
# Python list have themselves as an element, in essence python lists might be graphs
# and have cycles within them
x = [0, 1, 2]
x[1] = x
print("x:", x)

def deep_copy_list(old, copies=None):
    if copies is None:
        copies = {}
    
    oid = id(old) # Gets the unique python object-id for old

    if oid in copies:
        return copies[oid]
    
    if not isinstance(old, list): # Base Case: Not a list, remember and return it
        copies[oid] = old
        return copies[oid]
    
    # Recursive Case
    copies[oid] = []
    for e in old:
        copies[oid].append(deep_copy_list(e, copies))
    

