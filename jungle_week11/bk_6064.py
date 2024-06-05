# 카잉 달력
# count를 1씩 증가시키며 풀이하였더니 시간초과가 나왔다.  
# import sys 

# t = int(sys.stdin.readline())

# for i in range(t):
#     m,n,x,y=map(int,sys.stdin.readline().split())
#     x1 = 1
#     y1 = 1
#     count = 1
#     while True:
#         if x1 == x and y1 == y:
#             print(count)
#             break
#         if x1 == m and y1 ==n:
#             print(-1)
#             break
#         if x1 >= m:
#             x1 =1
#         else:
#             x1+=1
#         if y1 >= n:
#             y1 = 1
#         else:
#             y1+=1
#         count+=1

# count=x를 m만큼 계속 더해주며 찾았다. 
import sys 

t = int(sys.stdin.readline())

def gcd(n,m):       # 최대 공약수 구하기 
    if m == 0:
        return n
    else:
        return gcd(m,n%m)

for i in range(t):
    m,n,x,y=map(int,sys.stdin.readline().split())
    count = x
    check = False
    maxi = gcd(n,m) * (n // gcd(n,m)) * (m // gcd(n,m))     # 최소 공배수 구하기 
    while  maxi >= count:       # 최소 공배수까지 구하기  
        if (count-y) % n == 0:
            print(count)
            check = True
            break
        count+=m
    if not check:
        print(-1)