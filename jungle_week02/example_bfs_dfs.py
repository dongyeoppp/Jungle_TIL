# bfs dfs 예제  
graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}
from collections import deque
def BFS(graph,start):
    visited = []
    que = deque()
    que.append(start)
    while que:
        removed = que.popleft()
        visited.append(removed)
        for i in graph[removed]:
            if i not in visited:
                que.append(i)

    return visited
def DFS(graph,start):
        visited = []
        stack = []
        stack.append(start)
        while stack:
            removed = stack.pop()
            visited.append(removed)
            for i in graph[removed]:
                if i not in visited:
                    stack.append(i)
        return visited


print(BFS(graph,'G'))
print(DFS(graph,'G'))

# ['G', 'D', 'C', 'E', 'B', 'F', 'A', 'H', 'I', 'J', 'M', 'K', 'L']
# ['G', 'D', 'E', 'F', 'C', 'B', 'H', 'M', 'J', 'K', 'L', 'I', 'A']