# 색종이 만들기 

import sys

n = int(sys.stdin.readline())
num_list = []
for i in range(n):
    num_list.append(list((map(int,sys.stdin.readline().split()))))

count = 0 
while n>1:
    n = n // 2
    new1 = []
    new2 = []
    for i in range(n):
        new1.append(num_list[i][:n])
        new2.append(num_list[i][n:])
    for j in range(n-1):
        if new1[j] != new1[j+1]:
            break
        else:
            count +=1
    for j in range(n-1):
        if new2[j] != new2[j+1]:
            break
        else:
            count +=1

    new = []


