# 과일 탕후루
# 투포인터를 이용하여 풀이하였다. 
import sys

n = int(sys.stdin.readline())

fruit = list(map(int,sys.stdin.readline().split()))

left = 0 
right = 0
result = 0
dict = dict()

while right < n:
    # 사전에 값이 추가될 경우 
    if fruit[right] not in dict:
        dict[fruit[right]] = 1
    else :
        dict[fruit[right]] += 1
    # 사전의 길이가 2 이하가 될 때 까지 반복한다.  left ++ 
    while len(dict) > 2:
        dict[fruit[left]] -=1
        if dict[fruit[left]] == 0:
            del dict[fruit[left]]
        left+=1
    # right값을 늘려주기 전에 max값 저장 
    result = max(result,right-left+1)
    right+=1

print(result)