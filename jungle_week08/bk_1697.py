# 숨바꼭질   
# 시간초과로 실패
# import sys

# n , k = map(int,sys.stdin.readline().split())  
# count = 0
# while n != k :
#     if k % 2 == 1:
#         k+=1
#         count+=1
#     else:
#         k = k // 2
#         count+=1
# print(count)

# bfs를 이용하여 구현하였다.  
import sys
from collections import deque 
n , k = map(int,sys.stdin.readline().split())

def bfs(start):    
    que = deque()
    que.append((start,0))
    visited=[False] * 100001        # 이동할 수 있는 최대 위치 = 100000
    visited[start] = True
    while que:
        removed,sec= que.popleft()     # sec는 시간, depth를 의미한다. 
        if removed == k:
            return sec
        if removed- 1 >= 0 and not visited[removed-1]:      # 음수 값이 들어갈 수 없도록한다. 0까지는 갈 수 있음
            que.append((removed-1,sec+1)) 
            visited[removed-1] = True
        if removed*2 < 100001 and not visited[removed*2]:
            que.append((removed*2,sec+1))
            visited[removed*2] = True
        if removed+1 < 100001 and not visited[removed+1]:
            que.append((removed+1,sec+1))
            visited[removed+1] = True
print(bfs(n))

