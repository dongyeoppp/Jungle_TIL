# 큐 2

# stack과 동일하게 코드를 짰다가 시간초과를 맞았다. 
# 리스트에서 pop(0)을 실행하면 한자리씩 앞으로 옮기는 과정을 거쳐야 하기 때문에 시간복잡도가 올라가서 시간복잡도가 O(N)이다.
 
import sys
from collections import deque       # deque 모듈을 불러와 사용하였다.

n = int(sys.stdin.readline())
arr = deque()       # arr를 deque()로 선언
def push(arr,x):
    arr.append(x)
def pop(arr):
    if not arr :    # deque가 비어있을 경우 arr = False
         print(-1)
    else:
        removed = arr.popleft()     # 여기서 pop(0)을 popleft()로 바꿔줬더니 통과하였다.  
        print(removed)
def size(arr):
     print(len(arr))
def empty(arr):
    if not arr :
         print(1)
    else :
         print(0)
def front(arr):
    if not arr :
         print(-1)
    else:
         print(arr[0])
def back(arr):
    if not arr :
         print(-1)
    else:
         print(arr[-1])

result =[]
for i in range(n):
    answer = sys.stdin.readline().strip()
    if "push" in answer:
        new = int(answer.split(" ")[1])
        push(arr, new)
    elif "front" == answer:
       front(arr)
    elif "back" == answer:
        back(arr)
    elif "size" == answer:
        size(arr)
    elif "empty" == answer:
        empty(arr)
    elif "pop" == answer:
       pop(arr)
