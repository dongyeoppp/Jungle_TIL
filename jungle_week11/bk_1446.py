# 지름길 
# 다이나믹 프로그래밍을 이용하여 풀이하였다.  
import sys

n ,d = map(int,sys.stdin.readline().split())
short_load = []
for i in range(n):
    start , end, l = map(int,sys.stdin.readline().split())
    if end > d or end-start < l:        # 지름길을 사용하지 않아도 되는 경우 제외
        continue
    short_load.append((start,end,l))        # 지름길의 경로를 short_load 리스트에 튜플 형태로 담았다. 

short_load.sort()       # 출발지점이 작은 것 부터 정렬을 해주었다. 
dp = [i for i in range(d+1)]        # dp 테이블 ,인덱스값을 넣어줌 

for i in short_load:
    for j in range(1,d+1):
        if i[1] == j:
            dp[i[1]] = min(dp[j],dp[i[0]]+i[2])     # 원래 채워져 있던 값과 short_load에 들어있는 지름길 경로의 시작지점을 인덱스로 가지는 dp값에 거리 값을 더해준 값을 비교 
        else:
            dp[j] = min(dp[j],dp[j-1]+1)    # dp의 값 갱신 
    print(dp)
print(dp[-1])
