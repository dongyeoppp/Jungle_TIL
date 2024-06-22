# 전쟁 - 전투   
# bfs를 사용하여 풀이하였다.  
# m이 세로 크기이고 n이 가로 크기이다. m이 low를 뜻하고 n이 col을 뜻하기 때문에 헷갈릴 수 있다. 주의하자 
import sys
from collections import deque
n ,m = map(int,sys.stdin.readline().split())
war = []
for i in range(m):
    war.append(sys.stdin.readline().strip())

visited=[[False]* n for i in range(m)]      # 방문 체크 

def bfs(low,col):           
    global n,m,visited,war
    que = deque()
    count = 0
    que.append((low,col))               
    save = war[low][col]        # 아군인지 적군인지 저장 
    visited[low][col] = True
    up = [1,-1,0,0]
    down = [0,0,1,-1]
    while que:
        relow, recol = que.popleft()
        count+=1
        for i in range(4):
            x = relow + up[i]
            y = recol + down[i]
            if 0 <= x < m and 0<= y < n and not visited[x][y] and war[x][y] == save:        # 같은 색깔인지 확인
                que.append((x,y))
                visited[x][y] = True
    return count
blue = 0
white = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j] and war[i][j] == 'B' :     # blue인 경우 
            blue += bfs(i,j)**2
        elif not visited[i][j] and war[i][j] == 'W' :   # white인 경우 
            white += bfs(i,j)**2
print(white, blue)