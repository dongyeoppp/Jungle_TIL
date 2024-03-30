# 최소 스패닝 트리

# 최소 스패닝 트리란 주어진 그래프의 모든 정점을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.  
# 사이클이 없고 간선의 개수는 노드의 개수-1 개이다.   
# 최소 신장 트리에 대한 키워드 공부가 필요하다.  

# kruskal 알고리즘을 사용하였다(union-find 함수 사용 )
# find 함수 : 변수로 parent 리스트와 노드를 받아서 부모 노드를 찾는다.  
# union 함수 : parent 리스트와 두개의 노드를 받아 비교한다.    
import sys

v, e = map(int,sys.stdin.readline().split())

graph = []

for i in range(e):
    a,b,cost = map(int,sys.stdin.readline().split())
    graph.append((cost,a,b))

parent = [i for i in range(v+1)]
graph.sort()        # 그래프를 cost비용 순서로 정렬하였다.      
def find(parent, x):        # find함수를 재귀적으로 구현  
    if parent[x] == x:
        return x
    parent[x] = find(parent,parent[x])     # 루트 노드를 찾고 parent 리스트를 업데이트해준다.  
    return parent[x]
def union(parent,a,b):          # 두 노드가 속한 집합을 합친다. parent리스트에서 두 인덱스의 값을 더 작은값으로 통일해준다.  
    rootA = find(parent,a)
    rootB = find(parent,b)
    if rootA > rootB:
        parent[rootA] = rootB
    else:
        parent[rootB] = rootA

result = 0
for i in graph:
    cost, a,b = i
    if find(parent,a) != find(parent,b):        # 루트 노드가 다를경우만 합쳐주어 사이클이 돌지않게 해준다.  
        union(parent,a,b)
        result +=cost   # union함수를 실행할 때마다 cost비용을 더해준다.  
print(result)












   
    








    