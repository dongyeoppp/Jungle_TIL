# 말이 되고픈 원숭이

# bfs를 사용하여 해결 
# 벽 부수기 예제와 비슷한 문제이지만, 벽을 1번 이상 부술 수 있다는 점이 달랐다. 

import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
w, h = map(int,input().split())

graph = []
for i in range(h):
    new = list(map(int,input().split()))
    graph.append(new)

# 벽을 부술 때마다 체크하기 위해서 3차원 방문 리스트를 생성
visited = [[[0]*(k+1) for _ in range(w)] for _ in range(h)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

dx1 = [-2,-2,-1,1,2,2,1,-1]
dy1 = [-1,1,2,2,1,-1,-2,-2]

def bfs():
    que = deque()
    que.append((0,0,0))
    while que:
        # cnt는 말의 이동방법으로 이동한 횟수
        row, col, cnt = que.popleft()
        if row == h-1 and col == w-1:
            return visited[row][col][cnt]
        # 인접한 네방향으로 이동
        for i in range(4):
            x = dx[i] + row
            y = dy[i] + col
            if 0<= x < h and 0<= y < w and graph[x][y] != 1 and visited[x][y][cnt] == 0:
                visited[x][y][cnt] = visited[row][col][cnt] + 1
                que.append((x,y,cnt))
        # 말의 움직임으로 이동
        for i in range(8):
            x = dx1[i] + row
            y = dy1[i] + col
            # cnt가 인덱스 범위를 벗어날 수 있으므로 범위 조건을 확인
            if 0<= x < h and 0<= y < w and graph[x][y] != 1 and cnt+1 <= k and visited[x][y][cnt+1] == 0:
                visited[x][y][cnt+1] = visited[row][col][cnt] + 1
                que.append((x,y,cnt+1))
    # 도달하지 못할 경우
    return -1
print(bfs())

