# 이진 검색 트리  

import sys
sys.setrecursionlimit(10 ** 6)      # 파이썬은 기본으로 최대 1000번의 재귀 호출을 허용하기 때문에 최대깊이를 늘려준다.  
arr = []
while True:
    x = sys.stdin.readline().strip()    # 입력값이 없을 경우 int()로 받지 못하기 때문에 밑에서 int로 변형한 후에 arr에 추가해준다.  
    if not x:           # 입력값이 없을 경우 
        break
    arr.append(int(x))      
result = []
def new(arr,base):
    if len(arr) == 1:       # arr의 길이가 1이 될 경우 
        print(arr[0])
        return
    left = []
    right = []
    for i in range(1,len(arr)):
        if base > arr[i]:           # arr의 0번째 인덱스 값을 기준으로 작은 값은 left, 큰 값들은 right로 리스트를 나눠준다.   
            left.append(arr[i])
        elif base < arr[i]:
            right.append(arr[i])
    if left:
        new(left,left[0])       # 후위 순회한 결과를 print해야하므로 left, right, 루트 노드 순으로 출력을 해준다.  
    
    if right:
        new(right,right[0])
    print(base)

new(arr,arr[0])