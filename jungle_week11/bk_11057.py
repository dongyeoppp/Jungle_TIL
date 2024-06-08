# 오르막 수 
# 다이나믹 프로그래밍으로 풀이하였다.  

import sys

n = int(sys.stdin.readline())

dp = [[1]*10 for i in range(n)]     # dp 테이블 생성 

for i in range(1,n):
    dp[i][0] = sum(dp[i-1])     # 전 행의 모든 원소의 합을 다음 행의 첫번째 값에 넣는다. 
    for j in range(1,10):
        dp[i][j] = dp[i][j-1] - dp[i-1][j-1]        # dp 방정식 
print(sum(dp[-1])%10007)    # 마지막 행의 값들을 모두 더해 출력 (나머지로 구하지 않으면 틀림)



