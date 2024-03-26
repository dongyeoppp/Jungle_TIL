# 탑 

import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

count = n-1

answer =""
for i in range(n-1,0,-1):
    count = i-1
    while count >= 0:
        print(count,i)
        if arr[i] <= arr[count]:
            answer += f"{count+1} "
            break
        else:
            count-=1 
            if count <=0:
                answer += "0 "
                break
answer+="0"
print(answer[::-1])

