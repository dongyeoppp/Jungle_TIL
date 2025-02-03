# 카드 2   
# 큐를 사용하여 풀이 함
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

que = deque(i for i in range(1,n+1))
# 카드가 한 장 남을 때까지 while문 반복
while len(que) > 1:
    que.popleft()
    removed = que.popleft()
    que.append(removed)
print(que[0])