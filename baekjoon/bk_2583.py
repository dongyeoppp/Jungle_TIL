# 영역 구하기   
# bfs를 사용하여 풀이  

import sys
from collections import deque
input = sys.stdin.readline

m,n,k = map(int,input().split())
visited = [[False]*n for _ in range(m)]
for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    # 입력을 받으며 모눈 종이에 직사각형 true로 체크 
    for j in range(x1,x2):
        for k in range(y1,y2):
            if not visited[k][j]:
                visited[k][j] = True
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(row,col):
    que = deque()
    answer = 1
    que.append((row,col))
    visited[row][col] = True
    while que:
        rerow, recol = que.popleft()
        for i in range(4):
            x = rerow + dx[i]
            y = recol + dy[i]
            if 0<=x<m and 0<=y<n and not visited[x][y]:
                que.append((x,y))
                visited[x][y] = True
                # 영역의 넓이 체크 
                answer+=1
    return answer

result = []
for i in range(m):
    for j in range(n):
        # 직사각형이 아닌 경우 
        if not visited[i][j]:
            result.append(bfs(i,j))
# 영역의 넓이를 오름차순 정렬  
result.sort()
print(len(result))
print(*result)
