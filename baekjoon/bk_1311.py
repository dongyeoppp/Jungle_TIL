# 할 일 정하기 1
# 첫 시도 벡트래킹으로 모든 경우의 수를 다 보았는데 중복되는 경우가 너무 많아 시간초과가 발생함
# import sys

# input = sys.stdin.readline

# n = int(input())
# new = []
# for i in range(n):
#     new.append(list(map(int,input().split())))

# result = float('inf')
# low_set = set()
# col_set = set()
# dx = []
# for i in range(-(n-1),n):
#     for j in range(n):
#         dx.append(i)
# dy = []
# for i in range(-(n-1),n):
#     dy.append(i)
# dy = dy * n

# def back(low,col,count,answer):
#     global result,low_set,col_set
#     if count == n:
#         if result > answer:
#             result = answer
#         return
#     for i in range(len(dx)):
#         x = dx[i] + low
#         y = dy[i] + col
#         if 0<= x < n and 0<= y < n and x not in low_set and y not in col_set:
#             answer += new[x][y]
#             count += 1 
#             low_set.add(x)
#             col_set.add(y)
#             back(x,y,count,answer)
#             answer -= new[x][y]
#             count -= 1
#             low_set.remove(x)
#             col_set.remove(y)

# for low in range(n):
#     for col in range(n):
#         back(low,col,0,0)
# print(result)

# 정답 풀이 
import sys

input = sys.stdin.readline

n = int(input())
new = []
for i in range(n):
    new.append(list(map(int,input().split())))
# 비트 마스킹을 할 배열 생성/ ex) n = 3일 경우 (000 ~ 111)
visited = [-1] * (1<<n)

def dfs(row,visit):
    # 모든 작업을 다 수행한 경우 
    if row == n:
        return 0
    # 중복 계산을 방지
    if visited[visit] != -1:
        return visited[visit]
    result = float('inf')
    for i in range(n):
        # 해당 작업이 선택되지 않았을 경우 
        if (visit & (1<<i)) == 0:
            # 최솟값 갱신 
            result = min(result, dfs(row+1, visit | (1<<i)) + new[row][i])
    # 현재 비트마스크의 최솟값을 저장 
    visited[visit] = result 
    return result
print(dfs(0,0))