#부분 수열의 합  

# import sys
# from itertools import combinations
# n, m = map(int,sys.stdin.readline().split())
# arr = list(map(int,sys.stdin.readline().split()))

# count =0
# answer = 1
# while answer <= n:
#     new = list(combinations(arr,answer))
#     for i in range(len(new)):
#         result = 0
#         for j in range(len(new[0])):
#             result += new[i][j]
#         if result == m:
#             count+=1
#     answer+=1
# print(count)  


# combinations 안사용하고 다시 구현해보기 - 현재 미완료  
import sys
n, m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
answer = []
h = 1
while n > h:
    new = []
    for i in range(h):
        new.append(arr[i])
        for j in range(i+1,i+1+h):
            new.append(arr[j])
        answer.append(new)
    h+=1
print(answer)





