# 순위
# bfs를 사용하여 풀이

from collections import deque
def solution(n, results):
    graph1 = [[] for i in range(n+1)]
    graph2 = [[] for i in range(n+1)]
    # 그래프를 두개 만들어 순위 체크 
    for i in results:
        graph1[i[0]].append(i[1])
        graph2[i[1]].append(i[0])
    def bfs(graph,start):
        que = deque()
        que.append(start)
        visited = [False] * (n+1)
        visited[start] = True
        count = 0
        while que:
            node = que.popleft()
            for i in graph[node]:
                if not visited[i]:
                    que.append(i)
                    visited[i] = True
                    count+=1
        return count
    cnt = 0
    for i in range(1,n+1):
        # i선수 보다 순위가 낮은 선수의 수 + i보다 순위가 높은 선수의 수 >= n-1 이면 i선수의 순위를 알 수 있다.
        if bfs(graph1,i) + bfs(graph2,i) >= n-1:
            cnt+=1
    return cnt