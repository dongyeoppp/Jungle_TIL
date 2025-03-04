# 그림
# bfs를 사용하여 풀이 함 
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
new = []
for i in range(n):
    new.append(list(map(int,input().split())))

visited = [[False]*m for i in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(row,col):
    que = deque()
    visited[row][col] = True
    que.append((row,col))
    answer = 1
    while que:
        rerow , recol = que.popleft()
        for i in range(4):
            x = rerow + dx[i]
            y = recol + dy[i]
            if 0 <= x <n and 0<= y< m and new[x][y] == 1 and not visited[x][y]:
                que.append((x,y))
                visited[x][y] = True
                # 그림 넓이 체크 
                answer+=1
    return answer
            

count = 0
result = 0
for i in range(n):
    for j in range(m):
        if new[i][j] == 1 and not visited[i][j]:
            answer = bfs(i,j)
            # 그림의 넓이 중 가장 큰 값을 result에 저장 
            result = max(answer,result)
            # 그림의 개수 체크 
            count +=1

print(count)
print(result)
