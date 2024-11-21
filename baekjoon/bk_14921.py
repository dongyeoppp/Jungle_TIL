# 용액 합성하기 

import sys 
input = sys.stdin.readline

n = int(input())

new = list(map(int,input().split()))

start = 0
end = n-1
result = float('inf')
save = 0
while True:
    # start가 end보다 크거나 같아질 경우 반복문 종료 
    if start >= end:
        break
    answer = new[start] + new[end]
    # 0에 가장 가까운 값을 save에 저장 
    if abs(answer) < result:
        result = abs(answer)
        save = answer
    # 특성값이 0 보다 클 경우 
    if answer > 0 :
        end -= 1
    # 특성값이 0 보다 작을 경우     
    elif answer < 0:
        start += 1
    # 특성값이 0 일 경우 
    else:
        break
print(save)
