# 나이트의 이동 
# bfs를 사용하여 풀이 
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    start_row, start_col = map(int,input().split())
    end_row, end_col = map(int,input().split())
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    new_dx = [-1,-1,-1,1,1,1,-1,1]
    new_dy = [-1,1,-1,-1,-1,1,1,1]
    visited = [[0]*n for _ in range(n)]
    def bfs(row,col):
        que = deque()
        visited[row][col] = 1
        que.append((row,col))
        while que:
            rerow, recol = que.popleft()
            # 나이트 이동 
            for i in range(4):
                for j in range(2):
                    x = dx[i]+ rerow + new_dx[i*2+j]
                    y = dy[i]+ recol + new_dy[i*2+j]
                    if 0<=x<n and 0<=y<n and visited[x][y]  == 0:
                        visited[x][y] = visited[rerow][recol] + 1
                        # 나이트가 이동하려는 칸에 도착 
                        if x == end_row and y == end_col:
                            return 
                        que.append((x,y))
        return
    bfs(start_row,start_col)
    print(visited[end_row][end_col]-1)