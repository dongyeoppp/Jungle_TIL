# 쉬운 계단수   
# dp로 문제를 풀이하였다.  
import sys

n = int(sys.stdin.readline())

dp = [[0]*10 for i in range(n+1)]   # 행은 일의자리숫자를, 열은 계단수의길이를 나타낸다.    
dp[1][0] = 0
for i in range(1,10):
    dp[1][i] = 1
# 점화식을 사용하여 풀이  
for i in range(2,n+1):
    for j in range(0,10):
        if j == 0:                  # 예외 경우 1, 일의 자릿수가 0일때 
            dp[i][j] += dp[i-1][j+1]        
        elif j == 9:                   # 예외 경우 2, 일의 자릿수가 9일때  
            dp[i][j] += dp[i-1][j-1]
        else:                           # 이외의 경우   
            dp[i][j] += (dp[i-1][j+1] + dp[i-1][j-1])

print(sum(dp[-1])%1000000000)