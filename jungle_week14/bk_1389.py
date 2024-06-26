# 케빈 베이컨의 6단계 법칙 
# 큐를 사용하여 풀이하였다. 
import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
new = [[] for i in range(n+1)]      # 양방향 그래프 만들기 
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    new[a].append(b)
    new[b].append(a)

def distance(new,start):
    que = deque()
    que.append((start,1))
    visited = [False]*(n+1)
    visited[start] = True
    result = 0
    while que:
        removed,recount = que.popleft()
        for i in new[removed]:
            if not visited[i]:
                que.append((i,recount+1))       # depth를 check해서 더해준다.
                result+=recount
                visited[i] = True
    return result

mini = float('inf')
save = 0
for i in range(1,n+1):
    if mini>distance(new,i):
        save = i                    # 가장 작은 값을 가지고 있는 인덱스를 출력한다. 
        mini = distance(new,i)          
print(save)