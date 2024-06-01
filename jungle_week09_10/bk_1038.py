# 감소하는 수   
# combinations을 사용하여 풀이하였다. 
import sys
from itertools import combinations 
n = int(sys.stdin.readline())
# new리스트를 1개 부터 10개씩 묶었을 때 "감소하는 수"를 모두 찾을 수 있다. (내림차순 정렬)
new = [9,8,7,6,5,4,3,2,1,0]
answer = []
for i in range(1,len(new)+1):
    a = list(combinations(new,i))
    a.sort()
    answer.append(a)    # answer리스트에 combinations로 묶은 리스트를 모두 넣는다. (다시 올림차순으로 묶음을 정렬)

cnt = -1    # 몇번 째 감소하는 수 인지를 체크한다. 
check = False
for i in answer:
    for j in i:
        new = ""
        for k in j:
            new+=str(k)
        cnt+=1
        if cnt == n:        # 해당 cnt가 주어진 n과 같아지면 해당 숫자를 출력하고 반복문을 끝낸다. 
            check = True
            print(new)
            exit()
if cnt < n :        # cnt의 최댓값 1022 (감소하는 수가 9876543210일때 n값 = 1022)보다 n이 클 경우 -1을 출력   
    print(-1)