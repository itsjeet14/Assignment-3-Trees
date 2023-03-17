"""Implement BFS (Breath First Search) and DFS (Depth First Search)"""

# BFS and DFS using user input with data type

from queue import Queue

# BFS
def bfs(graph, start):
    visited = set()
    q = Queue()
    q.put(start)
    visited.add(start)

    while not q.empty():
        node = q.get()
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.put(neighbor)

# DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# User input for start node and traversal type
start_node = input("Enter the starting node: ")
print(f"Data type of the input node: {type(start_node)}")
traversal_type = input("Enter the traversal type (BFS or DFS): ")
print(f"Data type of the traversal type: {type(traversal_type)}")

if traversal_type == 'BFS':
    bfs(graph, start_node)
elif traversal_type == 'DFS':
    dfs(graph, start_node)
else:
    print("Invalid traversal type.")
