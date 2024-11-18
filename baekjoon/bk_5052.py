# 전화번호 목록   

## 시간초과 
# import sys

# input = sys.stdin.readline

# t = int(input())

# for i in range(t):
#     n = int(input())
#     number = []
#     for j in range(n):
#         number.append(input().strip())
#     number.sort(key=lambda x:len(x))
#     check = True
#     for j in range(n):
#         length = len(number[j])
#         for k in range(j+1,n):
#             if number[j] == number[k][:length]:
#                 check = False
#                 break
#         if not check:
#             break
#     if not check:
#         print("NO")
#     else:
#         print("YES")


# dictionary 자료구조 활용 (tri)

# import sys

# input = sys.stdin.readline

# t = int(input())

# for i in range(t):
#     n = int(input())
#     number = {}
#     # 전화번호 dictionary에 추가 
#     for j in range(n):
#         number[input().strip()] = 1
#     check = True
#     for j in number:
#         answer = ""
#         for k in j:
#             answer += k
#             # 접두어가 dict에 존재하면서 자신이 아닌 경우 확인 
#             if answer in number and answer != j:
#                 check = False
#                 break
#         if not check:
#             break
#     if not check:
#         print("NO")
#     else:
#         print("YES")


import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    number = []
    for j in range(n):
        number.append(input().strip())
    number.sort()
    check = True
    for j in range(n-1):
        # 접두어가 같을 경우 확인
        if number[j] == number[j+1][:len(number[j])]:
            check = False
            break
    if not check:
        print("NO")
    else:
        print("YES")








        