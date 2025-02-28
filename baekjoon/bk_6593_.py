# 상법 빌딩
# BFS를 사용하여 풀이 함 
import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs(row,col,floor):
    que = deque()
    que.append((row,col,floor))
    visited[floor][row][col] = 1
    while que:
        rerow, recol ,refloor = que.popleft()
        for i in range(6):
            x = dx[i] + rerow
            y = dy[i] + recol
            z = dz[i] + refloor
            if 0<= x < r and 0<= y < c and 0<= z < l and visited[z][x][y] == 0:
                # 출구일 경우 BFS 종료
                if graph[z][x][y] == "E":
                    return f"Escaped in {visited[refloor][rerow][recol]} minute(s)."
                # "." 으로 비어있는 칸일 경우 que에 좌표 넣고, visited에 최단거리 체크 
                if graph[z][x][y] == ".":
                    que.append((x,y,z))
                    visited[z][x][y] = visited[refloor][rerow][recol] + 1
    # 탈출 불가능 할 경우 
    return "Trapped!"
    
while True:
    l, r , c = map(int,input().split())
    # 입력 종료 조건 
    if l == 0:
        break
    graph = []
    for i in range(l):
        answer = []
        for j in range(r):
            answer.append(input().strip())
        graph.append(answer)
        input()
    # 3차원 리스트를 생성하여 방문 여부 + 최단 시간 체크 
    visited = [[[0]*c for _ in range(r)]for _ in range(l)]

    for i in range(l):
        for j in range(r):
            for k in range(c):
                # 시작 지점일 경우 BFS 수행 
                if graph[i][j][k] == "S":
                    print(bfs(j,k,i))
                    break