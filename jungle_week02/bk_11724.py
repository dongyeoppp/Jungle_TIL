# 연결 요소의 개수  
# 나누어진 각각의 그래프를 연결요소라고 한다.  

import sys
sys.setrecursionlimit(10 ** 6)
n,m = map(int,sys.stdin.readline().split())

graph = [[] for i in range(n+1)]        # 빈 그래프 만들기  

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())  
    graph[a].append(b)      
    graph[b].append(a)      #  무방향이므로 각 노드에 모두 요소를 넣어준다.  

def DFS(graph,start,visited):       #DFS알고리즘 재귀로 구현  
    if start not in visited:
        visited.append(start)
    for i in graph[start]:
        if i not in visited:
            visited.append(i)
            DFS(graph,i,visited)

visited = [] # 방문한 노드를 추가한다.  
count = 0       # dfs연산을 횟수 카운트  
for i in range(1,n+1):
    if i not in visited:    # visited리스트에 i 값이 없다면 dfs 실행  
        DFS(graph,i,visited)
        count+=1        # dfs 연산을 할때마다 +1씩 카운트   
print(count)


