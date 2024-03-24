# N - Queen 

# import sys

# n = int(sys.stdin.readline().strip())
# queen_list = []
# count = 0

# for j in range(n):
#     new = [0] * n
#     queen_list.append(new)
#                             # n * n 행렬 만들기 
# def prime(k, h):
#     # print(k,h)
#     global n, queen_list
#     for i in range(k):         
#         if queen_list[i][h] == 1:           # 같은 열에 있을 경우 제외 
#             return False
#     for j in range(1,h+1):      
#         if queen_list[k-j][h-j] == 1:       # 왼쪽 대각선에 있을 경우 제외
#             return False
#     for w in range(1,n-h):
#         if queen_list[k-w][h+w] == 1:       # 오른쪽 대각선에 있을 경우 제외
#             return False
#     return True

# def queen(r):               # r은 같은 행을 의미  
#     global count    
#     if r == n:
#         count += 1      # r == 4 가 되었을 경우 모든 행에 퀸을 놓았으므로 count 값을 올려줌
#     for i in range(n):
#         if prime(r, i):     # TRUE 반환할 경우
#             queen_list[r][i] = 1        # 해당 행에 퀸을 배치하고 다음행으로 이동
#             queen(r + 1)                   # 다음행에서 다시 함수 재귀   
#             queen_list[r][i] = 0           # 모든 경우에 대한 검사를 마치면 퀸을 놓은 위치에 값 제거 , 백 트래킹!
# queen(0)
# print(count)

import sys
n = int(sys.stdin.readline())
count = 0
check_col = [False] * n     # 같은 열에 퀸이 있는지 검사
check_left = [False] * (2*n-1)      # 왼쪽 대각선에 퀸이 있는지 검사
check_right = [False] * (2*n-1)     # 오른쪽 대각선에 퀸이 있는지 검사

def queen(row):
    global n, count
    if row == n :       # 마지막행을 지나 row 가 n이 되었을때 -> 경우의 수 하나 찾음 -> count  + 1
        count +=1
    for col in range(n):                                                                            # 왼쪽 대각선이 겹치는 경우는 행과 열의 합이 같음을 이용.
        if not check_col[col]  and  not check_left[row+col] and not check_right[col - row + n -1]:      # 오른쪽 대각선이 겹치는 경우는 행과 열의 차이가 같음을 이용(음수 값이 나올 수 있으므로 (n-1)값을 더하여 이용)
            check_col[col] = check_left[row+col] = check_right[col-row+n-1] = True        # 퀸이 겹치는 자리에 없을 경우 true값을 넣어줌
            queen(row+1)        # rowr값에 +1을 해주어 다음 행 검사로 넘어감. 재귀 함수 사용
            check_col[col] = check_left[row+col] = check_right[col-row+n-1] = False     # 행 검사를 하며 퀸을 놓을 수 있는 경우가 나오면 False 값을 넣어 리스트의 값들을 초기화
queen(0)
print(count)


