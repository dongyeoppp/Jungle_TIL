#  동전  

import sys

t= int(sys.stdin.readline())  

for i in range(t):
    n = int(sys.stdin.readline())       # 동전 갯수
    new = list(map(int,sys.stdin.readline().split()))    # 동전의 각 금액  
    m = int(sys.stdin.readline())       # n개의 동전으로 만들어야하는 금액  

    dp = [0]*(m+1)      # dp배열은 만들어야하는 각 금액 별로 가능한 동전의 조합 수가 들어간다.  
    dp[0] = 1           # 0원을 만들 경우의 수 1  
    for i in new:
        for j in range(1,m+1):
            if j >= i:          # 동전 금액보다 dp의 인덱스 값이 큰 경우에만 경우의 수를 추가한다.  
                dp[j] += dp[j-i] # 동전의 금액을 주기로 경우의 수가 더해지며 갱신된다.  
    print(dp[-1])


    


