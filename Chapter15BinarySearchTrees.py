
class BinaryTreeNode:
    def __init__(self, value, leftChild=None, rightChild=None):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild

# Recursion is used to search a tree since a tree can have an arbitrary amount of levels
def searchTree(searchValue, node):
    if node is None or node.value == searchValue: # Base Cases
        return node
    elif searchValue < node.value: # If search value is less than the current node, search left subtree
        return searchTree(searchValue, node.leftChild)
    else: # If search value is greater than the current node, search right subtree
        return searchTree(searchValue, node.rightChild)

def insertTree(value, node):
    if value < node.value:
        if node.leftChild is None: # If leftChild Node DNE then we insert here if value is less than this node
            node.leftChild = BinaryTreeNode(value)
        else: # Else continue with insertion process
            insertTree(value, node.leftChild)

    elif value > node.value:
        if node.rightChild is None:
            node.rightChild = BinaryTreeNode(value)
        else:
            insertTree(value, node.rightChild)
        
def delete(valueToDelete, node): # node paramater is the root of the tree
    if node is None: # Base Case, reached bottom of tree
        return None
    elif valueToDelete < node.value: # Searching the left subtree
        node.leftChild = delete(valueToDelete, node.leftChild)
        return node # return current node to be used as the new value of its parent's left or right child
    elif valueToDelete > node.value:
        node.rightChild = delete(valueToDelete, node.rightChild)
        return node
    
    elif valueToDelete == node.value: # Current node is the one we want to delete
        if node.leftChild is None: # If current node only has a right child, return this right child
            return node.rightChild
        elif node.rightChild is None:
            return node.leftChild
        
        # If current node has two children, delete current node by calling the lift function
        # Which changes the current node's value to the value of its successor node
        else:
            node.rightChild = lift(node.rightChild, node)
            return node

# Function finds the successor node; Value of nodeToDelete is given the value of the successor node
def lift(node, nodeToDelete):
    if node.leftChild: # If current node has a left child, recursively call this function to continue down the left subtree
        node.leftChild = lift(node.leftChild, nodeToDelete)
        return node
    
    # If current node has no left child, means current node of this function is the successor node
    # Make the node that we are deleting the value of the successor node
    else:
        nodeToDelete.value = node.value
        return node.rightChild
    
node1 = BinaryTreeNode(25)
node2 = BinaryTreeNode(75)
root = BinaryTreeNode(50, node1, node2)

# Inorder Traverse: Prints the Node values in Order; O(n) Efficiency
def traverse_and_print(node):
    if node is None: # Base Case that does nothing
        return 
    traverse_and_print(node.leftChild) # Heads down the left subtrees first until hits base case
    print(node.value) # Prints out the node values
    traverse_and_print(node.rightChild) # Heads down the right subtrees after until it hits base case

# Exercise 1
# 1 -> 5 (2 -> 4)(3) -> 9 (6 -> 8) -> 10

# Exercise 2
# log(1000) = 10 steps

# Exercise 3
# Function that returns the greatest value within a Binary Search Tree
def greatest_number_BSTree(node):
    if node.rightChild: # If it exists, it runs (If its not None)
        return greatest_number_BSTree(node.rightChild)
    else:
        return node.value
print(greatest_number_BSTree(root))

# Exercise 4
# Preorder Traversal, another way to traverse a tree
def traverse_and_print_PRE(node):
    if node is None:
        return 
    print(node.value)
    traverse_and_print_PRE(node.leftChild)
    traverse_and_print_PRE(node.rightChild)
# Moby, Great, Alice, Lord, Robin, Pride, Odyssey

# Exercise 5
# Postorder Traversal, another way to traverse a tree
def traverse_and_print_POST(node):
    if node is None:
        return
    traverse_and_print_POST(node.leftChild)
    traverse_and_print_POST(node.rightChild)
    print(node.value)
# Alice, Lord, Great, Pride, Odyssey, Robin, Moby

# CS Dojo Trees
# Linear Complexity O(n)
def findSum(node): # Initial node is the root
    if node is None:
        return 0
    return node.value + findSum(node.leftChild) + findSum(node.rightChild)
    # Returns the root node value + the sum of the left subtrees and right subtrees

print(findSum(root))

# Coding Interview Question
# Write function that returns number of non-empty universal value trees
# Universal Value Trees: Trees whose all values are the same
# Empty Trees Nodes are Universal Value Trees
# Can have Universal Value Trees
# Root node with empty left and right child nodes is a Universal Value Tree

uni_1 = BinaryTreeNode(2)
uni_2 = BinaryTreeNode(2)
uni_root = BinaryTreeNode(2, uni_1, uni_2)

def numUnis(node, Unis=0):
    if node is None:
        return Unis

    if node.leftChild is None and node.rightChild is None:
        Unis += 1
    elif node.value == node.leftChild.value and node.value == node.rightChild.value: # Skipped over if left and right childs are None
        Unis += 1

    return Unis + numUnis(node.leftChild) + numUnis(node.rightChild)

print(numUnis(uni_root))

# CS Dojo Solution
# Function checks if the tree is a unival tree
def is_tree_unival(root):
    if root is None:
        return True
    if root.leftChild != None and root.leftChild.value != root.value:
        return False
    if root.rightChild != None and root.rightChild.value != root.value:
        return False
    
    # If haven't returned yet, all the values are the same
    # Need to check the subtrees are unival trees as well
    if is_tree_unival(root.leftChild) and is_tree_unival(root.rightChild):
        return True
    
    return False # Not all values are the same so not unival

# Returns the number of non-empty sub univals of the tree
def count_univals(root):
    if root is None:
        return 0
    total_count = count_univals(root.leftChild) + count_univals(root.rightChild)
    if is_tree_unival(root):
        total_count += 1
    return total_count

print(count_univals(uni_root))
# Complexity of count_univals
# T(n) = O(n) + O(n-1) + ... + O(n) = O((n^2)/2) = O(n^2)

# Efficient counting univals

def count_univals_efficient(root):
    total_count, is_unival = helper(root) # Unpacks the values that are returned from the helper function
    return total_count

# Helper function that returns a number that are non-empty unival subtrees and a bool value
# Returns a tuple (#, Boolean)
def helper(root):
    if root is None:
        return (0, True)
    
    left_count, is_left_unival = helper(root.leftChild) # Checking if the left subtree is a unival
    right_count, is_right_unival = helper(root.rightChild) # Checking if the right subtree is a unival

    is_unival = True # Whole tree is assumed a unival

    if not is_left_unival or is_right_unival: # If Either is False means whole tree is not unival
        is_unival = False
    if root.leftChild != None and root.leftChild.value != root.value:
        is_unival = False
    if root.rightChild != None and root.rightChild.value != root.value:
        is_unival = False
    
    if is_unival:
        return (left_count + right_count + 1, True) # +1 Includes the current subtree within the recursion
    else:
        return (left_count + right_count, False)
    
print(count_univals_efficient(uni_root))