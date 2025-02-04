# 괄호
# 스택을 활용하여 풀이  
import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    answer = input().strip()
    stack = []
    for i in answer:
        if i == "(":
            stack.append(i)
        elif i == ")":
            # 괄호 한쌍을 만들었을 경우 
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
                break
    if stack:
        print("NO")
    else:
        print("YES")