# 도넛과 막대 그래프
from collections import deque
def solution(edges):
    answer = 0
    new = set()
    start = 0
    # answer = 노드의 개수
    for i in edges:
        if max(i) > answer:
            answer = max(i)
        new.add(i[1])

    graph = [[] for i in range(answer+1)]
    for i in edges:
        graph[i[0]].append(i[1])
        
    # start = 새로운 정점 
    for i in range(1,answer+1):
        # 들어오는 간선이 없고 나가는 간선이 두 개 이상이어야 함
        if i not in new and len(graph[i])>=2:
            start = i   

    # bfs함수 안에서 visited 배열을 만들 경우 bfs를 실행 할때마다 visited배열이 만들어지므로 함수 밖으로 뺐다. (시간초과 해결)
    visited = [False] * (answer+1)
    def bfs(start):
        que = deque()
        que.append(start)
        visited[start] = True
        edge = 0
        nodes = 0
        while que:
            node = que.popleft()
            # 노드의 개수와 간선의 개수를 체크
            nodes+=1
            edge += len(graph[node])
            for i in graph[node]:
                if not visited[i]:
                    que.append(i)
                    visited[i] = True
        return nodes, edge
    # 생성한 정점의 번호 , 도넛 모양 그래프의 수, 막대 모양 그래프의 수 , 8자 모양 그래프의 수
    result = [start,0,0,0]
    
    for i in graph[start]:
        nodes, edge = bfs(i)
        # 노드와 간선의 개수 같을 경우 = 도넛 모양 그래프의 수 + 1 
        if nodes == edge :
            result[1]+=1
        # 노드의 개수가 간선의 개수보다 1 적을 경우 = 막대 모양 그래프의 수 + 1 
        elif nodes-1 == edge:
            result[2] +=1
        # 노드의 개수가 간선의 개수보다 1 많을 경우 = 8자 모양 그래프의 수 + 1 
        elif nodes +1 == edge:
            result[3]+=1
    return result
        
        
