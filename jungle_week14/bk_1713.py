# 후보 추천하기  
# 사전을 이용해서 풀이 

import sys

n = int(sys.stdin.readline())

recommand = int(sys.stdin.readline())

student = map(int,sys.stdin.readline().split())

new_dict = dict()
count = 0
for i in student:
    if i in new_dict:           # dict에 원래 있던 후보일 경우 
       new_dict[i][1]+=1
    else:
        if len(new_dict) < n:
             new_dict[i] = [count,1]
             count+=1
        else:     # dict에 추천 학생 번호 
            save = min(new_dict.keys(), key=lambda k: (new_dict[k][1], new_dict[k][0]))
            del new_dict[save]
            new_dict[i] = [count,1]
            count+=1   

result = sorted(new_dict.keys())
print(*result)
