# 정수 삼각형 
# 다이나믹 프로그래밍으로 풀이하였다.  
import sys

n = int(sys.stdin.readline())
graph = []
for i in range(n):
    new = list(map(int,sys.stdin.readline().split()))
    graph.append(new)       # 삼각형 배열 받기  

dp = [[0]*(n+1) for i in range(n+1)]        # dp 테이블 

for i in range(1,len(graph)+1): 
    for j in range(1,len(graph[i-1])+1):  
        dp[i][j] = max(dp[i-1][j-1],dp[i-1][j])+graph[i-1][j-1] # dp 점화식 , 전 행에 있던 값에서 더해질 수 있는 값 중 큰 값을 골라 더해서 dp 테이블을 갱신해준다.

print(max(dp[-1]))  # dp 테이블에서 가장 마지막 행에 있는 값들 중 가장 큰 값을 출력한다. 