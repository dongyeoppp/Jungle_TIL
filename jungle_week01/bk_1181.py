# 단어 정렬

# import sys            # 삽입 정렬을 사용해서 구현
# n = int(sys.stdin.readline())
# str= []
# base = ""
# for i in range(n):
#     str.append(sys.stdin.readline().strip())
# str_list = list(set(str))
# str_list.sort()
# for j in range(len(str_list)-1):
#     for i in range(len(str_list)-1-j):
#         if len(str_list[i]) > len(str_list[i+1]):
#             base = str_list[i+1] 
#             str_list[i+1] = str_list[i]
#             str_list[i] = base
# for i in str_list:
#     print(i)

import sys      # sort 매서드를 사용
n = int(sys.stdin.readline())
str_list = []
for i in range(n):
    str_list.append(sys.stdin.readline().strip())
new_list = list((set(str_list)))        # 중복제거
new_list.sort()     # 사전 순으로 정렬
new_list.sort(key=len)  # 단어 길이 순으로 정렬
for i in new_list:
    print(i)
