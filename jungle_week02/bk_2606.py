# 바이러스  

# 인접 리스트를 구현하고 bfs알고리즘을 사용하였다.  인접행렬을 이용한 방법도 고려해볼 수 있다.  
import sys
from collections import deque       # bfs알고리즘에서 deque 라이브러리를 불러와 queue를 사용하였다.  
v = int(sys.stdin.readline())
e = int(sys.stdin.readline())

graph = [[]for i in range(v+1)]
for i in range(e):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph,start,visited = []):
    que = deque()
    visited = []  # 방문 노드 체크, que에 노드가 들어갈때 visited 리스트에 넣어주어 중복을 예방한다.  
    que.append(start)
    visited.append(start)

    while que:
        removed = que.popleft()
        for i in graph[removed]:
            if i not in visited:
                que.append(i)
                visited.append(i)
    return visited

print(len(bfs(graph,1))-1)

        
            
    



