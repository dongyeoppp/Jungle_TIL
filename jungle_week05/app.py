#  # z
# import sys  

# n,r,c = map(int,sys.stdin.readline().split())

# new = [[0]* 2**n for i in range(2**n)]
# row = 0 
# col = 0
# count = 0
# def recur(row,col):
#     if 
#         col+=2**n//2
#     elif i ==0:
#         row+=2**n//2
#     elif i ==0:
#         col+=2**n//2
#     elif i ==0:
#         col+=2**n//2
# re(0,0)

        
# for i in new:
#     print(i)    

# 구슬 찾기  

import sys 

n,m = map(int,sys.stdin.readline().split())
graph1 = [[] for i in range(n+1)]
graph2 = [[] for i in range(n+1)]
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph1[a].append(b)
    graph2[b].append(a)
def dfs(graph,start):
    stack=[]
    count = 0
    stack.append(start)
    while stack:
        removed = stack.pop()
        for i in graph[removed]:
            print(i)
            stack.append(i)
            count+=1
    return count

visite = 0
for i in range(1,n+1):
    if dfs(graph1,i)>=n//2+1:
        visite+=1
    if dfs(graph2,i)>=n//2+1:
        visite+=1
print(visite)





