# 수 정렬하기   
import sys
n = int(sys.stdin.readline())

num_list = []
for i in range(n):
    num = int(sys.stdin.readline())
    num_list.append(num)
new_num_list = sorted(num_list)         # sortd(리스트)를 통해 정렬된 리스트를 변수에 저장  
for i in new_num_list:
    print(i)

