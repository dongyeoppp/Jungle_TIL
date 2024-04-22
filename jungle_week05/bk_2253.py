# 점프  
# dp를 이용해서 해결하는 문제이다. 처음에 greedy한 접근(가장 멀리 점프하는 방법)으로 풀었지만 오답이었다.    
# import sys 

# n, m = map(int,sys.stdin.readline().split())
# dp = [0] * (n+1)
# dp_check = [True] * (n+1)
# for i in range(m):
#     a = int(sys.stdin.readline())
#     dp_check[a] = False

# dp[0] = 0
# dp[1] = 0
# dp[2] = 1
# start = 2
# jump = 2
# while start < n:
#     check = 0
#     for i in range(start+jump,start+jump-3,-1):
#         if start>=i:
#             check=-1
#             exit()
#         if i<=n and dp_check[i] == True:
#             dp[i] = dp[start]+1
#             check+=1
#             start = i
#             jump+=1
#             break
#         jump-=1
#     if check==0:
#         check=-1
#         break
# if check == -1:
#     print(check)
# else:
#     print(dp[-1])

import sys

n, m = map(int,sys.stdin.readline().split())
mini_stone = []     # 올라가지 못하는 작은 돌 번호 저장  
for i in range(m):
    a = int(sys.stdin.readline())
    mini_stone.append(a)
inf = float('inf')

dp = [[inf]*(int((n*2)**0.5)+2) for i in range(n+1)]        # 최대값을 초기화한 dp테이블  등차수열의 합 공식을  사용 -> n = k(k+1)//2 -> k<(2*n)**0.5로 근사한다.

dp[1][0]=0      # 처음에 1번 돌에 이미 서있으므로 0 을 넣어줌

for i in range(2,n+1):
    if i in mini_stone:         # 작은 돌일경우 넘김  
        continue
    for j in range(1,int((i*2)**0.5)+1):
        dp[i][j] = min(dp[i-j][j],dp[i-j][j-1],dp[i-j][j+1])+1          # i-j번째 돌에서 속도를 유지 혹은 -1. +1한 경우만 비교한다.

if min(dp[-1]) == inf :         # 주어진 목적지로 도착하지 못하는 경우 -1 출력   
    print(-1)
else:
    print(min(dp[-1]))