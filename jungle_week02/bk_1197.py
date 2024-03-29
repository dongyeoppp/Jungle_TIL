# 최소 스패닝 트리

# 최소 스패닝 트리란 주어진 그래프의 모든 정점을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.  
# 사이클이 없고 간선의 개수는 노드의 개수-1 개이다.   
# 최소 신장 트리에 대한 키워드 공부가 필요하다.  

import sys
v,e = map(int,sys.stdin.readline().split())

arr = [[0] *v for i in range(v)]
for i in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    arr[a-1][b-1] = c
    arr[b-1][a-1] = c

result = []  # 합한 값들을 추가 
visited = [0]*v
answer = 0
def new(k):
    global answer
    visited[k] = 1
    for i in range(v):
        if k!=i:
            answer += arr[k][i]
            visited[i] = 1
            now =i
            break
    if 0 not in visited:
        return answer
    new(now)
new(0)













   
    








    