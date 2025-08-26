from queue import Queue

def bfs_recursive(graph, que, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []
    
    if que.empty():
        return result
    
    node = que.get()
    if node not in visited:
        visited.add(node)
        result.append(node)
        print('Visited nodes:', visited)
        for neighbor in graph[node]:
            if neighbor not in visited:
                que.put(neighbor)
    
    return bfs_recursive(graph, que, visited, result)

# Graph and execution
graph = {
    'A': ['B', 'C', 'F'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'F'],
    'D': ['B'],
    'F': ['A', 'C']
}

que = Queue()
que.put('A')
print("BFS Recursive traversal:", bfs_recursive(graph, que))