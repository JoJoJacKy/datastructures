from typing import Counter
import random
from Chapter9StacksQueues import Queue
# Barebone Graph Implementation
# Can use OOP or Hash Table to represent a simple graph
friends = {
    "Alice":["Bob", "Diana", "Fred"],
    "Bob":["Alice", "Cynthia", "Diana"],
    "Cynthia":["Bob"],
    "Diana":["Alice", "Bob", "Fred"],
    "Elise":["Fred"],
    "Fred":["Alice", "Diana", "Elise"]
}
# This basic "Graph" has O(1) Linear Complexity Look Up Speed

# Directed Graph Implementation
# Using Arrays to represent those these people are being followed by
followees = {
    "Alice":["Bob", "Cynthia"],
    "Bob":["Cynthia"],
    "Cynthia":["Bob"]
}

# OOP Implementation of a Graph
# Uses an adjacency list implementation for keeping track of adjacent vertices
# Could use an adjacency matrix, useful for specific situations
class Vertex:

    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []
    
    def add_adjacent_vertex(self, vertex):
        if (vertex in self.adjacent_vertices): # If already friends, just returns doing nothing
            return
        self.adjacent_vertices.append(vertex) # Adds each other vertices to the friends list
        vertex.add_adjacent_vertex(self) # Adds each other vertices to the friends list

    def __str__(self):
        adjacentNames = ""
        for i in self.adjacent_vertices:
            adjacentNames += i.value + ", "
        return self.value + ": " + adjacentNames

# Depth First Search; Just traversing through the graph
def dfs_traverse(vertex, visited_vertices={}):
    visited_vertices[vertex.value] = True # Adds the current vertex to the visited hash table
    print(vertex.value) # Prints out the vertex value

    for neighborVertex in vertex.adjacent_vertices:
        if visited_vertices.get(neighborVertex.value, False): # Ignores the already visited Vertex
            return
        dfs_traverse(neighborVertex, visited_vertices) # Recursively Searches the Neighbor Vertex

# Depth First Search; Actually looking for something
def dfs(vertex, search_value, visited_vertices={}):
    if vertex.value == search_value: # Returns the vertex once we found what we were looking for
        return vertex

    visited_vertices[vertex.value] = True # Marks current vertex as visited

    for neighborVertex in vertex.adjacent_vertices:
        if visited_vertices.get(neighborVertex.value, False): # Skips over visited Vertices
            return

        if neighborVertex.value == search_value: # If a neighboring vertex is what we're looking for, return the neighbor vertex
            return neighborVertex
        
        vertex_searching_for = dfs(neighborVertex, search_value, visited_vertices)

        # If vertex we want is found, it would not return as None
        if vertex_searching_for: # Runs if its anything. Doesn't run if its None
            return vertex_searching_for
    
    return None


# In a social network example, each vertex represents a person
# Building a Directed Graph Example
alice = Vertex("alice")
bob = Vertex("bob")
cynthia = Vertex("cynthia")

dfs1 = Vertex("dfs1")
dfs2 = Vertex("dfs2")

alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(cynthia)
alice.add_adjacent_vertex(dfs1)
alice.add_adjacent_vertex(dfs2)
bob.add_adjacent_vertex(cynthia)

print(alice)
print(bob)
print(cynthia)

dfs_traverse(alice)
print("==================")
print(dfs(alice, "dfs1")) # Returns the dfs1 node, and shows that it is only adjacent to alice

# Breadth-First Search
def bfs_traverse(starting_vertex):
    queue = Queue()
    
    visited_vertices = {}
    visited_vertices[starting_vertex.value] = True # Marks starting_vertex as visited
    queue.enqueue(starting_vertex) # Adds the starting_vertex into the queue

    while queue.read(): # This runs while queue.read() is not None
        current_vertex = queue.dequeue() # This pops the first element and returns it from the queue
        print(current_vertex.value)

        # Iterate over the adjacent vertices of the current vertex
        for neighborVertex in current_vertex.adjacent_vertices:
            if not visited_vertices.get(neighborVertex, False): # If the neighboring vertex NOT YET visited
                visited_vertices[neighborVertex] = True # Mark vertex as visited
                queue.enqueue(neighborVertex) # Adds the neighbor vertex into the queue
print("////////////////////////")
bfs_traverse(alice)

# BFS Search
def bfs_search(starting_vertex, search_value):
    queue = Queue()
    
    visited_vertices = {}
    visited_vertices[starting_vertex.value] = True # Marks starting_vertex as visited
    queue.enqueue(starting_vertex) # Adds the starting_vertex into the queue

    while queue.read(): # This runs while queue.read() is not None
        current_vertex = queue.dequeue() # This pops the first element and returns it from the queue
        if current_vertex == search_value:
            return search_value

        # Iterate over the adjacent vertices of the current vertex
        for neighborVertex in current_vertex.adjacent_vertices:
            if not visited_vertices.get(neighborVertex, False): # If the neighboring vertex NOT YET visited
                visited_vertices[neighborVertex] = True # Mark vertex as visited
                queue.enqueue(neighborVertex) # Adds the neighbor vertex into the queue

    return None
print(bfs_search(alice, dfs2))

# Weighted Graphs
# Using a Hash Table to represent Adjacent Vertices over an Array
class WeightedGraphVertex:

    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = {} # Hash Table; Used to also house the weight of the edge

    def add_adjacent_vertices(self, vertex, weight): # When adding an adjacent vertex, also add the weight of the edge between the vertices
        self.adjacent_vertices[vertex] = weight # Vertex is Key and Weight is Value
    
