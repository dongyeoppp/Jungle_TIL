## 5주차 Red-Black Tree 및 알고리즘 문제 풀이 및 cs 개념

* 2024 - 04 -22 (36일차)    
#### AVL Tree   
* 이진 탐색 트리(BST)의 한 종류로 스스로 균형을 잡는 트리이다. (balance factor를 통해 균형 유지)   
* balance factor   
    * 임의의 노드 x에 대해서 BF(x) = 왼쪽 서브트리의 높이 - 오른쪽 서브트리의 높이   
    * AVL tree의 모든 노드들은 BF(x) 값이 1-,0,1 이다.   
* 최악의 경우에도 삽입/삭제/검색의 시간 복잡도는 O(log N)이다.    
* 엄격하게 균형을 유지하기 때문에 삽입/삭제 시 트리 균형을 확인하고 만약 균형이 깨졌다면 트리 구조를 재조정(바닥노드부터 루트 노드까지 높이를 다 계산해야 함)하기 때문에 이 때 시간이 많이 걸린다.   
* AVL 트리는 밸런스가 좀 더 엄격하게 유지되기 때문에 탐색에 유리하고(이론상으론 RB TREE와 시간복잡도는 O(log N)으로 같다) RB TREE는 밸런싱을 느슨하게 하기 때문에 AVL 트리에 비해 탐색엔 불리하지만 삽입, 삭제에 유리하다.  
* AVL 트리가 검색에 유리할 수 있지만 현실에서의 프로그램에서는 데이터 삽입, 삭제가 빈번하게 일어나므로 RB TREE가 주로 선택되어 사용된다.   

#### CS(Computer System)
* [Computer System 7장 링커](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week05/ComputerSystem1.md)    

#### 알고리즘 문제 풀이  
* 2253번 [점프](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week05/bk_2253.py)    
