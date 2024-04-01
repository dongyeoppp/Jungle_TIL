# 아침 산책  
import sys

n  = int(sys.stdin.readline())
a = sys.stdin.readline().strip()
graph = [[] for i in range(n+1)]
for i in range(n-1):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
in_out = [True]
for i in a:
    if i =='1':
        in_out.append(True)
    else:
        in_out.append(False)

def dfs(start):
    count = 0
    visited=[False]*(n+1)
    stack= [start]
    while stack:
        removed = stack.pop()
        visited[removed] = True
        for i in graph[removed]:
            if not visited[i]:
                if in_out[removed] and in_out[i]:
                    count+=1
                elif not in_out[removed] and in_out[i]:
                    count+=1
                else:
                    stack.append(i)
    return count
result = 0
for i in range(1,n+1):
    if in_out[i]:
        result += dfs(i)
print(result)




