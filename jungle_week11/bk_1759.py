# 암호 만들기   
# combinations를 사용하여 풀이하였다.  
import sys
from itertools import combinations
l,c = map(int,sys.stdin.readline().split())
new = list(map(str,sys.stdin.readline().split()))
new.sort()      # 사전식의 출력을 위해 정렬하였다. 
mo = ['a','e','i','o','u']      # 모음 리스트
answer = list(combinations(new,l))
for i in answer:
    count1 = 0   # 모음 개수 
    count2 = 0   # 자음 개수 
    for j in i:
        if j in mo:
            count1+=1       # 해당 문자열에 모음의 개수 count
        else:           
            count2+=1       # 해당 문자열에 자음의 개수 count
    if count1 >= 1  and count2 >=2:     # 해당 조건을 만족할 경우 print해주었다. 
        print(*i,sep="")