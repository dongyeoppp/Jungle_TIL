#  # z
# import sys  

# n,r,c = map(int,sys.stdin.readline().split())

# new = [[0]* 2**n for i in range(2**n)]
# row = 0 
# col = 0
# count = 0
# def recur(row,col):
#     if 
#         col+=2**n//2
#     elif i ==0:
#         row+=2**n//2
#     elif i ==0:
#         col+=2**n//2
#     elif i ==0:
#         col+=2**n//2
# re(0,0)

        
# for i in new:
#     print(i)    

# 점프  
import sys 

n, m = map(int,sys.stdin.readline().split())
dp = [0] * (n+1)
dp_check = [True] * (n+1)
for i in range(m):
    a = int(sys.stdin.readline())
    dp_check[a] = False

dp[0] = 0
dp[1] = 0
dp[2] = 1
start = 2
jump = 2
while start < n:
    check = 0
    for i in range(start+jump,start+jump-3,-1):
        if start>=i:
            check=-1
            exit()
        if i<=n and dp_check[i] == True:
            dp[i] = dp[start]+1
            check+=1
            start = i
            jump+=1
            break
        jump-=1
    if check==0:
        check=-1
        break
if check == -1:
    print(check)
else:
    print(dp[-1])







