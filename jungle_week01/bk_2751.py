# 2751번  수 정렬하기 2
import sys
n = int(sys.stdin.readline())
num_list = []
for i in range(n):  
    num_list.append(int(sys.stdin.readline()))
num_list.sort()         # 리스트.sort() -> 해당 리스트를 오름차순으로 정렬 
for i in range(n):
    print(num_list[i])