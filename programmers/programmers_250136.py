# 석유 시추 

# 처음 시도 : dfs를 이용해서 재귀로 풀이
# 효율성 테스트 실패 -> 런타임 에러 (시간초과)
def solution(land):
    def dfs(low,col,visited,count):
        visited[low][col] = True
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        for i in range(4):
            x = dx[i] + low
            y = dy[i] + col
            if 0 <= x <= len(land)-1 and 0 <= y <= len(land[0])-1 and not visited[x][y] and land[x][y] == 1:
                count = max(dfs(x,y,visited,count+1),count)
        return count
    
    result = 0
    for i in range(len(land[0])):
        visited = [[False] * len(land[0]) for k in range(len(land))]
        answer = 0
        for j in range(len(land)):
            if land[j][i] == 1 and not visited[j][i]:
                answer += dfs(j,i,visited,1)
        result = max(answer,result)
    
    return result

# dfs -> bfs로 바꿔서 풀이했지만 시간초과

# 석유 한 덩어리에 대해서 한 번의 bfs 탐색만 진행하기 위해 코드를 수정 

from collections import deque
def solution(land):
    def bfs(low,col,visited,answer):
        que = deque()
        que.append((low,col))
        count=1
        visited[low][col] = True
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        min_y = 501
        max_y = -1
        while que:
            relow, recol = que.popleft()
            # 석유 한 덩어리의 가장 큰 y값과 가장 작은 y 값을 저장 
            min_y = min(min_y,recol)
            max_y = max(max_y,recol)
            for i in range(4):
                x = dx[i] + relow
                y = dy[i] + recol
                if 0 <= x <= len(land)-1 and 0 <= y <= len(land[0])-1 and not visited[x][y] and land[x][y] == 1:
                    que.append((x,y))
                    visited[x][y] = True
                    count+=1
        # 가장 작은 y값과 가장 큰 y값 사이에 해당하는 y인덱스에 석유 덩어리의 크기 더하여 저장 
        for k in range(min_y,max_y+1):
                    answer[k]+=count
        return answer
    
    visited = [[False] * len(land[0]) for k in range(len(land))]
    # 시추관의 위치 표시 
    answer = [0]*(len(land[0]))
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i,j,visited,answer)
    return max(answer)