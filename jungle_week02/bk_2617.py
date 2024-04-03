# 구슬 찾기  
# dfs를 사용해서 구현하였다. 무게의 중간이 될 수 없는 구슬일 경우 해당 구슬보다 무거운 구슬이 (n+1)//2개 이상 많거나 가벼운 구슬이 (n+1)//2개 이상 많다.
import sys

n,m = map(int,sys.stdin.readline().split())

graph1 = [[] for i in range(n+1)]
graph2 = [[] for i in range(n+1)]
for i in range(m):
    a,b  = map(int,sys.stdin.readline().split())
    graph1[a].append(b)
    graph2[b].append(a)                             # dfs탐색을하여 대소구분을 위해 두개의 방향 그래프를 만들었다. 방향이 없을 경우 무엇이 큰지 작은지 알수 없기 때문에   

def dfs(graph,start):
    count =0
    visited=[False]*(n+1)
    stack = [start]
    visited[start] =True
    while stack:
        removed = stack.pop()
        for i in graph[removed]:
            if not visited[i]:          # i값이 중복으로 stack에 들어가는 것을 방지하기위해 visited리스트 검사  
                count+=1                # removed 값보다 작거나 큰값이 있으면 count, 이 count값이 >= (n+1)//2 일 경우 removed는 중간 구슬이 될 수 있다.  
                stack.append(i)
                visited[i] = True
    return count


visite = 0
for i in range(1,n+1):
    if dfs(graph1,i) >= (n+1)//2:
        visite+=1               # 중간 구슬이 될 수 없는 구슬이 있을 경우 +1 
for i in range(1,n+1):
    if dfs(graph2,i) >= (n+1)//2:
            visite+=1
print(visite)
