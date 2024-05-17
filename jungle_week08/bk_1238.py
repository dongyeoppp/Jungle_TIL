# 파티   
# 다익스트라 알고리즘을 사용하여 구현했다. 다익스트라 알고리즘은 하나의 노드를 기준으로 다른 노드로 가는 최단거리를 구하는 알고리즘이다.  
import sys
import heapq
inf = float("inf")
n , m , x = map(int,sys.stdin.readline().split())  
graph1 = [[] for i in range(n+1)]
graph2 = [[] for i in range(n+1)]       # 그래프를 두 개 만듬
for i in range(m):
    start, end , w = map(int,sys.stdin.readline().split())
    graph1[start].append((w,end))       # graph1은 집으로 돌아올 때의 최단거리를 정할 때 사용한다. 
    graph2[end].append((w,start))       # graph1과 반대로 start와 end 값을 바꿔주어 각자 집에서 x로 가는 최단 경로를 사용한다. 
def dijkstra(graph,start):
    weight = [inf]*(n+1)        # 최단 거리를 저장할 최단 경로 테이블을 만든다. 
    weight[start] = 0
    que = [(0,start)]       # 특정 노드를 start로 받아서 특정 노드에서 다른 노드로 가는 경로를 모두 저장한다.  

    while que:
        distance, node = heapq.heappop(que)
        if distance > weight[node]:     # 현재 pop한 거리 값이 경로 테이블에 저장되어 있는 값보다 크면 경로 테이블을 재조정할 필요가 없다.  
            continue
        for re_distance, re_node in graph[node]:
            if weight[node] + re_distance < weight[re_node]:            # 최단 경로 비교  
                weight[re_node] = weight[node] + re_distance
                heapq.heappush(que,(weight[re_node],re_node))
    return weight

result1 = dijkstra(graph1,x)
result2 = dijkstra(graph2,x)
last_result = []
for i in range(1,n+1):
    if i != x:
        last_result.append(result1[i]+result2[i])
print(max(last_result))