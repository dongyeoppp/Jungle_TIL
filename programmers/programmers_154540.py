# 무인도 여행
# bfs 사용하여 풀이 
from collections import deque
def solution(maps):
    new_low = len(maps)
    new_col = len(maps[0])
    visited = [[False]*new_col for i in range(new_low)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    def bfs(low,col):
        answer = 0
        que = deque()
        que.append((low,col))
        visited[low][col] = True
        answer += int(maps[low][col])
        while que:
            relow, recol = que.popleft()
            for i in range(4):
                x = relow + dx[i]
                y = recol + dy[i]
                if 0 <= x < new_low and 0 <= y < new_col and maps[x][y] != "X" and not visited[x][y]:
                    que.append((x,y))
                    visited[x][y] = True
                    answer+=int(maps[x][y])
        return answer
    
    result = []
    for i in range(new_low):
        for j in range(new_col):
            # 무인도이거나 방문하지 않은 경우 bfs 수행 
            if maps[i][j] != "X" and not visited[i][j]:
                result.append(bfs(i,j))
    result.sort()
    # 무인도가 없을 경우 [-1] 리턴  
    if result == []:
        return [-1]
    else:
        return result
    

# dfs 풀이

import sys
# 재귀 제한 해제해야 런타임에러 안남
sys.setrecursionlimit(10**6)
def solution(maps):
    new_low = len(maps)
    new_col = len(maps[0])
    visited = [[False]*new_col for i in range(new_low)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    def dfs(low,col):
        visited[low][col] = True
        answer = int(maps[low][col])
        for i in range(4):
            x = low + dx[i]
            y = col + dy[i]
            if 0 <= x < new_low and 0 <= y < new_col and maps[x][y] != "X" and not visited[x][y]:
                # dfs(x,y)값을 리턴하지 않고 answer에 누적하여 더해준다. 
                answer += dfs(x,y)
        return answer
    result = []
    for i in range(new_low):
        for j in range(new_col):
            if maps[i][j] != "X" and not visited[i][j]:
                result.append(dfs(i,j))
    result.sort()
    if result == []:
        return [-1]
    else:
        return result
        