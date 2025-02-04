# 괄호의 값
# 스택을 활용하여 풀이 함 .. 오래 걸림 !!
import sys

input = sys.stdin.readline

answer = input().strip()
stack = []
result = 0
ans = 1
# 이전 괄호를 save에 저장 
save = ""
for i in answer:
    if i == "(" or i == "[":
        stack.append(i)
        if i == "(":
            ans *= 2
        elif i == "[":
            ans *= 3
    else:
        if stack and stack[-1] == "(" and i == ")":
            stack.pop()
            # "()" 가 나올 경우 
            if save == "(":
                result += ans
            # 스택에서 "(" pop하며 ans 값 갱신  
            ans = ans // 2
        elif stack and stack[-1] == "[" and i == "]":
            removed = stack.pop()
            # "[]" 가 나올 경우 
            if save == "[":
                result += ans
            # 스택에서 "]" pop하며 ans 값 갱신 
            ans = ans // 3
        # 올바르지 못한 괄호열일 경우 
        else:
            stack.append(i)
            break
    save = i
if stack:
    print(0)
else:
    print(result)