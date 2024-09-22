# 피리 부는 사나이
import sys

input = sys.stdin.readline
# n -> 행, m -> 열
n, m = map(int,input().split())

new = []
for i in range(n):
    new.append(input().strip())

visited = [[False]*m for i in range(n)]
# 사이클을 체크할 새로운 리스트 생성 
check = [[0]*m for i in range(n)]
# count = 최소 safe zone의 개수 
count = 0

def dfs(row,col):
    global count
    if not visited[row][col]:
        visited[row][col] = True
        # 같은 사이클은 같은 answer 값을 가진다. 
        check[row][col] = answer
    else:
        # 이미 생성된 사이클을 침범했는지의 여부 확인
        # 침범하지 않았다면 count + 1
        if check[row][col] == answer:
            count+=1
        return
    if new[row][col] == "D":
        dfs(row+1,col)
    elif new[row][col] == "L":
        dfs(row,col-1)
    elif new[row][col] == "U":
        dfs(row-1,col)
    elif new[row][col] == "R":
        dfs(row,col+1)

answer = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            answer+=1
            dfs(i,j)
print(count)