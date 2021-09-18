
# Heap implementation with arrays
class Heap:
    def __init__(self):
        self.data = [] # Heap initialized as an empty array

    def root_node(self):
        return self.data[0]
    def last_node(self):
        return self.data[-1]
    
    def left_child_index(self, index):
        return (index * 2) + 1
    
    def right_child_index(self, index):
        return (index * 2) + 2
    
    def parent_index(self, index): # Using integer division that rounds downwards
        return (index - 1) // 2

    def insert(self, value):
        self.data.append(value) # Inserting new value as the last node
        new_node_index = len(self.data) - 1 # Keep track of last node index

        # Trickle Up Algorithm
        # Checking if the new node is greater than its parent node
        while new_node_index > 0 and self.data[new_node_index] > self.data[self.parent_index(new_node_index)]:
            # Swap the nodes if true
            self.data[self.parent_index(new_node_index)], self.data[new_node_index] = self.data[new_node_index], self.data[self.parent_index(new_node_index)]
            # Update the index of the new node
            new_node_index = self.parent_index(new_node_index)
    
    def delete(self):
        # Only ever delete root node of the heap
        self.data.pop(0)
        trickle_node_index = 0 # Keeps track of the trickling node's index

        # Following loop executes the "trickle down" Algorithm
        # Loop runs as long as trickle node has a child that is greater than it
        while self.has_greater_child(trickle_node_index):
            # Saves the larger child index
            larger_child_index = self.calculate_larger_child_index(trickle_node_index)

            # Swaps the trickle node with the larger child
            self.data[trickle_node_index], self.data[larger_child_index] = self.data[larger_child_index], self.data[trickle_node_index]

            trickle_node_index = larger_child_index

    def has_greater_child(self, index):
        # Check whether the node at index has a left or right children and
        # If either of those children are greater than the node at the index
        return (self.data[self.left_child_index(index)] and self.data[self.left_child_index(index)] > self.data[index]) or (self.data[self.right_child_index(index)] and self.data[self.right_child_index(index)] > self.data[index])

    def calculate_larger_child_index(self, index):
        # If there is no right child
        if not self.data[self.right_child_index(index)]:
            return self.left_child_index(index)
        
        # If the right child value is greater than the left child
        if self.data[self.right_child_index(index)] > self.data[self.right_child_index(index)]:
            return self.right_child_index(index)
        # If the right child not greater, return the left child 
        else:
            return self.left_child_index(index)

# Exercise 1
# Last Node would be 5 <- 9 <- 10 <- 11

# Exercise 2
# Deleting Root Node
# Root Node: 9 -> 6 -> 3

# Exercise 3 (HEAPSORT)
# Deleting out all the elements of a Max-Heap into an array 
# Returns an array in descending order
# (Would be in ascending order if deleting elements of a Min-Heap)