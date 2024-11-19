# 전깃줄
## dfs 빽트래킹을 하여 풀이 함 -> 시간초과
# import sys

# input = sys.stdin.readline

# n = int(input())

# line = []
# for i in range(n):
#     line.append(list(map(int,input().split())))

# count = [0] * n
# cross = []
# for i in range(n):
#     new = set()
#     for j in range(n):
#         if line[i][0] != line[j][0] and ((line[i][0]>line[j][0] and line[i][1] < line[j][1]) or (line[i][0] < line[j][0] and line[i][1] > line[j][1])):
#             count[i] += 1
#             new.add(j)
#     cross.append(new)
# answer = float('inf')
# def dfs(count,result):
#     global answer
#     save = []
#     maxi = max(count)
#     if maxi <= 0:
#         answer = min(result,answer)
#         return 
#     for i in range(n):
#         if maxi == count[i]:
#             save.append(i)
#     for i in save:
#         count[i] = 0 
#         result += 1
#         for j in range(n):
#             if i in cross[j]:   
#                 count[j] -=1
#         dfs(count,result)
#         count[i] = maxi
#         result -= 1
#         for j in range(n):
#             if i in cross[j]:
#                 count[j] +=1
    
# dfs(count,0)
# print(answer)

# 최장 증가 부분 수열(LIS) 갱신하며 풀이 
import sys

input = sys.stdin.readline

n = int(input())

line = []
for i in range(n):
    line.append(list(map(int,input().split())))
# A 전봇대 번호를 기준으로 정렬 
line.sort()
# dp배열에 겹치지 않는 최대 전깃줄의 개수를 갱신하며 저장 
dp = [1] * n

for i in range(1,n):
    for j in range(i):
        # i번째 전깃줄 보다 전에 있는 전깃줄들 비교
        # i번째 전깃줄과 j번째 전깃줄이 겹치지 않을 경우 dp 배열에 전깃줄의 개수 최대로 갱신 
        if line[i][1] > line[j][1]:
            dp[i] = max(dp[i],dp[j]+1)
# 전체 전깃줄의 개수 - 겹치지 않는 최대 전깃줄의 개수 => 서로 교차하지 않기 위해 없애야 하는 전깃줄의 최소 개수
print(n-max(dp))
