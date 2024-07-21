# 시리얼 번호 

import sys

n = int(sys.stdin.readline())
number = ['1','2','3','4','5','6','7','8','9']
arr = []
for i in range(n):
    arr.append(sys.stdin.readline().strip())
arr = sorted(arr, key=lambda x :(len(x),sum(int(ch) for ch in x if ch in number),x))        # 1. 길이 순 정렬, 2. 숫자의 합이 작은 순으로 정렬 3.사전순으로 정렬 
for i in arr:
    print(i)