# 잃어버린 괄호  

import sys
n = sys.stdin.readline().strip().split('-')     #'-' 를 기준으로 나눈 리스트를 만들었다.  
answer=[]
for i in n:
    add = 0
    if '+' in i:        # '+'연산자가 들어있는 요소는 '+'를 기준으로 다시 나눠주었다.   
        new = i.split('+')
        for j in new:       # '+'를 기준으로 나눈 리스트의 모든 요소를 더해서 answer리스트에 넣어주었다. 
            add+=int(j)
        answer.append(add)
    else:
        answer.append(int(i))       # '+' 연산자가 포함되어있지 않을 경우 int자료형으로 answer리스트에 넣어주었다.  
n = answer[0]   
for i in range(1,len(answer)):      # answer안에 있는 모든 값을 answer[0]에서 빼주었다.  
    n-=answer[i]
print(n)

# ex)
# 55-66+43-24+45   
# [55,66+43,24+45]
# answer= [55,109,69]  

