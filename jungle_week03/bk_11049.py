# 행렬의 곱셈 순서
# dp 알고리즘 문제, python으로 제출했는데 시간초과가 나와 pypy로 제출하여 통과했다.  
# 행렬 곱셉에 대한 점화식을 이해하고 인덱스 값을 맞춰주는 것이 상당히 어려웠다.  
import sys

n = int(sys.stdin.readline())
graph = [[0,0]]     # 인덱스를 맞춰주기 위해 잊어선안된다. 
inf = float('inf')
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
dp = [[0]*(n+1) for i in range(n+1)]    # 최소값을 저장할 dp 테이블  // i<j가 커야하므로 dp테이블의 일부만 사용하여 해결할 수 있다.

for i in range(1,n):                # i 값이 커질수록 대각선 오른쪽으로
    for j in range(1,n-i+1):        # j 값은 열을 의미하며 왼쪽 대각선을 의미하기도 한다. 
        dp[j][j+i] = inf        # 최솟값을 구하기 위해 큰값을 해당 위치에 넣어놓는다.  
        for k in range(j,j+i):      # k의 범위는 구하려는 위치의 행과 열 값의 사이로 놓는다.  
            dp[j][j+i] = min(dp[j][j+i],dp[j][k]+dp[k+1][j+i]+graph[j][0]*graph[k][1]*graph[j+i][1])  
            # 현재 해당 위치의 값과 행렬곱셉의 점화식을 이용한 값을 비교하여 최솟값으로 업데이트한다.  
print(dp[1][n])     # dp[1][n] 값에 최솟값이 저장된다.  




