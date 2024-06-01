# ABCDE   
# DFS와 백트래킹을 이용하였다. 
import sys   

n,m = map(int,sys.stdin.readline().split())
graph = [[]for i in range(n)]

for i in range(m):
    a ,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)      # 양방향 그래프  
check =False        # depth가 4이상인지 체크
def dfs(graph, visited, start, depth):
    global check
    if depth == 4:      #  종료 조건 , depth가 4이상일 경우 
        print(1)
        check=True
        exit()          # 재귀 종료
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, visited, i, depth + 1)
    visited[start] = False     # 재귀 종료, 다시 visited false 체크하여 재귀 문을 통해 다시 해당 노드로 갈 수 있게 함 , 중복 가능 

visited = [False]*n
for i in range(n):
    dfs(graph,visited,i,0)
if check == False:
    print(0)