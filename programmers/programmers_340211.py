# 충돌 위험 찾기 
# 단순 구현으로 풀이 
def solution(points, routes):
    # 최단 거리 구하기 -> 먼저 출발지와 목적지의 행의 값을 맞추고 열의 값을 맞춘다.
    # time -> 로봇이 움직인 시간 
    def bfs(start,end,time):
        start_row = points[start-1][0]
        start_col = points[start-1][1]
        end_row = points[end-1][0]
        end_col = points[end-1][1]
        if answer == []:
            answer.append((start_row,start_col,time))
        elif answer[-1] != (start_row,start_col,time):
            answer.append((start_row,start_col,time))
        while start_row != end_row:
            if start_row > end_row:
                start_row -= 1
                time +=1
                answer.append((start_row,start_col,time))
            elif start_row < end_row:
                start_row += 1
                time +=1
                answer.append((start_row,start_col,time))
        while start_col != end_col:
            if start_col > end_col:
                start_col -= 1
                time+=1
                answer.append((start_row,start_col,time))
            elif start_col < end_col:
                start_col += 1
                time+=1
                answer.append((start_row,start_col,time))
        return time
    # answer 리스트에 로봇이 위치한 행,열,시간 추가 
    answer = []
    for i in routes:
        time = 0
        for j in range(len(i)-1):
            time = bfs(i[j],i[j+1],time)
    # 초로 묶어서 행,열 값을 result에 추가 
    result = {}
    for i in answer:
        if i[2] not in result:
            result[i[2]] = []
            result[i[2]].append([i[0],i[1]])
        else:
            result[i[2]].append([i[0],i[1]])
    
    count = 0
    for i in result:
        new = []
        for j in result[i]:
            # 특정 초에 해당하는 [행,열]의 값이 2개 이상일 경우: 그 시간에 같은 곳에 위치한 로봇이 2개 이상임을 의미
            # 충돌 위험으로 판단 
            if j not in new and result[i].count(j) >=2:
                count+=1
            new.append(j)
    return count