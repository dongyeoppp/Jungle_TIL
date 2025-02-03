# 회전하는 큐
# deque를 사용하여 풀이하였다. 
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
answer = list(map(int,input().split()))
idx = 0
que = deque(i for i in range(1,n+1))
count = 0
while idx < m:
    for i in range(len(que)):
        # 원소의 인덱스 위치 = i , 찾아야하는 원소 answer[idx]
        if que[i] == answer[idx]:
            # 2번 연산을 해야 할 경우 
            if len(que) - i >= i:
                # 뽑아내려는 원소가 0번째 인덱스에 올때까지 반복문 반복  
                while que[0] != answer[idx]:
                    removed = que.popleft()
                    que.append(removed)
                    count+=1
            # 3번 연산을 해야 할 경우 
            else:
                while que[0] != answer[idx]:
                    removed = que.pop()
                    que.insert(0,removed)
                    count+=1
            # 뽑아내려는 원소가 첫번째 원소가 되었을 때 
            que.popleft()
            idx+=1
            break
print(count)
