# 잃어버린 괄호  

import sys
n = sys.stdin.readline().strip().split('-')
answer=[]
for i in n:
    add = 0
    if '+' in i:
        new = i.split('+')
        for j in new:
            add+=int(j)
        answer.append(add)
    else:
        answer.append(int(i))
n = answer[0]
for i in range(1,len(answer)):
    n-=answer[i]
print(n)


