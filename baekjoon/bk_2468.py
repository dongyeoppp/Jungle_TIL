# 안전 영역
# bfs를 사용하여 풀이

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

# answer = 가장 높은 높이
# 이중리스트에서 가장 큰 값 찾기 
answer = max(map(max,graph))
count = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(row,col,count):
    que = deque()
    que.append((row,col))
    visited[row][col] = True
    while que:
        rerow, recol = que.popleft()
        for i in range(4):
            x = dx[i] + rerow
            y = dy[i] + recol
            # count 값 보다 높은 지역 + 방문하지 않은 지역 큐에 넣기 
            if 0<= x < n and 0<= y < n and graph[x][y] > count and not visited[x][y]:
                que.append((x,y))
                visited[x][y] = True
    return 
result = 1  
while count < answer:
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            # count값 보다 높은 높이만 확인하여 안전영역 체크 
            if graph[i][j] > count and not visited[i][j]:
                bfs(i,j,count)
                cnt +=1
    # 안전한 영역의 최대값 체크   
    result = max(result,cnt)
    count += 1
print(result)