# # 트리의 부모 찾기   
# # 인접리스트에 dfs를 구현한다. 
# # dfs를 재귀함수로 구현하였다. 시간초과가 나와서 스택으로 구현해 보아야겠다.  

# 스택으로 구현 1

# import sys
# v = int(sys.stdin.readline())
# graph = [[]for i in range(v+1)]
# for i in range(v-1):
#     a,b = map(int,sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
# result = [0]*(v+1)

# def dfs(graph,start,visited=[]):
#     stack = [start]
#     while stack:
#        removed = stack.pop()
#        if removed not in visited:
#            visited.append(removed)
#            for i in graph[removed]:
#                 if i not in visited:
#                     stack.append(i)
#                     result[i] = removed
#     return visited
# dfs(graph,1)
# for i in result[2:]:
#     print(i)

# 스택으로 구현하였으나 또 시간초과가 나왔다. 코드에 문제가 있다.   
# 문제를 찾았다. 원래 visited에 인덱스 값을 그대로 넣어 start not in visited로 중복 검사를 하였는데 이게 시간 복잡도가 n으로 높게 나온게 문제였다.  
# visited리스트를 false로 초기화하고 중복이 없을 경우 True를 넣어주었다. 시간초과 문제를 해결하였다. 
#  재귀함수로 구현한 코드도 시간초과가 해결 되었다. 런타임에러가 낫지만 재귀최대값을 높게 설정해주어 해결하였다.  

# 스택으로 구현  2 
import sys
v = int(sys.stdin.readline())
graph = [[]for i in range(v+1)]
for i in range(v-1):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
result = [0]*(v+1)

def dfs(graph,start,visited=[False]*(v+1)):
    stack = [start]
    while stack:
       removed = stack.pop()
       if not visited[removed]:
           visited[removed] = True
           for i in graph[removed]:
                if not visited[i]:
                    stack.append(i)
                    result[i] = removed
dfs(graph,1)
for i in result[2:]:
    print(i)  

# dfs 재귀함수로 구현  
# import sys
# sys.setrecursionlimit(10 ** 6)
# v = int(sys.stdin.readline())
# graph = [[]for i in range(v+1)]
# for i in range(v-1):
#     a,b = map(int,sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
# result = [0]*(v+1)
# def dfs(graph,start,visited=[False]*(v+1)):
#     if not visited[start]:
#         visited[start] = True
#     for i in graph[start]:
#         if not visited[i]:
#             visited[i] = True
#             result[i]=start
#             dfs(graph,i)
# dfs(graph,1)

# for i in result[2:]:
#     print(i)





    



