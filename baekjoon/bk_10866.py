# 덱   
# 큐를 구현할 때와 마찬가지로 deque()를 사용하여 풀이 함 
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dequeue = deque()
for i in range(n):
    answer = input().split()
    order = answer[0]
    # insert를 통해 원하는 인덱스에 특정 값을 넣음 
    if order == "push_front":
        dequeue.insert(0,answer[1])
    elif order == "push_back":
        dequeue.append(answer[1])
    elif order == "pop_front":
        if dequeue:
            print(dequeue.popleft())
        else:
            print(-1)
    elif order == "pop_back":
        if dequeue:
            print(dequeue.pop())
        else:
            print(-1)
    elif order == "size":
        print(len(dequeue))
    elif order == "empty":
        if dequeue:
            print(0)
        else:
            print(1)
    elif order == "front":
        if dequeue:
            print(dequeue[0])
        else:
            print(-1)
    elif order == "back":
        if dequeue:
            print(dequeue[-1])
        else:
            print(-1)
