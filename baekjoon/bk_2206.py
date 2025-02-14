# 벽 부수고 이동하기   


import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

new = []
for i in range(n):
    new.append(input().strip())

dy = [1,-1,0,0]
dx = [0,0,1,-1]
visited = [[float('inf')]*m for _ in range(n)]

def bfs(row,col,count):
    que = deque()
    visited[row][col] = 1
    que.append((row,col,count))
    while que:
        rerow, recol, cnt = que.popleft()
        for i in range(4):
            x = dx[i] + rerow
            y = dy[i] + recol
            if 0<=x <n and 0<= y <m and visited[rerow][recol]+1 < visited[x][y]:
                if cnt == 0 or new[x][y] == "0":
                    visited[x][y] = visited[rerow][recol] + 1
                    if new[x][y] == "1":
                        cnt +=1
                    que.append((x,y,cnt))
                    
    return

bfs(0,0,0)
print(visited)
if visited[n-1][m-1] == float('inf'):   
    print(-1)
else:
    print(visited[n-1][m-1])
