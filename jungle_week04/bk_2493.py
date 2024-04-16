# 탑  
# 스택을 사용해서 구현하였다.   
import sys 
n = int(sys.stdin.readline())

tower = list(map(int,sys.stdin.readline().split()))  
stack=[]
result = [0] *n

for i in range(n):
    while stack and tower[stack[-1]]< tower[i]:             # 더 큰 값을 만났을 경우 pop , 해당 인덱스의 타워가 가장 크다면 result의 해당 인덱스는 0
        stack.pop()
    if stack:
        result[i]= stack[-1]+1
    stack.append(i)

print(" ".join(map(str,result)))        # 공백을 기준으로 나눠 result 리스트를 문자열로 