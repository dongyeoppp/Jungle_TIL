# 스택  

import sys
n = int(sys.stdin.readline())
arr = []
def push(arr,x):
    arr.append(x)
def pop(arr):
    if arr == []:
        return -1
    else:
        removed = arr.pop()     # pop을 사용할 시 변수에 담으면 삭제되는 값이 저장된다.
        return removed
def size(arr):
    return len(arr)
def empty(arr):
    if arr == []:
        return 1
    else:
        return 0
def top(arr):
    if arr == []:
        return -1
    else:
        return arr[-1]
new = []
for i in range(n):
    order = sys.stdin.readline().strip()
    if "push" in order:
        push(arr,order.split()[-1])      # "push 123"이라고 값을 받고 split()으로 나눠 마지막 요소(정수값)를 return하여 스택에 넣어주었다.
    elif "top" in order:
        new.append(top(arr))
    elif "size" in order:
        new.append(size(arr))
    elif "empty" in order:
        new.append(empty(arr))
    elif "pop" in order:
        new.append(pop(arr))
for i in range(len(new)):
    print(new[i])