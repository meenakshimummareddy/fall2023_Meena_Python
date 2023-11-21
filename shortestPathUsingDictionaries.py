# Undirected graph and finding shortest path using Dictionaries
from collections import deque

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

def shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next_vertex in graph[vertex] - set(path):
            if next_vertex == end:
                return path + [next_vertex]
            else:
                queue.append((next_vertex, path + [next_vertex]))

# Example
source = 'A'
destination = 'F'
result = shortest_path(graph, source, destination)
print("Shortest path from", source, "to", destination, ":", result)
