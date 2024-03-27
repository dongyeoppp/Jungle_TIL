# 뱀 


import sys

n = int(sys.stdin.readline())

k = int(sys.stdin.readline())
arr = []
for i in range(n):
    new = []
    for j in range(n):
        new.append(0)
    arr.append(new)

for i in range(k):
    arr1 = list(map(int,sys.stdin.readline().split()))
    arr[arr1[0]][arr1[1]] =1
l = int(sys.stdin.readline())

row = 0
col = 0
count = 0
answer = {}

for j in range(l):
    arr2 = list(map(str,sys.stdin.readline().split()))
    answer[arr2[0]] = arr2[1]


