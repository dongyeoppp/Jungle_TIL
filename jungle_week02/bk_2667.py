# 단지 번호 붙이기  (2주차 시험)
# bfs사용하여 구현하였다.  
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

graph = [[]for i in range(n)]
for i in range(n):
    new = input().strip()
    for j in new:
        graph[i].append(int(j))

up = [1,-1,0,0]
down = [0,0,1,-1]
visited = [[False]*n for i in range(n)]

def bfs(row,col):
    new = 0
    que = deque()
    que.append((row,col))
    while que:
        rerow, recol = que.popleft()
        new+=1                  # 1이 적힌곳이 묶여 있기 때문에 좌표를 이동할때마다 count   
        visited[rerow][recol] = True
        for i in range(4):
            x = rerow + up[i]
            y = recol + down[i]
            if 0<=x<n and 0 <= y <n:
                if not visited[x][y] and graph[x][y] ==1 and (x,y) not in que :
                    que.append((x,y))
    return new

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:      # 1이 적힌 곳에 도착했을 경우 bfs함수 실행 (방문하지 않은곳만)
            result.append(bfs(i,j))         # bfs에서 방문한 좌표 갯수를 return 하여 result 리스트에 넣었다.   
print(len(result))      # 총 단지 수  
result.sort()       # 오름차순 정렬 후 print   
for i in result:
    print(i)   