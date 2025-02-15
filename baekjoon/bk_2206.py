# 벽 부수고 이동하기   
# bfs를 사용하여 풀이

import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

new = []
for i in range(n):
    new.append(input().strip())

dy = [1,-1,0,0]
dx = [0,0,1,-1]
# 3차원 배열을 사용 
# visited[row][col][0] -> 벽을 부시지 않은 경로
# visited[row][col][1] -> 벽을 부신 경로 
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

def bfs(row,col,count):
    que = deque()
    visited[row][col][count] = 1
    que.append((row,col,count))
    while que:
        rerow,recol,recount = que.popleft()
        # 목표 위치에 도달 
        if rerow == n-1 and recol == m-1:
            return visited[rerow][recol][recount]
        for i in range(4):
            x = dx[i] + rerow
            y = dy[i] + recol
            if 0<= x < n and 0 <= y < m :
                # 벽을 만났지만 벽을 부수지 않은 경로일 경우  
                if new[x][y] == "1" and recount == 0:
                    visited[x][y][1] = visited[rerow][recol][0] + 1
                    que.append((x,y,1))
 
                # 벽이 안니고 지나치지 않은 경로일 경우  
                elif new[x][y] == "0" and visited[x][y][recount] == 0:
                    visited[x][y][recount] = visited[rerow][recol][recount] + 1
                    que.append((x,y,recount))
            
    return -1

print(bfs(0,0,0))

