## 알고리즘 키워드 공부 + cs 개념   
* 2024 - 04 -01 (15일차)   

#### 다익스트라 알고리즘 구현  
* 힙을 사용한 다익스트라 알고리즘 코드 구현    
    ```
    import heapq
    inf = float("inf")

    n = 5
    m =6
    k =1 
    graph = [[], [(1, 5), (1, 2), (3, 3)], [(1, 1), (1, 3), (5, 4)], [(3, 1), (1, 2), (2, 4)], [(5, 2), (2, 3)], [(1, 1)]]
    def dijkstra(start):
        distance = [inf] * (n + 1)
        distance[start] = 0
        que = [(0, start)]

        while que:
            dist, node = heapq.heappop(que)
            if dist > distance[node]:       # dist 값이 distance 리스트에 저장된 값보다 클 경우 방문한 노드로 생각하고 continue
                continue
            for redist, renode in graph[node]:
                if distance[node] + redist < distance[renode]:      # 처음 노드에서 현재 node까지 오는 최단 거리 = distance[node] + 현재 노드에서 다음 노드로 가는 거리 <
                                                                        # 처음노드에서 다음 노드로 가는 거리 (=distance에 저장되어있는거리)
                    distance[renode] = distance[node] + redist
                    heapq.heappush(que,(distance[renode],renode))

        return distance
    print(dijkstra(k))
    # [inf, 0, 1, 2, 4, 1]
    ```   

#### 플로이드 와샬 알고리즘   

* 다익스트라 알고리즘  
    * 하나의 정점에서 출발했을 때 다른 모든 정점으로의 최단 경로를 구하는 알고리즘   
    * 가장 적은 비용을 하나씩 선택   

* 플로이드 와샬  
    * '모든 정점'에서 '모든 정점'으로의 최단 경로를 구하는 알고리즘  
    * 기본적으로 '거쳐가는 정점'을 기준으로 알고리즘을 수행   
    * "x노드에서 y노드로 가는 최소 비용"과 "x에서 노드 1로 가는 비용 + 노드 1에서 y 로 가는 비용"을 비교한다.   
    * 플로이드 와샬 알고리즘 코드 구현   
        ```
        # 플로이드 와샬 알고리즘   

        import sys
        inf  = float("inf")  
        n = 4
        graph = [[0,0,0,0,0],[0,0,2,inf,4],[0,2,0,inf,5],[0,3,inf,0,inf],[0,inf,2,1,0]]             # 행렬로 그래프를 나타낸다.  

        def floyd_warshall():
            for k in range(1,n+1):
                for i in range(1,n+1):
                    for j in range(1,n+1):
                        graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])      # k는 기준으로 잡은 노드를 의미한다. 기준으로 잡은노드를 거쳐 가는 경로가 더 짧을 경우 그래프의 값을 재조정한다.  
                                                                                    # 2를 기준으로 [1][3]값을 확인할때 1에서 3으로 가는 경로 보다 2를 거쳐 1->2->3으로 가는 경로가 더 짧으면 값을 조정한다.  
        floyd_warshall()

        for i in graph[1:]:
            print(i[1:])
        ```   
#### ComputerSystem(~1.9)  
* computersystem 책을 참고하여 정리하였다. [cs(1.5~1.9)]/(https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week02/ComputerSystem2.md)

#### 알고리즘 문제풀이   
* 18352번 [특정 거리의 도시 찾기](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week02/bk_18352.py)   
* 1916번 [최소 비용 구하기](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week02/bk_1916.py)   


