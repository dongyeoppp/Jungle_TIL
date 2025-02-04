# 좋은 단어   
# 스택을 사용하여 풀이 함
import sys

input = sys.stdin.readline

n = int(input())
result = 0
for i in range(n):
    answer = input().strip()
    stack = []
    for j in answer:
        if not stack or stack[-1] != j: 
            stack.append(j)
        # 선끼리 교차 하지 않고 쌍을 지을 수 있을 경우
        else:
            stack.pop()
    # 좋은 단어일 경우
    if not stack:
        result+=1
print(result)
