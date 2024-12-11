# 거리두기 확인하기 
from collections import deque
def solution(places):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    def bfs(new,j,k,visited):
        que = deque()
        que.append((j,k))
        visited[j][k] = True
        while que:
            row, col = que.popleft()
            for i in range(4):
                x = row + dx[i]
                y = col + dy[i]
                # 파티션이 없을 경우 bfs 이동 
                if 0 <= x < 5 and 0 <= y < 5 and new[x][y] != "X" and not visited[x][y] and abs(j-x)+abs(k-y) <= 2:
                    # 맨해튼 거리 안에 P가 존재할 경우 거리두기 실패 
                    if new[x][y] == "P":
                        return False
                    que.append((x,y))
                    visited[x][y] = True
        return True
                
    result = []
    for i in places:
        visited = [[False]*5 for i in range(5)]
        save = True
        for j in range(5):
            for k in range(5):
                # 응시자가 앉아 있는 자리 체크 
                if i[j][k] == "P":
                    if not bfs(i,j,k,visited):
                        # 거리두기 실패 했을 경우 save = False로 바꾸고 반복문 종료 
                        save = False
                        break
            if not save:
                break
        # save 값을 체크하여 result 리스트에 값 추가 
        if save:
            result.append(1)
        else:
            result.append(0)       
    return result