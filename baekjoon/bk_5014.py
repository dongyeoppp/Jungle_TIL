# 스타트 링크 
# bfs가 아닌 큐를 이용한 풀이에 가깝다. 다른 bfs 풀이를 참고해보자  

import sys
from collections import deque
input = sys.stdin.readline

f, s, g,u,d = map(int,input().split())
# 방문했던 층수 add하며 체크 
check = set()

def bfs():
    que = deque()
    que.append((s,0))
    while que:
        here, ans = que.popleft()
        # g층에 도착했을 경우 
        if here == g:
            return ans
        # 지금 있는 층수보다 목적지 층수가 더 클 경우 
        if here < g:
            new_here = here+u
            # 지금 위치에서 u층 위로 이동하였을 때 해당 층 수가 없을 경우 
            if new_here > f:
                new_here = here - d
                # 아무 층으로도 이동 못할 경우 - 이 예외를 체크하지 않아 실패를 했었다.
                if new_here < 1:
                    return -1
            # 방문 했던 층일 경우 -1 return 
            if new_here in check:
                return -1
            # 다음 층수 que에 push
            que.append((new_here,ans+1)) 
            check.add(new_here)
        # 지금 있는 층수보다 목적지 층수가 더 작을 경우 
        elif here > g:
            new_here = here -d 
            # 지금 위치에서 d층 아래로 이동하였을 때 해당 층수가 없을 경우 
            if new_here < 1:
                new_here = here + u
                # 아무 층으로도 이동하지 못할 경우 - 이 예외 체크 필수..
                if new_here > f:
                    return -1
            # 방문했던 층일 경우 -1 return 
            if new_here in check:
                return -1
            # 다음 층수 que에 push
            que.append((new_here,ans+1))
            check.add(new_here)
            
result = bfs()
# 해당 층수를 방문할 수 없을 경우 
if result == -1:
    print("use the stairs")
else:
    print(result)

################################################################

# 다른 풀이 
import sys
from collections import deque
input = sys.stdin.readline

f, s, g,u,d = map(int,input().split())

def bfs():
    que = deque()
    que.append(s)
    visited[s] = 1
    while que:
        here = que.popleft()
        # 목적지에 도달했을 경우 
        if here == g:
            return visited[here] -1
        # 현재 위치에서 올라가거나 내려갈 경우의 층수를 모두 que에 넣는다. (범위 안에 있는 층수 이고 방문하지 않은 층수여야 함)
        for i in (here+u,here-d):
            if 1<= i <= f and visited[i] == 0:
                    que.append(i)
                    # 거리 갱신
                    visited[i] = visited[here] + 1

    # 목적지에 도달하지 못한 경우 
    return "use the stairs"
# f만큼의 배열을 생성
visited = [0] * (f+1)
print(bfs())