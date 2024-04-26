# 빙산   
# bfs를 통해 풀이하였다. python으로는 통과하지 못하여 pypy로 제출했다.  

import sys
from collections import deque
n , m = map(int,sys.stdin.readline().split())
new=[]
for i in range(n):
    new.append(list(map(int,sys.stdin.readline().split())))

def bfs(new,row,col):           # 일반적으로 dfs보다 bfs가 더 빠르다고 하여 bfs로 구현하였다.  
    global visited          # 방문한 빙산을 체크하여 빙산이 다 녹아 0 이 되더라도 그 값이 다른 빙산이 녹는데 영향을 주지 않도록 하였다.  
    que = deque()
    visited = [[False]*m for i in range(n)]
    up = [1,-1,0,0]
    down = [0,0,1,-1]
    que.append((row,col))
    visited[row][col] = True
    while que:
        rerow, recol = que.popleft()        
        count = 0 
        for i in range(4):
            x = rerow+up[i]
            y = recol+down[i]
            if 0 <= x < n and 0 <= y < m:
                if not visited[x][y] and new[x][y] ==0:
                    count +=1       # 빙하를 둘러싼 바다 체크하여 count +1
                else:
                    if not visited[x][y]:
                        que.append((x,y))           # 방문하지 않은 곳 bfs로 탐색하기위해 que에 넣기
                        visited[x][y] = True        # bfs는 que에 append할 때 visited 체크(dfs는 pop할때 체크하자)
        new[rerow][recol] = max(0,new[rerow][recol]-count)          # max 값을 통해 0이하로 값이 작아지지 않도록 하자   
year = 0
while True:
    cnt=0
    visited = [[False]*m for i in range(n)]     
    for i in range(1,n):
        for j in range(1,m):
            if not visited[i][j] and new[i][j] !=0:          # visited는 bfs에서 전역변수를 체크해주었기 때문에 여기도 반영이 될 수 있다. 
                bfs(new,i,j)                    
                cnt+=1
    if cnt == 0:            # cnt가 그대로 0일 경우는 빙산이 없을 경우
        year =0 
        break 
    if cnt>=2:      # cnt가 2이상이라는 것은 빙하가 둘러 나누어져 있다는것이므로 break 이후 바로 년도를 출력   
        break
    year+=1
print(year)