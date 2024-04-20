# 행렬 곱셈 순서   
import sys 
n = int(sys.stdin.readline())
graph = [(0,0)]
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    graph.append((a,b))
dp =[[0]*(n+1) for i in range(n+1)]
inf = float('inf')
for i in range(1,n):
    for j in range(1,n-i+1):
        dp[j][j+i] = inf
        for k in range(i,j+i):
            dp[j][j+i] = min(dp[j][j+i],dp[j][k]+dp[k+1][j+i]+graph[j][0]*graph[k][1]*graph[j+i][1])
print(dp[1][n])