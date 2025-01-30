# # 두 수의 합
# # 초기에 deque를 사용하여 풀이하였는데 시간초과가 발생 함

# import sys
# from collections import deque

# input = sys.stdin.readline

# n = int(input())
# new = list(map(int,input().split()))
# x = int(input())

# que = deque(new)
# cnt = 0
# while que:
#     removed = que.popleft()
#     if removed >= x:
#         continue
#     else:
#         num = x - removed
#         # 매번 in 연산을 실행하여 최악의 경우 O(n**2)의 시간복잡도를 가질 수 있음
#         if num in que:
#             cnt +=1
# print(cnt)

# 정렬 후 투포인터 사용하여 풀이 
import sys

input = sys.stdin.readline

n = int(input())
new = list(map(int,input().split()))
x = int(input())

new.sort()

start = 0
end = n-1
count = 0
while start < end:
    # x 가 두 수의 합 보다 클 경우
    if x > new[start] + new[end]:
        start += 1
    # x 가 두 수의 합 보다 작을 경우 
    elif x < new[start] + new[end]:
        end -= 1
    # x와 두 수의 합이 같을 경우 
    else:
        count +=1
        start += 1
        end -= 1 
print(count)
