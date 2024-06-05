# 2의 멱수의 합   
# dp를 이용하여 풀이하였다. 
import sys

n = int(sys.stdin.readline())

dp = [0]*(n+1)

dp[1] = 1

for i in range(2,n+1):
    if i%2 == 0:
        dp[i] = (dp[i-1] + dp[i//2]) % 1000000000       # i가 짝수인 경우 
    else:
        dp[i] = dp[i-1] % 1000000000          # i 가 홀수일 경우
print(dp[-1])


# 동전 문제 처럼도 풀어보자  