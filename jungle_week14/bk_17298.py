# 오큰수
# 스택을 이용하여 풀이하였다. 오른쪽에 있는 수(자신보다 큰 수) 중 가장 왼쪽에 있는 값을 구해야한다. 
import sys

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

stk = []
answer = [-1] * n       # 출력할 리스트의 default값으로 -1을 넣어주었다. 
for i in range(len(arr)):
    while stk and arr[stk[-1]] < arr[i]:        # stack이 비어있거나 stack의 마지막 값이 arr[i]보다 작을 경우 
        removed = stk.pop()                     # 가장 가까운 값중 자신보다 큰 값이 있다면 stk에서 pop 
        answer[removed] = arr[i]                # 자신의 인덱스에 해당 값을 반영 
    stk.append(i)       # arr의 인덱스값을 stk에 넣어준다. 

print(*answer)     
