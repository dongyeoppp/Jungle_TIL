# 사다리 조작
# dfs로 풀이 
# python 시간초과 발생 -> pypy로 제출해서 성공

import sys

input = sys.stdin.readline
n, m, h = map(int,input().split())

# 사다리에 대한 행렬 생성 
ladder = [[-1] * (n+1) for i in range(h+1)]
# 가로선 생성, right일 경우 오른쪽으로 left일 경우 왼쪽으로 사다리 타기 
for i in range(m):
    a,b = map(int,input().split())
    ladder[a][b] = "right"
    ladder[a][b+1] = "left"

# 해당 사다리를 탔을 때 결과값이 참일 경우 true 리턴
def check():
    for i in range(1,n+1):
        answer = i
        for j in range(1,h+1):
            if ladder[j][answer] == "right":
                answer+=1
            elif ladder[j][answer] == "left":
                answer-=1
        if answer != i:
            return False
    return True

result = float('inf')
def dfs(count):
    global result
    # 원하는 값이 나올 경우 return
    if check():
        result = min(result,count)
        return
    # count값이 3 보다 커질 경우 return 
    if count  == 3 or result <= count:
        return 
    else:
        for i in range(1,n):
            for j in range(1,h+1):
                if ladder[j][i] == -1 and ladder[j][i+1] == -1:
                    ladder[j][i] = "right"
                    ladder[j][i+1] = "left"
                    dfs(count+1)
                    ladder[j][i] = -1
                    ladder[j][i+1] = -1
    return 

dfs(0)
if result > 3:
    result = -1
print(result)



