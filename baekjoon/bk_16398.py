# # 행성 연결
# # prim 알고리즘으로 풀이 
# import sys
# import heapq
# input = sys.stdin.readline

# n = int(input())
# new = []
# for i in range(n):
#     new.append(list(map(int,input().split())))
# graph = [[]for i in range(n)]
# # 양방향 그래프 만듬. (간선비용과 노드)를 해당 노드 인덱스에 추가 
# for i in range(n):
#     for j in range(i+1,n):
#         if new[i][j] != 0:
#             graph[i].append((new[i][j],j))
#             graph[j].append((new[i][j],i))
# # 최소 스패닝 트리 : 주어진 그래프의 모든 정점을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리
# def prim(graph):
#     heap = []
#     result = 0
#     visited = [False] * n
#     start = 0
#     visited[start] = True
#     for i in graph[start]:
#         heapq.heappush(heap,i)
#     while heap:
#         cost, node = heapq.heappop(heap)
#         # 방문하지 않은 노드일 경우에만 cost를 result에 더해준다. 
#         if not visited[node]:
#             visited[node] = True
#             result += cost
#             for i in graph[node]:
#                 if not visited[i[1]]:
#                     heapq.heappush(heap,i)
#     return result

# print(prim(graph))

# kruskal 알고리즘 풀이

import sys
input = sys.stdin.readline

n = int(input())
new = []
for i in range(n):
    new.append(list(map(int,input().split())))
graph = []
# (간선의 비용, start노드, end 노드)를 graph에 담고 간선의 비용 순서로 오름차순 정렬 
for i in range(n):
    for j in range(i+1,n):
        graph.append((new[i][j],i,j))
graph.sort()
parent = [i for i in range(n)]
def find(parent,x):
    if parent[x] == x:
        return x
    parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    root1 = find(parent,a)
    root2 = find(parent,b)
    if root1 > root2:
        parent[root1] = root2
    else:
        parent[root2] = root1
result = 0
count = 0
for i in graph:
    # 부모노드가 같을 경우 사이클이 생김으로 부모노드가 다를 경우에만 최소비용간선으로 추가 
    if find(parent,i[1]) != find(parent,i[2]):
        union(parent,i[1],i[2])
        result += i[0]
        count += 1
    # 최소 간선의 개수는 (노드의 개수 -1) 임으로 최소 간선을 모두 찾았다면 반복문 종료 
    if count == n-1:
        break
print(result)