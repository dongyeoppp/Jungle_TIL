# 수리공 항승  

import sys

n,l = map(int,sys.stdin.readline().split())

water = list(map(int,sys.stdin.readline().split()))

water.sort()
answer = []
count =0
for i in water:
    if i not in answer:
        count+=1
        for j in range(l):
            answer.append(i+j)
print(count)