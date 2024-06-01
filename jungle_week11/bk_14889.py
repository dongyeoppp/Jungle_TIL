# 스타트와 링크   
# combinations 조합을 사용하였다. 
import sys   
from itertools import combinations
n = int(sys.stdin.readline())
team = []       # 능력치를 나타내는 배열을 담는다. 
for i in range(n):
    new= list(map(int,sys.stdin.readline().split()))  
    team.append(new)

answer= []
for i in range(n):
    answer.append(i)        # answer에 팀원의 번호를 담는다. (0~n-1까지)

new_team = list(combinations(answer,n//2))      # n의 절반으로 묶을 수 있는 경우의 수를 combinations를 통해 new_team에 넣는다. 
result = float('inf')               # result에 팀 능력치 차이의 최소값을 담는다. 초기값은 무한대로 세팅 

for i in new_team:
    power1 = 0      # 스타트 팀의 능력치
    for j in i:
        for k in i:
            if j != k:
                power1 += team[j][k]
    side_team = []      # 링트 팀 리스트에는 스타트 팀에 안들어가는 번호를 모두 넣는다. 
    for j in answer:
        if j not in i :
            side_team.append(j)
    power2 = 0      # 스타트팀의 능력치 
    for j in side_team:
        for k in side_team:
            if j !=k:
                power2 += team[j][k]
    result = min(result,abs(power1-power2))     # 두 팀의 능력치 차이를 result에 저장한다. 차이가 적은값으로 계속 갱신한다. 
    if result == 0:     # result가 0일 경우 최소값이 되므로 반복문을 탈출한다. 
        break
print(result)

# 백트래킹으로도 한 번 풀이해보자 !!   