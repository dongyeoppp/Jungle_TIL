# 불   
# bfs를 사용하여 풀이하였다. 불이 있는 위치를 먼저 que에 넣어주고, 상근이의 위치를 넣어주었다. 방문 위치를 체크하며 상근이가 지도 밖으로 나갔을 때 return 처리하였다.
import sys
from collections import deque
n = int(sys.stdin.readline())

def bfs(new,low,col,visited,w,h,fire):
    que=deque()
    count = 0
    for i in fire:
        que.append((i[0],i[1],count,False))     # 불의 좌표를 먼저 que에 넣어준다.(false는 불과 상근이를 구분하기 위해 넣었다. false는 불을 의미한다.)
        visited[i[0]][i[1]] = True
    que.append((low,col,count,True))            # 상근이의 좌표 넣기(true는 상근이를 의미)
    visited[low][col] = True
    up = [1,-1,0,0]
    down = [0,0,1,-1]
    while que:
        relow, recol, recount, is_danger = que.popleft()
        for i in  range(4):
            new_count = recount
            x = relow + up[i]
            y = recol + down[i]
            new_count+=1
            if  x >= h or y >=w or x <0 or y < 0 :      # 해당 좌표가 지도를 벗어났을 경우
                if is_danger:       # 해당 좌표의 is_danger의 값이 true일 경우 (상근이가 지도가 밖으로 벗어날 경우) return 
                    return new_count
            elif not visited[x][y] and new[x][y] == '.':        # '.'이 있는 곳으로만 이동 (불이든 상근이이든)
                que.append((x,y,new_count,is_danger))
                visited[x][y] = True
            
for i in range(n):
    w,h = map(int,sys.stdin.readline().split())
    new = []        # 빌딩의 지도 
    for j in range(h):
        new.append(list(sys.stdin.readline().strip()))
    visited = [[False]*w for i in range(h)]
    fire= []        # 불의 좌표 리스트
    for j in range(h):
        for k in range(w):
            if new[j][k] == "@":        # 상근이의 위치 찾기 
                low = j
                col = k
            elif new[j][k] == "*":      # 불의 위치 찾아서 리스트에 넣기  
                fire.append((j,k))
    result = bfs(new,low,col,visited,w,h,fire)      # new : 지도, low: 상근이가 위치하는 행, col: 상근이가 위치하는 열, visited : 방문여부체크, w,h: 지도의 행과 열, fire: 불의 위치 리스트 
    if result == None:
        print("IMPOSSIBLE")     # return 값이 없을 경우 
    else:
        print(result)