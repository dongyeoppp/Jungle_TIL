# 트럭   
# 큐를 사용하여 풀이하였다.  
import sys
from collections import deque
n, w, l = map(int,sys.stdin.readline().split())

truck = list(map(int,sys.stdin.readline().split()))

que = deque()

for i in range(w):      # 초기 que에 w 만큼 0을 채운다. 
    que.append(0)

truck_idx = 0       # truck리스트의 인덱스 값을 갱신 
time =0             # 시간 갱신 
while que:
    if truck_idx < len(truck):      # truck_idx값이 truck 리스트의 길이보다 작다면 더 이상 들어갈 truck이 없으므로 pop만 수행한다. 
        removed =que.popleft()
        l+=removed      # 다리에 올라갈 수 있는 트럭의 무게 갱신 
        if l - truck[truck_idx] >= 0:       # l이 0보다 같거나 클 경우 다른 트럭이 올라갈 수 있다.  
            que.append(truck[truck_idx])
            l -= truck[truck_idx]
            truck_idx+=1
            time+=1
        else:                              #  l이 0 보다 작을 경우 트럭이 올라갈 수 없다. 
            que.append(0)
            time+=1
    else:
        que.popleft()
        time+=1
print(time)