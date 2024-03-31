# 이분 그래프   
# 처음에 이분그래프는 사이클이 없는 그래프라고 생각하고 문제를 풀었다. 하지만 이분 그래프에도 사이클이 존재할 수 있다. 이분그래프에 대한 개념을 다시 이해하고 풀었다.  
# 그래프를 두 그룹으로 나누었을때 특정노드와 인접한 노드가 같은 그룹으로 묶이지 않는 것을 이분 그래프라고 하고 이를 이용해 문제를 풀이했다. 
# 인접한 노드끼리 서로 다른 값을 정해주었고 bfs 알고리즘을 진행하며 이 값이 같을 경우 false를 반환하도록 하였다. 
import sys
from collections import deque

k = int(sys.stdin.readline())

def bfs(start,group):       # duque를 통해 bfs 구현, 변수로 시작 노드start와 인접 노드를 구분할 group변수를 주었다.   
    que = deque()
    que.append(start)
    visited[start] = group  # que에 노드를 넣어줄 경우 해당 노드 인덱스에 해당하는  visited리스트에 group값을 넣어준다.  
    while que:
        removed = que.popleft()
        for i in graph[removed]:
            if not visited[i]:
                que.append(i)
                visited[i] = -visited[removed]      # 부모 노드에 -을 붙인 group값을 넣어주어 서로 구분될 수 있도록 한다. 
            elif visited[i] == visited[removed]:    # 만약 서로 인접한 노드의 group값이 같디면 바로 false를 반환한다.  
                return False
            
    return True     # 위 과정에서 아무 지장이 없을시 true 반환  
            
for k in range(k):
    v,e = map(int,sys.stdin.readline().split())
    graph = [[]for i in range(v+1)]
    visited = [False] *(v+1)
    for i in range(e):
        a,b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1,v+1):          # 그래프가 따로 떨어져 있을 수 있으므로 모든 노드를 시작지점으로 다 봐야한다.  
        if  not visited[i]:     # visited리스트에 값이 없을 경우에만 bfs함수를 실행한다.
            result = bfs(i,1)
            if not result:          # result 값이 false일 경우 break
                break
    if result:          # result 값이 True일 경우  
        print("YES")
    else:               # result 값이 false일 경우 
        print("NO")
        