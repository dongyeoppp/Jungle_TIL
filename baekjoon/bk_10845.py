# 큐   

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

que = deque()
for i in range(n):
    answer = input().split()
    command = answer[0]
    if command == "push":
        que.append(int(answer[1]))
    elif command == "pop":
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif command == "size":
        print(len(que))
    elif command == "empty":
        if que:
            print(0)
        else:
            print(1)
    elif command == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif command == "back":
        if que:
            print(que[-1])
        else:
            print(-1)
