
# Single Linked List Implementation
# Java has linked lists built-in; Many languages do not
class Node:
    next_node = None # Serves as the link to the next node
    previous_node = None
    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data
    
    def __str__(self) -> str:
        return "Node Data: " + str(self.data)

class LinkedList: # The Linked List just keeps track of the first node

    def __init__(self, first_Node):
        self.first_node = first_Node
    
    def read(self, index): # Accessing the index of the item within the linked list
        current_node = self.first_node
        current_index = 0
        while current_index < index:
            current_node = current_node.next_node
            current_index += 1
        if current_node != None:
            return current_node # Returns the node 
        else:
            return None
    
    def index_of(self, value): # Seaching for particular value within our linked list
        current_node = self.first_node
        current_index = 0
        
        while current_node != None:
            if current_node.get_data() == value:
                return current_index
            current_node = current_node.next_node
            current_index += 1
        return None # Returns None when runs out of elements to search
    
    def insert_at_index(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next_node = self.first_node # New first node references the old first node
            self.first_node = new_node # Updates the first node property of the linked list
            return
        
        # If inserting anywhere else that is not the beginning
        current_node = self.first_node
        current_index = 0
        # Access the node the index before where we are inserting the new node
        while current_index < index - 1:
            current_node = current_node.next_node # Just updates the nodes till we get to the node right before where we want to insert the new node
            current_index += 1
        
        new_node.next_node = current_node.next_node # New node gets the reference the next node from the previous node
        current_node.next_node = new_node # Updates the reference of the previous node to the new node
    
    def delete_at_index(self, index):
        if index == 0: # Deleting the first Node
            self.first_node = self.first_node.next_node 
        
        current_node = self.first_node
        current_index = 0

        while current_index < index - 1: # Accessing the node right before where we want to delete
            current_node = current_node.next_node
            current_index += 1
        
        node_after_deleted_node = current_node.next_node.next_node
        current_node.next_node = node_after_deleted_node
    
    def displayAllItemData(self): # Prints out all the data from all the items in the linked list
        current_node = self.first_node
        while current_node != None:
            print(current_node)
            current_node = current_node.next_node
    
    def getLastItemData(self):
        current_node = self.first_node
        while current_node != None:
            last_node = current_node
            current_node = current_node.next_node
        return last_node
    
    def reverseLinkedList(self):
        current_node = self.first_node
        last_node = self.getLastItemData()
        nodes = []
        while current_node.next_node != None:
            nodes.append(current_node)
            current_node = current_node.next_node
        nodes.reverse()
        self.first_node = last_node
        self.first_node.next_node = nodes[0]
        for i in range(len(nodes)-1):
            nodes[i].next_node = nodes[i+1]
        nodes[len(nodes)-1].next_node = None

    # Reverse Linked List by keeping track of current_node, the previous and next nodes
    def reverse(self):
        previous_node = None
        current_node = self.first_node

        while current_node != None:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node
        
        self.first_node = previous_node
    
    def delete_middle_node(self, node):
        node.data = node.next_node.data
        node.next_node = node.next_node.next_node
            


nodeA = Node(100)
chainList = LinkedList(nodeA)

nodeB = Node(200)
nodeC = Node(300)
nodeD = Node(400)
nodeA.next_node = nodeB
nodeB.next_node = nodeC
nodeC.next_node = nodeD
print(chainList.read(3))
print(chainList.index_of(100))
print("-------------")
chainList.insert_at_index(1,150)
chainList.displayAllItemData()
print(chainList.getLastItemData())
print("================")
chainList.reverse()
print(chainList.displayAllItemData())
print("-------------")
# Doubly Linked List
class DoublyLinkedList:
    def __init__(self, first_node=None, last_node=None):
        self.first_node = first_node
        self.last_node = last_node
    
    def insert_at_end(self, value):
        new_node = Node(value)

        # If doubly linked list is empty
        if self.first_node == None:
            self.first_node = new_node
            self.last_node = new_node
        else: # Doubly Linked List has at least one node
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node # The Doubly Linked List last node is updated
        
    def remove_from_front(self):
        removed_node = self.first_node
        self.first_node = self.first_node.next_node
        return removed_node
    
    def displayAllDataReversed(self):
        current_node = self.last_node
        while current_node != None:
            print(current_node)
            current_node = current_node.previous_node

# Doubly Linked Lists are the perfect data structure for Queues
class Queue:

    def __init__(self):
        self.data = DoublyLinkedList()
    
    def enqueue(self, element):
        self.data.insert_at_end(element)
    
    def dequeue(self):
        removed_node = self.data.remove_from_front()
        return removed_node.data
    def read(self):
        if self.data == None:
            return None
        else:
            return self.data.first_node.get_data()

doobleList = DoublyLinkedList()
doobleList.insert_at_end(1)
doobleList.insert_at_end(2)
doobleList.insert_at_end(5)
doobleList.insert_at_end(10)
doobleList.insert_at_end(11)
doobleList.displayAllDataReversed()
