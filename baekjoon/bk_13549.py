# 숨바꼭질 3 
# bfs를 사용하여 풀이 함
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())

# 시간을 체크하기 위한 방문 리스트 
visited = [0] * 100001
def bfs(x):
    que = deque()
    que.append(x)
    visited[x] = 1
    while que:
        removed = que.popleft()
        # 동생을 찾았을 경우 
        if removed == k:
            return visited[removed] -1
        # 3가지 경우를 고려하여 que에 넣는다. 
        for i in (removed*2,removed+1,removed-1):
            if 0<=i<=100000:
                # 순간이동 할 경우 
                if i == removed * 2:
                    # 갱신되었다고 무조건 빠르지 않을 수 있음으로 visited에 적힌 시간을 비교하여 que에 넣는다. 
                    if visited[i] == 0 or visited[i] > visited[removed]:
                        visited[i] = visited[removed]
                        que.append(i)
                # 걸어서 갈 경우 
                elif i == removed+1 or i == removed-1:
                    if visited[i] == 0 or visited[i] > visited[removed] + 1:
                        visited[i] = visited[removed] + 1
                        que.append(i)

print(bfs(n))