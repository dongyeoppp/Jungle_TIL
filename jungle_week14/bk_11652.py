# 카드
import sys

n = int(sys.stdin.readline())
arr = []
dict = dict()
for i in range(n):
    answer = int(sys.stdin.readline())
    arr.append(answer)
    if answer not in dict:
        dict[answer] = 0
    dict[answer] +=1

dict = sorted(dict.items(), key= lambda x: (-x[1],x[0]))        # 1. 빈도를 기준으로 오름차순으로 정렬 , 2. 키값을 기준으로 정렬 
print(dict[0][0])