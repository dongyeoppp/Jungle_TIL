# 빙산
# bfs를 사용해서 구현하였다. python3로 실행을 하니 시간초과가 발생하였다. pypy로 실행했더니 통과하였다.  
import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
graph = []
for i in range(n):
    new = list(map(int,sys.stdin.readline().split()))
    graph.append(new)                   # 먼저 graph에 행렬형식으로 빙산데이터를 받았다.  
ice = [[0]*m for i in range(n)]
for i in range(1,n):
    for j in range(1,m):
            ice[i][j] = graph[i][j]         # graph와 동일한 데이터를 가진 ice라는 행렬을 만들었다. bfs를 통해 빙산이 녹지 않은 곳을 돌면서 update되는 값을 graph에 반영할 것 이다. 
                                            # 빙산이 한번에 녹아야한다. 초기에 나타나는 주변 0값의 개수를 유지하기 위해 만들었다.  

def bfs(row,col):
    que = deque()
    que.append((row,col))
    while que:
        rerow, recol = que.popleft()
        visited[rerow][recol] = True
        count = 0                   # 해당 행렬값에 동서남북으로 0이 몇개있는지를 세어 count에 저장한다. 
        if graph[rerow+1][recol] == 0:
            count +=1
        if graph[rerow][recol+1] == 0:
            count +=1
        if graph[rerow-1][recol] == 0:
            count +=1
        if graph[rerow][recol-1] == 0:
            count +=1
        ice[rerow][recol] = max(0,graph[rerow][recol]-count)      # max 함수를 써서 0이하로 내려가는 값을 방지해주고 빙산이 녹은 만큼 ice행렬을 업데이트 하였다.   
        
        if not visited[rerow+1][recol] and graph[rerow+1][recol] > 0 and (rerow+1,recol) not in que:
            que.append((rerow+1,recol))                                                                # 방문하지 않고 빙산의 높이가 0이 아닌 그리고 que에 중복되어 들어가지 못하도록 설정하고 que에 넣어주었다.
        if not visited[rerow][recol+1] and graph[rerow][recol+1] > 0 and (rerow,recol+1) not in que:
            que.append((rerow,recol+1))
        if not visited[rerow-1][recol] and graph[rerow-1][recol] > 0 and (rerow-1,recol) not in que:
            que.append((rerow-1,recol))
        if not visited[rerow][recol-1] and graph[rerow][recol-1] > 0 and (rerow,recol-1) not in que:
            que.append((rerow,recol-1))

time = 0    # 년도 세기 
while True :
    visited = [[False]*m for i in range(n)]     # 한번 탐색이 끝날 때마다 visited 리스트를 초기화 해주었다. 
    recur=0             # 재귀함수가 두번 사용되는 것을 count
    for i in range(1,n):
        for j in range(1,m):
            if graph[i][j] != 0 and not visited[i][j]:
                bfs(i,j)
                recur+=1        # 현재 for문 안에서 재귀함수가 두번 사용되었다는 것은 얼음이 두덩이로 나뉘었다는 것이다.
    if recur == 0:      # 한번에 다 녹아서 분리되지 않을 경우 0을 출력  
        time= 0
        break

    if recur >=2 :      # 재귀 함수가 두번이상 실행되면 break
        break
    for i in range(1,n):
        for j in range(1,m):
            graph[i][j]=ice[i][j]       # 재귀함수가 실행된 이후 ice 행렬에서 업데이트 된 값을 graph에 넣어주었다.  
    time+=1 # while문을 돌때마다 시간 +1
print(time)


                


                
    
        









    


