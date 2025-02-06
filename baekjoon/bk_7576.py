# 토마토

import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int,input().split())

tomato = []
for i in range(n):
    tomato.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(answer):
    que = deque()
    # 익은 토마토를 전부 que에 먼저 넣기 
    for i in answer:
        que.append((i[0],i[1]))
    while que:
        rerow, recol = que.popleft()
        for i in range(4):
            x = rerow + dx[i]
            y = recol + dy[i]
            if 0<= x< n and 0<=y<m and tomato[x][y] == 0:
                que.append((x,y))
                # 며칠이 지나는지 체크하기 위해 1씩 더함 
                tomato[x][y] = tomato[rerow][recol] + 1
                
    return 
# 익은 토마토의 위치를 answer리스트에 담음 
answer = []
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            answer.append((i,j))
bfs(answer)
check = False
# 안 익은 토마토가 있는지 확인 
for i in tomato:
    if 0 in i:
        check = True
        break
if check:
    print(-1)
else:
    # 모든 토마토가 다 익는데 최소 며칠이 걸리는지 확인 (이중 리스트에서 최대값 구하기)  
    print(max(map(max,tomato))-1)