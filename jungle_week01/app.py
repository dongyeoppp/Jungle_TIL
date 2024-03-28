
# import sys

# v,e = map(int,sys.stdin.readline().split())

# indegree = [0] * (v+1)      # 모든 노드의 진입 차수 0으로 초기화  
# graph = []
# for i in range(e):
#     graph.append(list(map(int,sys.stdin.readline().split())))
#     indegree[graph[i][1]] += 1
 
# def topology_sort():
#     result = []
#     queue = []
    
#     for i in range(1,v+1):
#         if indegree[i] == 0:
#             queue.append(i)
    
#     while queue:
#         now = queue.pop(0)
#         result.append(now)
#         for i in graph:
#             if i[0] == now:
#                 indegree[i[1]] -= 1
#             if indegree[i[1]] == 0:
#                 queue.append(i[1])

#     for i in result:
#         print(i,end=" ")
# topology_sort()

            




## 위상정렬 


import sys

v, e = map(int, sys.stdin.readline().split())

indegree = [0] * (v + 1)  # 모든 노드의 진입 차수 0으로 초기화  
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1
print(graph)
# def topology_sort():
#     result = []
#     queue = []

#     for i in range(1, v + 1):
#         if indegree[i] == 0:
#             queue.append(i)

#     while queue:
#         now = queue.pop(0)
#         result.append(now)
#         for next_node in graph[now]:
#             indegree[next_node] -= 1
#             if indegree[next_node] == 0:
#                 queue.append(next_node)

#     for node in result:
#         print(node, end=" ")

# topology_sort()
