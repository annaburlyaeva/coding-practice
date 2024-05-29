# BFS

from collections import deque


def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Initialize the queue with the start node

    while queue:
        vertex = queue.popleft()  # Dequeue a vertex from the queue
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)  # Process the node

            # Enqueue all adjacent nodes that haven't been visited
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited


# Example
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')
