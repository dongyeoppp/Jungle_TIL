# 퇴사          
# dp를 사용하여 풀이하였다. 
import sys

n = int(sys.stdin.readline())  
new = []
for i in range(n):
    t, p = map(int,sys.stdin.readline().split())  
    new.append((t,p))

dp = [0 for i in range(n+1)]        # dp 배열
 
for i in range(n):
    for j in range(i+new[i][0],n+1):
        # 점화식
        dp[j] = max(dp[j],dp[i]+new[i][1])
print(dp[-1])