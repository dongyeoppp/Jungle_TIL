# 다리 만들기
# bfs를 두 개 만들어 풀이 함
import sys
from collections import deque 
input = sys.stdin.readline

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 각각의 섬을 체크하기 위한 bfs
# 같은 섬을 나타내는 부분의 grpah 값을 1이 아닌 다른 값으로 수정
def bfs(row,col,ans):
    que = deque()
    que.append((row,col))
    graph[row][col] = ans
    while que:
        rerow, recol = que.popleft()
        for i in range(4):
            x = dx[i] + rerow
            y = dy[i] + recol
            if 0<= x < n and 0<= y < n and graph[x][y] == 1:
                que.append((x,y))
                graph[x][y] = ans
    return 

# 같은 섬 체크 
answer = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j,answer)
            answer += 1 

# 최단 거리 체크를 위한 bfs
def new_bfs(row,col,num):
    que = deque()
    que.append((row,col))
    visited[row][col] = 1
    while que:
        rerow, recol = que.popleft()
        for i in range(4):
            x = dx[i] + rerow
            y = dy[i] + recol
            if 0<= x < n and 0<= y < n and visited[x][y] == 0:
                # 육지가 아닌 곳에 visited의 값을 수정해 가며 거리 업데이트 
                if graph[x][y] == 0:
                    que.append((x,y))
                    visited[x][y] = visited[rerow][recol] + 1
                # 다른 육지에 도착!
                elif graph[x][y] != num:
                    return visited[rerow][recol]
    # 다른 육지에 도달하지 못 했을 경우 최대값 return 
    return float('inf')

result = float('inf')
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            visited = [[0] * n for i in range(n)]
            ans = new_bfs(i,j,graph[i][j])
            # 최단거리 체크 
            result = min(result,ans)
print(result-1)