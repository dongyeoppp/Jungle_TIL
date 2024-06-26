# 토너먼트   

import sys
from collections import deque
n ,a, b = map(int,sys.stdin.readline().split())

# 두 사람의 번호만 true로 체크 
check = [False] * (n+1)
check[a] = True
check[b] = True

que = deque()
for i in range(1,n+1):
    que.append(i)       # que에 모든번호 넣기 
count = 1
while True:
    for i in range((n+1)//2):       # round 체크 
        if n % 2 !=0:       # n이 홀수일 경우 
            if i == n//2:       # 마지막 번호는 짝이 없음으로 따로 처리 , count+1
                first = que.popleft()
                que.append(first)
                count+=1
            else:       # 마지막 번호가 아닐 경우 두 수를 que에서 꺼내어 비교 후 경우에 따라 하나만 다시 que에 넣는다. 
                first = que.popleft()
                second = que.popleft()
                if check[first] and check[second]:      # 두 사람이 만났을 경우 
                    print(count)
                    exit()
                elif check[second]:     # 두번째 사람만 true일 경우 
                    que.append(second)
                else:
                    que.append(first)  # 첫번째 사람만 true이거나 둘다 false일 경우 
        else:               # n이 짝수일 경우 
            first = que.popleft()
            second = que.popleft()
            if check[first] and check[second]:
                print(count)
                exit()
            elif check[second]:
                que.append(second)
            else:
                que.append(first)
            if i == (n+1)//2-1:     # 마지막 판 일때 
                count+=1
    n = n//2 + n % 2      