# 텀 프로젝트 
# dfs 재귀를 사용하여 풀이 함. 시간초과 발생 !!

# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# t = int(input())

# def dfs(number):
#     global answer
#     if visited[student[number]]:
#         answer= number
#         return
#     visited[student[number]] = True
#     dfs(student[number]-1)

# for i in range(t):
#     n = int(input())
#     student = list(map(int,input().split()))
#     result = [0] * (n+1)
#     for j in range(n):
#         if result[j+1] == 1:
#             continue
#         visited = [False] * (n+1)
#         answer = 0
#         dfs(j)
#         if answer == j:
#             for k in range(1,n+1):
#                 if visited[k]:
#                     result[k] = 1
#     print(result.count(0)-1)


# 정답 풀이
# dfs 재귀 풀이 
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

def dfs(number):
    global result
    visited[number] = True
    cycle.append(number)
    number = student[number]
    if visited[number]:
        if number in cycle:
            result += len(cycle[cycle.index(number):])
        return
    dfs(number)

for i in range(t):
    n = int(input())
    student = [0]+list(map(int,input().split()))
    result = 0
    visited = [False] *(n+1)
    for j in range(1,n+1):
        if not visited[j]:
            cycle = []
            dfs(j)
    print(n-result)