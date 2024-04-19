# 동전2
# dp 테이블을 사용한 문제  
import sys
inf = float('inf')
new = []
n,k = map(int,sys.stdin.readline().split())
for i in range(n):
    a = int(sys.stdin.readline())
    new.append(a)
dp = [inf]*(k+1)        # 동전의 가치를 인덱스로 가지는 테이블 만듬 (초기값은 무한)
dp[0] = 0       # 가지고있는 동전으로 0원을 만들 수 있는 경우의 수는 없다.
for i in new:
    for j in range(i,k+1):      # 해당 동전 가치 인덱스부터
        dp[j] = min(dp[j],dp[j-i]+1)        # dp에 원래 들어가있던 값과 비교하여 작은값으로 dp 갱신  
if dp[-1] == inf:       # 가지고 있는 동전으로 주어진 k 를 만들 수 없는 경우 -1을 출력  
    print(-1)
else:
    print(dp[-1])