# 쇠막대기   
# 스택을 활용하여 풀이 .. 풀이하는데 오래 걸림..!! 

import sys

input = sys.stdin.readline
answer = input().strip()

stack = []
result = 0
check = True
for i in answer:
    if i == "(":
        stack.append(i)
        check = True
    elif i == ")":
        stack.pop()
        # 레이저일 경우 레이저로 인해 잘리는 쇠 막대기 개수를 result에 더함 
        if check:
            result += len(stack)
            check = False
        # 레이저가 아닌 경우 -> 쇠 막대기 하나가 끝나는 지점이므로 자르고 남은 쇠막대기 + 1 
        else:
            result += 1
        
print(result)