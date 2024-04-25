# 에디터   
# stack을 사용하여 풀이하였다. 
import sys

s = sys.stdin.readline().strip()
m = int(sys.stdin.readline())
stack = []      # stack을 두개 생성
rest = []
for i in range(len(s)):
    stack.append(s[i])

for i in range(m):
    new = list(sys.stdin.readline().strip())
    if len(new)>1:
        stack.append(new[2])
    else:
        if new[0] == 'L':
            if stack != []:
                removed = stack.pop()
                rest.append(removed)
        elif new[0] == 'D':
            if rest != []:
                removed = rest.pop()
                stack.append(removed)
        elif new[0] == 'B':
            if stack != []:
                stack.pop()
result = "".join(stack+list(reversed(rest)))        # 원래 for문을 써서 stack에 있는 문자와 rest에 있는 문자를 합쳤는데 시간초과가 나와 수정하였다.
print(result)                                     

# for i in stack:
#     sys.stdout.write(i)
# for j in range(len(rest)):
#     sys.stdout.write(rest.pop())              # sys.stdout.layout을 이용하면 출력을 합쳐서 빠르게 출력할 수 있다고 한다. (print보다 빠르다)
