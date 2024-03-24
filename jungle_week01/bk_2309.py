# 일곱 난쟁이  

import sys
from itertools import combinations

num_list = []
for i in range(9):
    num_list.append(int(sys.stdin.readline()))
new = list(combinations(num_list,7))

for i in new:
    if sum(i) == 100:
        new_list = list(i)
        break
new_list.sort()
for j in new_list:
    print(j)


# num_list = []
# for i in range(9):
#     num_list.append(int(sys.stdin.readline()))

# num_list.sort()
# a = sum(num_list)
# for i in range(9):
#     for j in range(i+1,9):
#         if a - num_list[i] - num_list[j] == 100:
#             for h in range(9):
#                 if h == i or h == j:
#                     continue
#                 else:
#                     print(num_list[h])
#             break

