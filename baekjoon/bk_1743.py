# 음식물 피하기

import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int,input().split())

new = [[0]*(m+1) for i in range(n+1)]
# 음식물이 놓인 자리는 1로 표시하여 체크 
for i in range(k):
    r, c = map(int,input().split())
    new[r][c] = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = [[False]*(m+1) for i in range(n+1)]

def bfs(row,col):
    que = deque()
    que.append((row,col))
    visited[row][col] = True
    count = 1
    while que:
        rerow, recol = que.popleft()
        for i in range(4):
            x = rerow + dx[i]
            y = recol + dy[i]
            # 주변에 음식물이 있는지 확인하여 음식물의 크기가 커질 수 있는지 체크 
            if 0 <= x <= n and 0 <= y <= m and new[x][y] == 1 and not visited[x][y]:
                que.append((x,y))
                visited[x][y] = True
                # 큐에 값을 넣을 때마다 체크하여 음식물의 크기 확인 
                count+=1
    return count

result = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if new[i][j] == 1:
            # 가장 큰 음식물 result 값에 담기 
            result = max(bfs(i,j),result) 
print(result)