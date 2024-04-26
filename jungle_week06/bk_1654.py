# 랜선 자르기  
# 이분 탐색을 사용하여 풀이하였다.  
import sys

k,n = map(int,sys.stdin.readline().split())
new = []
for i in range(k):
    new.append(int(sys.stdin.readline()))
start = 1
last = sum(new)//n

while start<=last:
    count = 0
    mid = (start+last) // 2 
    for i in new:
        count += i//mid
    if count < n:
        last = mid-1
    else:
        start = mid+1           # 최댓값을 구하기 위해 count>=n 일때도 범위를 갱신해주었다.  
print(last)