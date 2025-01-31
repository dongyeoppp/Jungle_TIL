# # 백준 1158 
# # 요세푸스 문제
# # 큐를 사용하여 풀이 함. 시간이 많이 걸림 
# import sys
# from collections import deque

# input = sys.stdin.readline

# n, k = map(int, input().split())

# que = deque(i for i in range(1,n+1))
# count = 0
# result = []
# while que:
#     removed = que.popleft()
#     count+=1
#     if count == k:
#         result.append(removed)
#         count = 0
#         continue
#     que.append(removed)

# answer = "<"
# for i in range(n-1):
#     answer += str(result[i])+", "
# answer+=str(result[-1])+">"
# print(answer)

# 시간 단축 풀이 
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

new = [i for i in range(1,n+1)]
count = 0
result = []
for i in range(n):
    count += k-1
    # 특정 위치 인덱스에 있는 값을 제거하며 result에 추가 
    if count >= len(new):
        count = count % len(new)
    result.append(str(new.pop(count)))

# sep="": 출력할 값들 사이의 기본 구분자(default:" ",공백)을 ""(빈 문자열)로 변경 
print("<",", ".join(result),">",sep="")
