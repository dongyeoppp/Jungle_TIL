# 숨바꼭질 4

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int,input().split())

# 이전 방문한 번호 체크 
visited = [-1]*100001

def bfs(n,k):
    que = deque()
    que.append(n)
    visited[n] = n
    while que:
        removed = que.popleft()
        if removed == k:
            return
        for i in (removed*2,removed+1,removed-1):
            if 0 <= i <= 100000 and visited[i] == -1:
                # 이전 번호 visited에 저장
                visited[i] = removed
                que.append(i)
    return 

bfs(n,k)
result = []
answer = k
while answer != visited[answer]:
    ans = visited[answer]
    result.insert(0,ans)
    answer = ans 
result.append(k)
print(len(result)-1)
print(*result)
