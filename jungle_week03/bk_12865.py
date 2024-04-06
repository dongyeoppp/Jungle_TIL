# 아주 평범한 배낭  
# knapsack 문제이다. 행렬을 그려보며 풀이하였다.  
import sys

n, k = map(int,sys.stdin.readline().split())  
items = []*(n+1)        # 물건의 무게와 가치를 넣을 리스트
items.append([0,0])     # 첫 인덱스에는 0,0 값을 넣어 준다. (물건이 없을 경우)

for i in range(n):
    item = list(map(int,sys.stdin.readline().split()))
    items.append(item) 

dp = [[0]*(k+1) for i in range(n+1)]        # 물건의 가치를 넣어 업데이트 할 리스트  (dp테이블: 이전 값을 고려하여 값을 갱신한다.)
for i in range(1,n+1):
    for j in range(1,k+1):
        if j < items[i][0]:             # 현재 물건의 무게가 배낭에 들어갈 수 있는 무게 보다 클 경우 (가방에 들어갈 수 있는 무게의 최대값(j)보다 물건이 무거우면 가방에 넣을 수 없다.)  
            dp[i][j] = dp[i-1][j]       # 이전 물건에서 해당 무게에 넣은 가방의 가치를 그대로 넣어준다.  
        else:
            dp[i][j]=max(items[i][1]+dp[i-1][j-items[i][0]],dp[i-1][j])     # 이번 해당 물건을 가방에 넣을 수 있을 경우(가방의 넣을 수 있는 최대 무게 보다 해당 물건의 무게가 더 가벼울 경우)  
                                                                            # 해당 물건의 가치(items[i][1]) + 이전 물건의 인덱스 행에서 (현재 가방에 넣을 수 있는 무게 - 현재 물건의 무게)인 열에 들어있는 값과
                                                                            # 이 전 물건(i-1)에서 해당 무게(j)에 넣은 가방의 가치를 비교하여 더 큰 값으로 갱신  

print(dp[n][k])
