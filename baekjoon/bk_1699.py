# 제곱수의 합 

import sys

n = int(sys.stdin.readline())

dp = [i for i in range(n+1)]

# 사용할 수 있는 가장 큰 제곱수까지 
for i in range(2,int(n**(1/2))+1):
    # 4부터 n까지를 dp 테이블을 채워감 
    for j in range(i**2,n+1): 
        if j % (i**2) == 0:
            dp[j] = j // (i ** 2)
        else:
            if dp[j] > dp[j%(i**2)] + dp[j//(i**2)]:
                dp[j] = dp[j%(i**2)] + dp[j//(i**2)]
            #  dp[j] = min(dp[j],dp[j%(i**2)] + dp[j//(i**2)]) 을 위의 로직으로 대체하여 시간 복잡도를 낮춤 

print(dp[-1])
