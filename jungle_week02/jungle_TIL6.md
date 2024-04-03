## 알고리즘 문제 풀이, 퀴즈 리뷰   
* 2024 - 04 -02 (16일차)   

#### quiw review  

* 캐시 메모리를 사용할 때 시스템의 성능이 향상되는 이유(지역성)    
    * 지역성 : 프로그램이 메모리를 접근할 때 특정 부분을 집중적으로 사용하는 경향   
        * 시간적 지역성(Temporal Locality) : 한 번 접근된 데이터는 가까운 미래에 다시 접근될 가능성이 높다는 원리이다. (루프 내에서 반복적으로 사용되는 변수는 시간적 지역성의 좋은 예이다.)
        * 공간적 지역성(Spatial Locality) : 메모리에 특정 주소에 접근한 후, 그 주변 주소에 있는 데이터에 접근될 가능성이 높다는 원리이다. (이는 배열이나 연속적인 메모리 블록에 접근할 때 종종 발생한다.)    
    * 캐시 메모리는 이러한 지역성 원리를 활용하여 자주 사용되거나 연속적으로 사용될 가능성이 높은 데이터를 미리 캐시에 저장한다. 이로 인해 cpu는 필요한 데이터를 캐시에서 빠르게 찾을 수 있다.   

* bfs, dfs 구현 
    * BFS   
        ```
        def BFS(graph,start):
            visited = []
            que = deque()
            que.append(start)
            while que:
                removed = que.popleft()
                visited.append(removed)
                for i in graph[removed]:
                    if i not in visited:
                        que.append(i)

            return visited
        ```   
    * DFS  
        ```
        def DFS(graph,start):
            visited = []
            stack = []
            stack.append(start)
            while stack:
                removed = stack.pop()
                visited.append(removed)
                for i in graph[removed]:
                    if i not in visited:
                        stack.append(i)
            return visited
        ```   
* 프로세스와 쓰레드의 차이   
    * 프로세스 : 독립적으로 실행되는 프로그램의 인스턴스로, 자체적인 주소 공간, 메모리, 데이터 스택 및 다른 시스템 자원을 갖는다.  
    * 쓰레드 : 프로세스 내부의 실행 흐름 단위로, 프로세스의 자원과 주소 공간을 공유하면서 실행된다.  
    * 프로세스는 독립적인 메모리 공간과 시스템 자원을 가지지만, 쓰레드는 데이터 및 시스템 자원을 공유한다.   
    * 프로세스 간 자원 공유는 IPC 메커니즘을 통해 이루어진다.  
        * IPC(Inter-Process Communication) : 독립적인 공간을 가지는 프로세스 간 통신에 사용되는 기법이다. (프로세스들 사이에 서로 데이터를 주고 받을 수 있다.)   

* b-tree 성능  
    * b-tree 인덱스를 사용할 경우 시간복잡도는 O(logN)이다. 여기서 N은 데이터 베이스 내의 레코드(데이터메이스 내에서의 개별 항목) 수이다.   
    * b-tree 구조는 균형 이진 트리와 유사하므로 데이터를 효율적으로 검색할 수 있다.  
    * b-tree 인덱스를 사용하지 않을 경우 선형 검색(순차검색이라고도 하며, 데이터가 모인 집함의 처음부터 끝까지 하나씩 순서대로 비교하며 원하는 값을 찾아내는 알고리즘)을 수행해야 하므로 검색 시간 복잡도는 O(N)이 된다. 따라서, 데이터 양이 많을수록 b-tree 인덱스를 사용하는 것이 성능 면에서 훨씬 유리하다.   

#### 알고리즘 문제 풀이  

* 21606번 [아침산책](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week02/bk_21606.py)   
* 14888번 [연산자 끼워넣기](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week02/bk_14888.py)   

  
