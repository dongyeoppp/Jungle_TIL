# 키로거  
 
import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    key = input().strip()
    # 두 개의 스택을 사용하여 풀이 
    answer = []
    bucket = []
    consor = 0
    for j in key:
        if j == "<":
            if answer == []:
                continue
            bucket.append(answer.pop())
        elif j == ">":
            if bucket == []:
                continue
            answer.append(bucket.pop())
        elif j == "-":
            if answer == []:
                continue
            answer.pop()
        # 비밀 번호 글자 일 경우 
        else:
            answer.append(j)
    if bucket != []:
        while bucket:
            removed = bucket.pop()
            answer.append(removed)
    print("".join(answer))



##### 오답 풀이 #####
 
# 커서의 위치를 수시로 이동시킴
# 문자를 삭제하거나 추가할 경우 문자열을 슬라이싱하여 시간초과 발생 !!
# import sys

# input = sys.stdin.readline
# n = int(input())

# for i in range(n):
#     key = input().strip()
#     answer = ""
#     cunsor = 0
#     for i in key:
#         if i == "<":
#             if cunsor > 0:
#                 cunsor -= 1
#         elif i == ">":
#             if cunsor < len(answer):
#                 cunsor += 1
#         elif i == "-":
#             cunsor -= 1
#             answer = answer[:cunsor] + answer[cunsor+1:]
#         else:
#             answer = answer[:cunsor] + i + answer[cunsor:]
#             cunsor+=1
#     print(answer)


# 키로거  
# 슬라이싱 대신 리스트에 insert와 del을 사용하여 리스트의 특정 인덱스 위치의 값을 추가하거나 제거 -> 시간 초과 발생 
# import sys

# input = sys.stdin.readline
# n = int(input())

# for i in range(n):
#     key = input().strip()
#     answer = []
#     consor = 0
#     for j in key:
#         if j == "<":
#             if consor > 0:
#                 consor -= 1
#         elif j == ">":
#             if consor < len(answer):
#                 consor += 1
#         elif j == "-":
#             if consor <= 0:
#                 continue
#             consor -= 1
#             del answer[consor]
#         else:
#             answer.insert(consor,j)
#             consor+=1
#     print("".join(answer))