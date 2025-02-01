# 제로
# 스택을 활용하여 풀이 함.
import sys  

input = sys.stdin.readline

k = int(input())

result = []
for i in range(k):
    answer = int(input())
    if answer == 0:
        result.pop()
        continue
    result.append(answer)
print(sum(result))
    
