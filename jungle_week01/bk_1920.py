# 수 찾기 

import sys

n = int(sys.stdin.readline())

num_list = set(map(int,sys.stdin.readline().split()))       # 리스트로 받았는데 시간 초과 오류가 나서 set으로 받아서 처리했다.

m = int(sys.stdin.readline())
num_list2 = list(map(int,sys.stdin.readline().split()))
for i in num_list2:
   if i in num_list:
    print("1")
   else:
    print("0")