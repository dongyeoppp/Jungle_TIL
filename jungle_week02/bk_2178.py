# 미로 탐색   
# bfs를 사용하여 해결하였다.  처음 시작 점부터 bfs탐색하며 해당 지점까지 간 최소 거리를 graph에 갱신에 가며 graph[n][m]에 도달할때 최소값이 해당 행렬값으로 들어갈 수 있도록하였다. 
import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())

graph = [[]*m for i in range(n)]
for i in range(n):
    new = sys.stdin.readline().strip()
    for j in new:
        graph[i].append(int(j))                 # graph라는 행렬을 만들어주었다.  

def bfs(row,col):
    que = deque()
    que.append((row,col))
    visited = [[False]*m for i in range(n)]
    visited[row][col] = True
    while que :
        rerow, recol = que.popleft()    # 인덱스 범위를 넘어가지 않도록하고 해당인덱스에서 상하좌우를 탐색하여 이동할 수 있는 곳의 행과 열값을 stack에 넣어 주었다. (0이아니고 방문하지 않은 노드만)
        if 0 <= rerow+1 < n and 0 <= recol < m and graph[rerow+1][recol] != 0 and not visited[rerow+1][recol] :     
            que.append((rerow+1,recol))
            visited[rerow][recol] = True
            graph[rerow+1][recol] = graph[rerow][recol] +1          # 이동한 지점에 이전 지점의 graph값에 +1을 해주었다.  
        if 0 <= rerow < n and 0 <= recol+1 < m and graph[rerow][recol+1] != 0 and not visited[rerow][recol+1] :
            que.append((rerow,recol+1))
            visited[rerow][recol] = True
            graph[rerow][recol+1] = graph[rerow][recol] +1
        if 0 <= rerow-1 < n and 0 <= recol < m and graph[rerow-1][recol] != 0 and not visited[rerow-1][recol] :
           que.append((rerow-1,recol))
           visited[rerow][recol] = True
           graph[rerow-1][recol] = graph[rerow][recol] +1
        if 0 <= rerow < n and 0 <= recol-1 < m and graph[rerow][recol-1] != 0 and not visited[rerow][recol-1] :
            que.append((rerow,recol-1))
            visited[rerow][recol] = True
            graph[rerow][recol-1] = graph[rerow][recol] +1
        
bfs(0,0)
print(graph[n-1][m-1])