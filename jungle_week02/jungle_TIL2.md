## 2주차 알고리즘 문제풀이 및 키워드 정리  
#### 위상정렬  
* 위상정렬 알고리즘  
```
import sys
# from collections import deque     # queue라이브러리를 사용하면 더 효과적이다.  

v, e = map(int, sys.stdin.readline().split())

indegree = [0] * (v + 1)  # 모든 노드의 진입 차수 0으로 초기화  (진입차수란 특정노드로 들어오는 간선의 개수이다.)
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)      # 해당 인덱스 노드에 진입하는 노드 추가  # [[], [2, 5], [3, 6], [4], [7], [6], [4], []]
    indegree[b] += 1        # b인덱스에 해당하는 진입차수 +1        # [0, 0, 1, 1, 2, 1, 2, 1]

def topology_sort():
    result = []
    queue = []
    #q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    for i in range(1, v + 1):
        if indegree[i] == 0:
            queue.append(i)     # 진입차수가 0인 인덱스가 시작지점이 된다.  queue리스트에 해당인덱스 추가  

    while queue:                # queue에 아무것도 들어지않고 비어있게 될때 까지   
        now = queue.pop(0)      # queue에 제일 먼저 들어온 값 pop
        #  now = q.popleft()
        result.append(now)      # 해당 인덱스를 result에 추가  
        for i in graph[now]:    # now=1일때 1과 연결되어있는 노드가 들어있는 리스트에서 해당노드의 진입차수에 -1을 해준다. graph[now] =[2,5]라면 2,5인덱스의 진입차수를 -1한다.
            indegree[i] -= 1    
            if indegree[i] == 0:        # 진입차수가 0이되면 바로 queue리스트에 넣어준다.  
                queue.append(i)

    for node in result:
        print(node, end=" ")

topology_sort()
```   

#### 알고리즘 문제 풀이   

* ```sys.setrecursionlimit(10 ** 6)```: 파이썬은 기본으로 최대 1000번의 재귀함수를 허용하는데 그 최대값을 늘려줄 수 있다.  
* ```arr = [[0] *v for i in range(v)]``` : 이중 배열 0으로 초기화 한다.   
* 리스트 문 print하기 꿀팁  
    ```
    result = [1,2,3,4]
    print(*reuslt)
    # 1 2 3 4 -> 괄호 제거, 요소 사이에 공백넣어 출력  
    ```

* 1260번 [DFS와 BFS](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week02/bk_1260.py)  
* 1991번 [트리 순회](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week02/bk_1991.py)   
* 5639번 [이진 검색 트리](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week02/bk_5639.py)  
* 11724번 [연결 요소의 개수](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week02/bk_11724.py)   
* 2252번 [줄 세우기](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week02/bk_2252.py)   

