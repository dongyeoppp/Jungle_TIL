# 적록색약   
# bfs로 풀이하였다.
import sys
from collections import deque
n = int(sys.stdin.readline())
color = []      # 적록 색약이 적용되지 않은 그래프  
color1 = []     # 적록 색약이 적용된 그래프   
for i in range(n):
    new = sys.stdin.readline().strip()
    color.append(new)
    new1 = []
    for j in new:
        if j == "G":
            new1.append("R")
        elif j == "R":
            new1.append("R")
        else:
            new1.append("B")
    color1.append(new1)

visited1 = [[False]* n for i in range(n)]       # 적록색약을 고려하지 않은 visited
visited2 = [[False]* n for i in range(n)]       # 적록색약을 고려한 visited
def bfs(color,start1,start2,visited):
    que = deque()
    que.append((start1,start2))
    visited[start1][start2] = True
    up = [1,0,-1,0]
    down = [0,1,0,-1]
    while que:
        restart1,restart2 = que.popleft()
        for i in range(4):
            x = restart1+up[i]
            y = restart2+down[i]
            if 0 <= x < n and 0 <= y < n and not visited[x][y]:
                if color[restart1][restart2] == color[x][y]:
                    que.append((x,y))
                    visited[x][y] = True

count1 = 0
count2 = 0
for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            bfs(color,i,j,visited1)    # 적록색약을 고려하지 않은 bfs
            count1+=1
for i in range(n):
    for j in range(n):
        if not visited2[i][j]:
            bfs(color1,i,j,visited2)   # 적록색약을 고려한 bfs
            count2+=1
print(count1,count2)