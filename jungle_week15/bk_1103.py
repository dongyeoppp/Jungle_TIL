# # 게임
# # dp와 dfs를 사용하여 풀이 
# import sys
# # 재귀 제한 늘림
# sys.setrecursionlimit(10**6)

# n, m = map(int,sys.stdin.readline().split())
# graph = []
# for i in range(n):
#     graph.append(str(sys.stdin.readline().strip()))

# result = 0
# visited = [[False]*m for i in range(n)]
# dp = [[0]*m for i in range(n)]
# def dfs(low,col,start,count):
#     global result
#     dx = [start,-start,0,0]
#     dy = [0,0,start,-start]
#     for i in range(4):
#         x = dx[i] + low
#         y = dy[i] + col
#         # dp에 저장된 수 보다 count+1이 클 경우에만 재귀 수행
#         # 중복되는 탐색을 제거하여 시간을 줄임 
#         if 0 <= x < n and 0 <= y < m and graph[x][y] != "H" and dp[x][y] < count+1 :
#             if visited[x][y]:
#                 print(-1)
#                 exit()
#             else:
#                 dp[x][y] = count+1
#                 visited[x][y] = True
#                 dfs(x,y,int(graph[x][y]),count+1)
#                 visited[x][y] = False
#     result = max(count,result)
# visited[0][0] = True
# dfs(0,0,int(graph[0][0]),1)
# print(result)

# 다른 방법으로 풀이 
import sys
# 재귀 제한 늘림
sys.setrecursionlimit(10**6)

n, m = map(int,sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(str(sys.stdin.readline().strip()))

visited = [[False]*m for i in range(n)]
dp = [[0]*m for i in range(n)]
def dfs(low,col,start):
    # 사이클 발생
    if visited[low][col]:
        print(-1)
        exit()
    if dp[low][col] != 0:
        return dp[low][col]
    visited[low][col] = True
    result = 1
    dx = [start,-start,0,0]
    dy = [0,0,start,-start]
    for i in range(4):
        x = dx[i] + low
        y = dy[i] + col
        if 0 <= x < n and 0 <= y < m and graph[x][y] != "H" :
            result = max(result,dfs(x,y,int(graph[x][y]))+1)
    visited[low][col] = False
    dp[low][col] = result
    return dp[low][col]
print(dfs(0,0,int(graph[0][0])))
