# DFS와 BFS   

import sys
from collections import deque 

n,m,v=map(int,sys.stdin.readline().split())

arr = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

queue = deque()
stack = []

def BFS(arr,v,result=[]):
    for i in arr:
        i.sort()
    visited = [False]*(n+1)     # 해당 노드를 갔다왔는지 체크  
    queue.append(v)
    visited[v] = True

    while queue:
        current = queue.popleft()
        result.append(current)
        for i in arr[current]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return result

def DFS(arr,v,result=[]):
    for i in arr:
        i.sort(reverse=True)        # 작은 수가 stack에서 먼저 나갈 수 있도록 함  
    stack = [v]     # 스택 리스트를 추가하여 처음 방문하는 노드를 넣는다. 
    while stack:
        current_node = stack.pop()
        if current_node not in result:
            result.append(current_node)
            for i in arr[current_node]:
                stack.append(i)
            # stack.extend(arr[current_node]) 위의 for문을 extend를하여 표현 가능  
    return result

for i in DFS(arr,v):
    print(i,end=" ")
print()
for i in BFS(arr,v):
    print(i,end=" ")
