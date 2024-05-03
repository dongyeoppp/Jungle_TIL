# 옥상 정원 꾸미기  
# 스택을 이용하여 풀이하였다. 해당 건물에서 볼 수 있는 옥상 수를 세지 않고, 해당 건물을 볼 수 있는 옥상 수를 계산하였다.  
import sys

n = int(sys.stdin.readline())
new = []

for i in range(n):
    new.append(int(sys.stdin.readline()))
stack =[]
count = 0
for i in new:
    while stack and stack[-1] <= i:
        stack.pop()
    stack.append(i)
    count += len(stack) - 1         # stack의 해당 길이를 check
print(count)