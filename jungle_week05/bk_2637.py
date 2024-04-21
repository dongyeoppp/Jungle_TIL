# 장난감 조립  

# 위상정렬과 dp를 이용하여 풀이하였다.  
import sys 
from collections import deque

n = int(sys.stdin.readline())        
m = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]
indgree= [0]*(n+1)          # 노드의 차수를 저장할 리스트

for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[b].append((a,c))      # a에서 b로 도착  //c는 가중치  
    indgree[a] +=1          # 차수 증가  
      
dp = [[0]*(n+1) for i in range(n+1)]        # dp 테이블   
que = deque()   
for i in range(1,n+1):
    if indgree[i] == 0:
        dp[i][i] = 1
        que.append(i)           # indgree 리스트 안에 0이 아닌 값의 인덱스를 사용.  해당 인덱스 =i일때 dp[i][i]를 1로 설정한 이후 que에 넣어준다.  

while que:      # que에 값이 없을 때까지   
    removed = que.popleft()     
    for end,weight in graph[removed]:       # end는 도착지. weight는 가중치  
        for k in range(1,n+1):
            dp[end][k] += dp[removed][k] * weight       # end 행의 k번째 dp에 있던 기존 값에  removed행의 k번째 값에 가중치를 곱한 값을 더한다.
        indgree[end] -= 1       # 위의 for문이 종료된 후!! 목적지 노드에 차수 -1 
        if indgree[end] == 0:       # 이때 목적지 인덱스의 차수가 0이 되었다면 que에 해당 인덱스 값 넣기  
            que.append(end)

for i in range(1,n+1):      # 출력            
    if dp[n][i] != 0:
        print(i, dp[n][i])