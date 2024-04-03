# 미로 만들기  
# 다익스트라를 구현하여 실행했다. 행렬의 각 위치마다 가중치 값을 넣은 이중리스트(초기 값은 0)를 만들어 사용하였다. heapq를 사용하여 최솟값이 먼저 pop될 수 있도록 하였다.  
import sys
import heapq
n = int(sys.stdin.readline().strip())
graph=[[] for i in range(n)]

for i in range(n):
    answer = sys.stdin.readline().strip()
    for j in answer:
        graph[i].append(int(j))

distance=[[0]*n for i in range(n)]          # 거리 가중치를 넣을 리스트  
up = [1,-1,0,0]
down = [0,0,1,-1]
visited = [[False]*n for i in range(n)]     # 방문 체크 리스트  

def dijkstra(row, col):
    global distance
    que = [(distance[row][col],row,col)]    # 가중치를 먼저 넣어서 가중치값에 따라 pop될 수 있도록 한다.
    visited[row][col] = True
    while que:
        dist, rerow, recol = heapq.heappop(que)
        if rerow == n-1 and recol == n-1:
            return distance[rerow][recol]           # 도착점에 도착할 경우 도착점의 가중치 값 return 
        for i in range(4):
            x = rerow+up[i]
            y = recol+down[i]
            if 0 <= x < n and 0 <= y < n:           # 해당 인덱스에서 동서남북 비교  
                if not visited[x][y] and graph[x][y] == 1 and (distance[x][y],x,y) not in que:          # 방문하지 않고, 흰방일 경우 + que에 들어있지 않은 값일때   
                    distance[x][y]= dist                          # distance[rerow][recol] 값을 이동한 위치에도 똑같이 넣어준다.   
                    heapq.heappush(que,(distance[x][y],x,y))        
                    visited[x][y] = True
                if not visited[x][y] and (distance[x][y],x,y) not in que and graph[x][y] == 0:      # 이 경우는 검은방일 경우  
                    distance[x][y] = dist+1                       # 검은 방을 만났을 경우 가중치 값에 +1을 하여 distance 리스트를 업로드해준다. 
                    heapq.heappush(que,(distance[x][y],x,y))  
                    visited[x][y] = True
print(dijkstra(0,0))


    





