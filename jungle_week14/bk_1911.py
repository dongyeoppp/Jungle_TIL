# 흙길 보수하기     
# 첫번째 풀이  
# answer값이 마지막 웅덩이의 끝나는지점까지 커지는 경우의 수를 보았는데 시간초과가 나왔다. 

# import sys
# n, l = map(int,sys.stdin.readline().split())
# new = []
# for i in range(n):
#     new.append(list(map(int,sys.stdin.readline().split())))
# new.sort()

# answer = 1
# result = 0
# new_idx = 0

# while new_idx < len(new):
#     if new[new_idx][0] <= answer < new[new_idx][1]:
#         answer+=l
#         result+=1
#         continue
#     if new[new_idx][1] <= answer:
#         new_idx+=1
#         continue
#     answer+=1
# print(result)

# 두번째 풀이 
# 그리디 알고리즘 

import sys
n, l = map(int,sys.stdin.readline().split())
new = []
for i in range(n):
    new.append(list(map(int,sys.stdin.readline().split())))
new.sort()      # 웅덩이 정렬 

result = 0      # 필요한 널빤지 개수 갱신 
last = -1       # 웅덩이의 마지막 지점 
for start,end in new:
    if last < start :  # 널빤지로 한 웅덩이를 채웠는데 다음 웅덩이의 일부분도 채워지는 경우 
        answer = (end - start+l-1) // l     # 해당 웅덩이에 필요한 널빤지의 개수 
        result += answer
        last = l*answer+start       # 널빤지가 채워진 부분의 마지막값 저장 
    else:           # 하나의 널빤지가 하나의 해당 웅덩이만 채운경우 
        answer = (end - last+l-1) // l      # 이전에 저장한 last값 부터 end까지의 범위로 널빤지를 사용한다.  
        result += answer
        last = l*answer+last
print(result)
