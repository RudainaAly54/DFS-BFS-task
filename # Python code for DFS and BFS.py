# Python code for DFS and BFS
# Using a Python dictionary to represent a graph

graph = {
    'A': ['B', 'T'],
    'B': ['H'],
    'T':['C','E'],
    'C': [],
    'E': ['G','D'],
    'F': [],
    'H':['F'],
    'D': [],
    'G':[]
}

# DFS algorithm
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()  # Initialize an empty set to keep track of visited nodes
    visited.add(node)   # Mark the current node as visited
    print(node, end=' ')  # Print the current node
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)  # Recursively visit unvisited neighbors
    return visited

# BFS algorithm
def bfs(graph, start):
    visited = set()  # Initialize an empty set to keep track of visited nodes
    queue = [start]  # Create a queue for BFS
    while queue:
        vertex = queue.pop(0)  # Dequeue the first node from the queue
        if vertex not in visited:
            visited.add(vertex)  # Mark the current node as visited
            print(vertex, end=' ')  # Print the current node
            queue.extend(set(graph[vertex]) - visited) # Enqueue unvisited neighbors

    return visited


print("DFS traversal:")
dfs_visited = dfs(graph, 'A')
print("\nBFS traversal:")
bfs_visited = bfs(graph, 'A')