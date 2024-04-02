# 빙산

import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
graph = []
for i in range(n):
    new = list(map(int,sys.stdin.readline().split()))
    graph.append(new)
ice = [[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
            ice[i][j] = graph[i][j]

def bfs(low,col):
    que = deque()
    que.append((low,col))
    while que:
        relow, recol = que.popleft()
        visited[relow][recol] = True
        count = 0
        if graph[relow+1][recol] == 0:
            count +=1
        if graph[relow][recol+1] == 0:
            count +=1
        if graph[relow-1][recol] == 0:
            count +=1
        if graph[relow][recol-1] == 0:
            count +=1
        ice[relow][recol] = max(0,graph[relow][recol]-count)
        
        if not visited[relow+1][recol] and graph[relow+1][recol] > 0 and (relow+1,recol) not in que:
            que.append((relow+1,recol))
        if not visited[relow][recol+1] and graph[relow][recol+1] > 0 and (relow,recol+1) not in que:
            que.append((relow,recol+1))
        if not visited[relow-1][recol] and graph[relow-1][recol] > 0 and (relow-1,recol) not in que:
            que.append((relow-1,recol))
        if not visited[relow][recol-1] and graph[relow][recol-1] > 0 and (relow,recol-1) not in que:
            que.append((relow,recol-1))

time = 0
while cc!=2:
    cc = 0
    visited = [[False]*m for i in range(n)]
    for i in range(1,n):
        for j in range(1,m):
            if graph[i][j] != 0 and not visited[i][j]:
                bfs(i,j)
                print("hi")
    for i in range(1,n):
        for j in range(1,m):
            graph[i][j]=ice[i][j]

    time+=1
   
    
print(time)
                


                
    
        









    


