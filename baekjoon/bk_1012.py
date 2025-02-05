# 유기농 배추   
# dfs를 사용하여 풀이    
import sys
# recursion error를 방지하기 위해 제한 값을 재 조정 (원래는 10**3)
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(row, col,new):
    # 지렁이가 갈 수 있는 배추를 2로 지정하여 재방문 방지 
    new[row][col] = 2
    for i in range(4):
        x = row + dx[i]
        y = col + dy[i]
        if 0<= x < n and 0 <= y < m and new[x][y] == 1:
            dfs(x,y,new)

for i in range(t):
    m, n, k = map(int,input().split())
    # 0을 기본 값으로 지정 
    new = [[0]*m for _ in range(n)]
    for j in range(k):
        col, row = map(int,input().split())
        # 배추가 심어진 곳을 1로 변경 
        new[row][col] = 1
    count = 0
    for p in range(n):
        for q in range(m):
            if new[p][q] == 1:
                dfs(p,q,new)
                # 지렁이 개수 체크
                count +=1
    print(count)