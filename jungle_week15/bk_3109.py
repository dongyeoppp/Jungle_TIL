# 빵집

import sys
n , m = map(int,sys.stdin.readline().split())
new = []
for i in range(n):
    new.append(sys.stdin.readline().strip())

visited = [[False] * m for i in range(n)]
# 이동 방향 
dx = [-1,0,1]
def dfs(low,col):
    # 마지막 열에 도착 했을 경우 재귀 종료 
    if col+1 == m :
        return True
    for i in range(3):
        x = dx[i] + low
        y = col + 1
        if 0<=x < n and 0<= y < m and new[x][y] != "x" and not visited[x][y]:
            visited[x][y] = True
            if dfs(x,y):
                return True

result = 0
for i in range(n):
    # 마지막 열까지 파이프라인을 연결할 수 있을 경우 
    if dfs(i,0):
        result+=1
print(result)
