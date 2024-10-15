# 지구 온나화

import sys
input = sys.stdin.readline

r, c = map(int,input().split())
map = []
for i in range(r):
    new = str(input().strip())
    map.append(new)

# check = "x"는 True, "."은 False로 체크한 행렬
check = []
for i in map:
    answer = []
    for j in i:
        if j == ".":
            answer.append(False)
        else:
            answer.append(True)
    check.append(answer)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(r):
    for j in range(c):
        # "X" 주변에 "X"가 하나 이하라면 check 행렬에 False로 체크 
        if "X" == map[i][j]:
            count = 0
            for k in range(4):
                x = dx[k] + i
                y = dy[k] + j
                if 0<=x<r and 0<=y<c and map[x][y] == "X":
                    count +=1 
            if count < 2:
                check[i][j] = False
# True로 체크된 곳의 인덱스의 값을 모두 구해 최소.최댓값 확인 
result_x = []
result_y = []
for i in range(r):
    for j in range(c):
        if check[i][j]:
            result_x.append(i)
            result_y.append(j)
# 최소 모양의 직사각형 행 자르기
check = check[min(result_x):max(result_x)+1]
maxi_result_y = max(result_y)
mini_result_y = min(result_y)

# 최소 모양의 직사각형 열 자르고, 한 행씩 출력 
for i in check:
    answer = i[mini_result_y:maxi_result_y+1]
    new_answer = ""
    for j in answer:
        if j:
            new_answer+="X"
        else:
            new_answer+="."
    print(new_answer)