# 가장 긴 증가하는 부분 수열  
import sys

n = int(sys.stdin.readline())  

graph = list(map(int,sys.stdin.readline().split()))

dp =[1]*(n)             # dp테이블 1로 초기화    
for i in range(1,n):        
    for j in range(0,i):
        if graph[i] > graph[j]:      # graph[i] 값이 graph[j]보다 클 경우에만 해당 인덱스의 dp테이블에 들어있는 값을 비교한다.   
            dp[i] = max(dp[i],dp[j]+1)      # 위의 경우를 만족하는 dp[0] - dp[i-1] 사이의 값 중 가장 큰 값에 1을 더해 dp[i]를 업데이트한다.   
print(max(dp))      # dp 리스트에 최댓값이 가장 긴 부분 수열의 길이가 된다.   
