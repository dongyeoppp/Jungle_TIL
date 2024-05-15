# 겹치는 건 싫어  
# 튜 포인터를 사용하여 풀이하였다. 
import sys

n , k = map(int,sys.stdin.readline().split())
new = list(map(int, sys.stdin.readline().split()))   
start = 0
end = 0         # 두개의 변수를 포인터로 사용 
dic = dict()       
for i in new:
    dic[i]=0    # 주어진 수를 key로 가지는 사전을 만들었다. 초기값은 0   
result =[]      # 두 포인터의 차이를 계속 저장해주었다.
while start <= n-1:         # start 포인터가 n이 되었을 때 while문을 종료한다.
    if dic[new[start]] < k:         # 주어진 k의 개수보다 작은 경우는 start+1, 사전에서도 해당 숫자의 value값 +1 
        dic[new[start]]+=1
        start+=1
        result.append(start-end)
    else:                       # start가 가리키는 숫자의 갯수가 k개 보다 커졌을 경우  
        while dic[new[start]] == k:   # start가 가리키는 숫자를 key로 갖는 tkwjsdml value값이 k개로 줄때까지 end+1 
            dic[new[end]]-=1
            end+=1
            result.append(start-end)        # start와 end값이 조정될 때마다 start-end값을 result에 추가한다.  
print(max(result))          # result값에 최댓값을 출력한다.  
