# 2*n 타일링 2

import sys

n =  int(sys.stdin.readline())

dp = [0]*(n+1)
dp[1] = 1
if n == 1:
    print(1)
    
# n이 2이상일 경우
else:
    dp[2] = 3
    for i in range(3,n+1):
        dp[i] = dp[i-2]*2 + dp[i-1]
    print(dp[n]%10007)