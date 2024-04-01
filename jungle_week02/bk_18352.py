#특정 거리의 도시 찾기  
# 다익스트라 알고리즘 사용하여 구현  

import sys
import heapq

inf = float('inf')
n, m , k, x = map(int,sys.stdin.readline().split())
graph = [[]for i in range(n+1)]

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append((1,b))      # 가중치와 노드 값을 쌍으로 묶어서 graph에 넣는다.

distance = [inf]*(n+1)      # 최대값을 거리로 값으로 넣은 리스트를 만듬  
def dijkstra(start):
    que = [(0,start)]       # 기준으로 잡은 노드를 que에 넣는데 이때 가중치 값은 0이다. 
    distance[start] = 0     # 자기자신으로의 거리도 0  
    while que:
        dist, node =heapq.heappop(que)      # 우선순위 큐를 사용해서 큐에 들어가있는 거리중에 가장 작은값부터 pop
        if dist > distance[node]:       # 현재 노드의 거리가 이미 기존에 구한 거리 보다 크면 이미 최단 경로를 구한것으르 가정하고 넘어감  
            continue
        for redist, renode in graph[node]:
            if distance[node] + redist < distance[renode]:          # ex) node가 2일때  distance[node] = 1 (1에서 바로 2로 가는 비용) + redist = 1(2에서 3으로 가는 비용)
                                                                    # < distance[renode] => 1에서 3으로 바로 가는 비용 
                distance[renode] = distance[node] + redist          # distance의 값을 없데이트 
                heapq.heappush(que,(distance[renode],renode))       # 수정된 가중치 값과 노드값을 우선순위 큐에 push
    return distance
count = 1
answer = 0
for i in dijkstra(x)[1:]:
    if i == k:
        print(count)
        answer+=1
    count+=1
if answer ==0:
    print(-1)
    