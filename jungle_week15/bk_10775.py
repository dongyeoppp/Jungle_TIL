# 공항
# 그리디하게 문제 풀이
# 첫번째 풀이 시간 초과 발생
# import sys

# input = sys.stdin.readline

# g = int(input())

# p = int(input())

# airplane = []
# for i in range(p):
#     airplane.append(int(input()))

# check = [False]*(g+1)

# count = 0
# for i in airplane:
#     answer = False
#     for j in range(i,0,-1):
#         if not check[j]:
#             check[j] = True
#             answer = True
#             count +=1
#             break
#     if not answer:
#         break
# print(count)

# 두번째 풀이 
# union,find 사용 하여 풀이 

import sys

input = sys.stdin.readline

g = int(input())

p = int(input())

airplane = []
for i in range(p):
    airplane.append(int(input()))

gate = []
for i in range(0,g+1):
    gate.append(i)

# 재귀를 통해 부모 값을 찾기 
def find(x):
    if x != gate[x]:
        gate[x] = find(gate[x])
    return gate[x]

# 현재 값과 그 전값을 통합하기 
def union(x,y):
    a = find(x)
    b = find(y)
    if a > b:
        gate[a] = b
    else:
        gate[b] = a

count = 0
for i in airplane:
    answer = find(i)
    # answer가 0일 경우 더 이상 도킹할 게이트가 없음을 의미 
    if answer == 0:
        break
    union(answer,answer-1)
    count+=1
print(count)