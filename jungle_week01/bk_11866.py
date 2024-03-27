# 요세푸스 문제  0

import sys

n, k = map(int,sys.stdin.readline().split())
arr=[]
for i in range(1,n+1):
    arr.append(i)
result = []
while arr != []:        # arr가 비어질때 까지 while문 실행
    for i in range(k):
        removed = arr.pop(0)        # k번 동안 arr의 0인덱스 값 제거
        if i != k-1:
            arr.append(removed)     # 제거한 인덱스의 값을 다시 리스트의 마지막에 추가  
        else:
            result.append(removed)  # k번쩨 값일 경우 다시 arr에 추가하지 않고, result에 추가 (result에는 항상 리스트의 k번째값이  들어감 )
answer = ", ".join(map(str,result))       
print("<"+answer+">")