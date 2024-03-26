# 외판원 순회 2  

import sys
n = int(sys.stdin.readline())

# travel = []
# for i in range(n):
#     travel.append(list(map(int,sys.stdin.readline().split())))
travel = [[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]] 
for i in range(n):
    total = 0
    start  = i
    count2 = 0
    count1 = i
    visited = [False] * 4
    cnt = 0
    while cnt != n:
        if count1 != count2 and not visited[count2]:
            if cnt == n-1:
                total += travel[count1][start]
            else:
                total += travel[count1][count2]
                cnt += 1
                count1 = count2
                count2 = 0
                visited[count1] = True
        else :
            count2 +=1
    print(total)