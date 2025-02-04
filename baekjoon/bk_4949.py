# 균형잡힌 세상   
# 스택을 사용하여 풀이 하였다. 
import sys

input = sys.stdin.readline
while True:
    stack = []
    answer = input()
    # while문 종료 / answer == "."일 경우 출력 초과가 발생하여 조건문을 수정 하였다. 
    if answer[0] == ".":
        break
    for i in answer:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            # 균형이 잡히지 않았을 경우 
            else:
                stack.append(i)
                break
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            # 균형이 잡히지 않았을 경우 
            else:
                stack.append(i)
                break
    if stack:
        print("no")
    else: 
        print("yes")

