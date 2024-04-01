# 최소비용 구하기
# 다익스트라 알고리즘 사용  

import sys
import heapq
n = int(sys.stdin.readline())  
m = int(sys.stdin.readline())
inf = float('inf')
graph = [[]for i in range(n+1)]
for i in range(m):
    a,b,cost = map(int,sys.stdin.readline().split())
    graph[a].append((cost,b))       # 단방향으로 그래프 구현  

distance = [inf] * (n+1)        # 거리 정보를 담을 리스트 생성  

def dijkstra(start):
    que = [(0,start)]       # 시작점을 우선순위 큐에 넣어준다. 가중치는 0
    distance[start] = 0     # 거리 정보를 담은 리스트에도 가중치 0을 넣어줌 

    while que:
        dist , node = heapq.heappop(que)        
        if dist > distance[node]:       # 거리정보를 담은 리스트에 있는 값이 현재 거리보다 작을 경우 이미 최소값이 들어가있다고 인지하고 continue
            continue
        for redist, renode in graph[node]:
            if distance[node] + redist < distance[renode]:      
                distance[renode] = distance[node] + redist
                heapq.heappush(que,(distance[renode],renode))
    return distance
first, last = map(int,sys.stdin.readline().split())
print(dijkstra(first)[last])