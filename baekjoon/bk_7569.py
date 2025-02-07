# 토마토
# bfs로 풀이. 3중 리스트 사용 
import sys
from collections import deque
input = sys.stdin.readline

m,n,h = map(int,input().split())

# 토마토들의 정보 저장 
tomato = []
for i in range(h):
    answer = []
    for j in range(n):
        answer.append(list(map(int,input().split())))
    tomato.append(answer)
# 익은 상태의 토마토가 있는 위치를 new리스트에 저장 
new = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                new.append((i,j,k))
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs(new):
    que = deque()
    # 익은 토마토들의 위치를 먼저 que에 넣음 
    for i in new:
        que.append((i[0],i[1],i[2]))
    while que:
        height, row, col = que.popleft()
        for i in range(6):
            z = height + dz[i]
            x = row + dx[i]
            y = col + dy[i]
            # 안 익은 토마토일 경우 
            if 0<=z<h and 0<=x<n and 0<=y<m and tomato[z][x][y] == 0:
                # 익을 때까지 걸리는 기간을 체크하기 위해 1씩 더함 
                tomato[z][x][y] = tomato[height][row][col] + 1
                que.append((z,x,y))
    return

bfs(new)
check = True
result = 1
for i in range(h):
    for j in range(n):
        if 0 in tomato[i][j]:
            # 토마토가 모두 익지 못하는 상황 일 경우 
            check = False
            break
    # 모든 토마토가 다 익을 때까지 걸리는 최소한의 일수를 확인 
    result = max(result,max(map(max,tomato[i])))
result = 1
if not check:
    print(-1)
else:
    print(result-1)