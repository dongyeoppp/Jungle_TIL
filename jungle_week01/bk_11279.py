# 최대 힙

import sys
import heapq        # heapq 라이브러리 불러오기  기본적으로 최소힙이 구현되어 있다. 

n = int(sys.stdin.readline())
heap = []
for i in range(n):
    answer = int(sys.stdin.readline())
    if answer >0:
        heapq.heappush(heap,-answer)    # heappush를 사용하였다. 이때 값을 넣을 리스트 heap과 요소값 answer값을 전달한다.(최대 힙을 구현해야 하므로 answer에 -를 붙여준다)
    elif answer == 0:
        if not heap:    # 힙이 비어있을 경우 
            print(0)
        else:
            print(-1 * heapq.heappop(heap))     # heappop함수를 사용해 값을 뽑아낸다. 이때 다시 -1을 곱하면 최대값이 출력된다.  
    
    