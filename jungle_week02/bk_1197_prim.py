# prim 알고리즘 사용하기  
# heap을 사용하여 최소 힙을 사용하여 구현  
import sys
import heapq

v,e = map(int,sys.stdin.readline().split())

graph = [[] for i in range(v+1)]        # kruskal 알고리즘과 다르게 연결리스트 형태로 graph를 만들었다.  

for i in range(e):
    a,b,cost = map(int,sys.stdin.readline().split())
    graph[a].append((cost,b))
    graph[b].append((cost,a))       # 무방향 그래프이므로 값을 바꿔서 또 한번 넣어준다.  

def prim(graph):        # prim 함수의 변수로 그래프를 주었다.  
    n = len(graph)
    visited = [False] * n   # 방문한 노드를 체클할 수 있는 리스트를 만들어줬다.  
    heap = []   # heap을 통해서 갈 수 있는 노드 중 최소값을 선택해 이동할 수 있도록 한다. (최소 힙)
    result= 0   

    start = 1       # 시작 노드는 1로 설정하였다.  
    visited[start] = True
    for i in graph[start]:
        heapq.heappush(heap,i)      # heqp에 push
    while heap:     # heap이 빌때까지 while문 반복   
        cost, next =heapq.heappop(heap)     # 최소값부터 heap에서 pop한다.  
        if not visited[next]:           # 가지 않은 노드일 경우에만 cost비용을 result에 더해준다. 한번 방문한 노드일 경우 heap에서 pop만 실행된다.  
            visited[next] = True        # 방문한 노드 체크  
            result+=cost        # cost 더하기  
            for i in graph[next]:       # 다음 노드로 들어가는 edge 정보를 다시 heap에 push해준다.  
                heapq.heappush(heap,i)
    return result
total_result = prim(graph)
print(total_result)






