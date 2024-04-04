# 경쟁적 전염  
# 최소힙을 이용하여 알고리즘을 구현하였다. 
import sys
import heapq

n, k = map(int,sys.stdin.readline().split())
graph = []
for _ in range(n):
    new = list(map(int,sys.stdin.readline().split()))
    graph.append(new)           # 행렬로 graph를 만들어 구현했다.  
s,p,q = map(int,sys.stdin.readline().split())
up = [1,-1,0,0]  
down = [0,0,1,-1]

def sort(graph):
    que = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0 and graph[i][j] != -1:          # graph의 값이 0이나 -1이 아닐 경우만 heap에 넣어준다.  
                heapq.heappush(que,(graph[i][j],i,j))           # heap에 가중치를 같이 넣어주어 가중치가 작은 값이 먼저 나올 수 있도록 했다. 
    while que:
        weight, rerow, recol = heapq.heappop(que)               
        for i in range(4):          # 해당 행렬에서 동서남북 값 비교  
            x = rerow + up[i]
            y = recol + down[i]
            if 0<=x<n and 0<=y < n:     # 행렬의 범위가 넘어가지 않을 경우만 실행  
                if graph[x][y] == 0:        # 해당 노드값이 0일 경우 이전 노드의 가중치값을 넣어준다.    
                    graph[x][y] = weight
                    if x == p-1 and y == q-1:       # 문제에서 제시한 행렬값에 0이 아닌 값이 들어갈 경우 함수를 종료한다.   
                        return 
                    graph[rerow][recol] = -1        # 이전 노드에는 -1값을 넣어주어서 que에 다시 못들어가도록 한다. 
    return
for _ in range(s):
    if graph[p-1][q-1] != 0:        # 값을 확인할 행렬값에 0이 아닌 다른 값이 들어갔을 경우 break
        break
    sort(graph)         # 이 부분에서 오류가 있어 오랬동안 문제를 해결하지 못했다.if문과 sort()을 바꿔주었더니 해결되었다.  
                        # [[0,0,0],[0,1,0],[0,0,0]] 일 경우 1을 바로 -1로 바꿔주고 가중치 값을 출력할 수 있기때문에 if문을 먼저 실행하고 sort()함수를 실행 시켜야한다!!
print(graph[p-1][q-1])          # 해당위치에 가중치값을 출력한다. 