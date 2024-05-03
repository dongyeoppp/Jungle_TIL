# A -> B
# top-down 방식으로 풀이하였다.  
# 
import sys

a, b = map(int,sys.stdin.readline().split())
count = 1
while b >= a:
    if a == b:
        break
    if str(b)[-1] == '1':       # 일의 자리가 1일 경우  
        new = str(b)[0:len(str(b))-1]
        b = int(new)
        count +=1
    elif b % 2 == 0:        # 일의 자리가 짝수일 경우  
        b = b // 2
        count+=1
    else:           # 일의 자리가 1이 아닌 홀수일 경우 
        break
if a == b:
    print(count)
else:
    print(-1)

# dfs 재귀를 사용한 bottom-up방식을 사용하였다.  
# import sys

# a, b = map(int,sys.stdin.readline().split())
# inf = float('inf') 
# def dfs(a,count,b):
#     if a > b:               # b를 만들 수 없는 경우 
#         return inf
#     elif a == b:
#         return count
#     else:
#         return min(dfs(a*2,count+1,b),dfs(a*10+1,count+1,b))        # 최솟값을 구하는 것이므로 min을 사용  
# result= dfs(a,0,b)
# if result == inf:
#     print(-1)
# else:
#     print(result+1)