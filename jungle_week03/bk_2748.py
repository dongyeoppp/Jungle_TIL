# 피보나치 수 2

# 바텀 업 방식 
# 반복문을 사용하는 방식이며 상향식이라고 한다.  
import sys
n = int(sys.stdin.readline())
dp = [0]* 100   # 값을 저장해 놓을 리스트를 만들고 
dp[1] = 1
dp[2] = 1       # 1일때와 2일때 값을 미리 저장해놓는다.  
def fibo(x):
    for i in range(3,x+1):
        dp[i] = dp[i-2] + dp[i-1]       # 반복문의 범위를 정하고 dp에 값을 넣는다. 
    return dp[x]
print(fibo(n))  

# 탑 다운 방식  
# 재귀함수를 사용하는 방식이며 하향식이라고 한다.  
import sys
n = int(sys.stdin.readline())
dp = [0] * 100
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if dp[x] != 0 :
        return dp[x]            # dp에 0이 아닌 값일 경우(이미 더한 값이 들어가 있는 경우) return
    dp[x] = fibo(x-1) + fibo(x-2)       # dp에 값을 저장한다.  
    return dp[x]
print(fibo(n))