# 줄 세우기  
# 위상정렬을 사용하여 풀이한다.  
import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())

graph = [[] for i in range(n+1)]
indegree = [0] * (n+1)
for i in range(m):
    row,col = map(int,sys.stdin.readline().split())
    graph[row].append(col)              # direct graph 완성하기
    indegree[col] +=1     # 진입차수 리스트 만들기  

def sorting():          # 위상정렬 구현  
    result=[]
    que = deque()           # 큐 선언  
    for i in range(1,n+1):
        if indegree[i] == 0:        # 진입차수가 0일 경우의 index값 que에 넣기  
            que.append(i)
    while que:          # que가 빌때까지 반복  
        removed = que.popleft()
        result.append(removed)
        for i in graph[removed]:        # 제거된 노드와 인접한 진입차수 제거  
            indegree[i] -=1
            if indegree[i] == 0:        # 차수가 0인 노드읭 인덱스 다시 que에 추가  
                que.append(i)
    print(*result)     
sorting()


    