dallas = WeightedGraphVertex("Dallas")
toronto = WeightedGraphVertex("Toronto")

dallas.add_adjacent_vertices(toronto, 138) # Dallas -> Toronto (138$)
toronto.add_adjacent_vertices(dallas, 216) # Toronto -> Dallas (216$)



# Weighted Vertex Graph
# But in terms of Cities and Flight Prices
class City:

    def __init__(self, name):
        self.name = name # Name of Vertex
        self.routes = {} # Adjacent Vertices
    
    def add_route(self, city, price): # Adding the Adjacent Vertices
        self.routes[city] = price # Adding the Weights of the Edges
    
# The Weighted Directed Graph Of Cities
atlanta = City("Atlanta")
boston = City("Boston")
chicago = City("Chicago")
denver = City("Denver")
el_paso = City("El Paso")

atlanta.add_route(boston, 100)
atlanta.add_route(denver, 160)
boston.add_route(chicago, 120)
boston.add_route(denver, 180)
chicago.add_route(el_paso, 80)
denver.add_route(chicago, 40)
denver.add_route(el_paso, 140)

# Dijkstra's Algorithm
def dijkstra_shortest_path(starting_city, final_destination):
    cheapest_prices_table = {}
    cheapest_previous_stopover_city_table = {}

    # For Simplicity, using an array to keep track of the known cities that HAVE NOT been visited yet
    unvisited_cities = []

    # Add city's name as first key inside the cheapest_prices_table
    # Using a hash table since we have look ups
    visited_cities = {} # Key are visited cities, with value the price to get there from starting city (Shortest)

    # If value of 0, since it costs nothing to get there 
    cheapest_prices_table[starting_city.name] = 0 # Adding the Starting City to the table

    current_city = starting_city

    while current_city:
        # Add current_city to visited cities hash
        # Remove current_city from list of unvisited cities
        visited_cities[current_city.name] = True
        if current_city in unvisited_cities:
            unvisited_cities.remove(current_city)

        # Iterate over each of the current_city's adjacent cities
        for adjacentCity, price in current_city.routes.items(): # Since routes is a hash table (Key-Value Pair)
            if not visited_cities.get(adjacentCity.name, False): # If discovered new city and unvisited, add to the unvisited array
                unvisited_cities.append(adjacentCity)
            
            # Calculate price from starting city to adjacent city using the current city as the 2nd-to-last stop
            price_through_current_city = cheapest_prices_table[current_city.name] + price

            # Check if price from starting city to adjacent city is cheapest one found so far
            if not cheapest_prices_table.get(adjacentCity.name, None) or price_through_current_city < cheapest_prices_table.get(adjacentCity.name):
                # Update the two tables
                cheapest_prices_table[adjacentCity.name] = price_through_current_city
                cheapest_previous_stopover_city_table[adjacentCity.name] = current_city.name
        
        # Visit the next unvisited city
        # Selecting which adjacent city is the cheapest to go to
        if unvisited_cities:
            minCity = unvisited_cities[0]
            minPrice = cheapest_prices_table[minCity.name]
            for unvisitedCity in unvisited_cities:
                if cheapest_prices_table[unvisitedCity.name] < minPrice:
                    minCity = unvisitedCity
                    minPrice = cheapest_prices_table[minCity.name]
            current_city = minCity
        else:
            current_city = None
    
    shortest_path = [] # Using a simple array to build the shortest path
    # Need to work backwards from the final destination
    current_city_name = final_destination.name # Input Parameter

    while current_city_name != starting_city.name: # Works backwards to the starting city
        shortest_path.append(current_city_name)
        current_city_name = cheapest_previous_stopover_city_table[current_city_name]
    
    shortest_path.append(starting_city.name) # Add the starting city at the end
    shortest_path.reverse() # We reverse the list then return
    return shortest_path


print(dijkstra_shortest_path(atlanta, el_paso))


# Exercise 1
# Nail Polish, Hammer, Pins, Needles

# Exercise 2
# A B E J F O C G K D H L M I N P

# Exercise 3
#               P
# A  B C D E F G H I J K L M O P

# Exercise 4
# Completed bfs_search()

# Exercise 5
# Shortest Path Within An Unweighted Graph
# Shortest Path is the least number of nodes to get another specified node
# Focuses around BFS since the closer vertices would be the shortest path to the ending vertex
def shortest_path_unweighted_graph(first_vertex, second_vertex, visited_vertices={}):
    queue = Queue()

    previous_vertex_table = {} # Keeps track of the immediate preceding vertex
    visited_vertices[first_vertex.value] = True
    queue.enqueue(first_vertex)

    while queue.read():
        current_vertex = queue.dequeue()
        for adjacentVertex in current_vertex.adjacent_vertices:
            if not visited_vertices.get(adjacentVertex.value, False):
                visited_vertices[adjacentVertex.value] = True
                queue.enqueue(adjacentVertex)

            # Store in previous vertex table the adjacent vertex as the key and the current_vertex as teh value
            # Indicates that the current vertex is the immediate preceding vertex that leads to the adjacent vertex
            previous_vertex_table[adjacentVertex.value] = current_vertex.value
    
    shortest_path = []
    current_vertex_value = second_vertex.value

    while current_vertex_value != first_vertex.value:
        shortest_path.append(current_vertex_value)
        current_vertex_value = previous_vertex_table[current_vertex_value]
    shortest_path.append[first_vertex.value]
    shortest_path.reverse()
    return shortest_path

# William Fiset Dijsktra's Algorithm
