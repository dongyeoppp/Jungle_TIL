# 멀티탭 스케줄링  
# greedy 알고리즘을 사용하여 해결하였다.  
# 플러그를 빼는 경우 -> count 값을 늘리는 경우, 무슨 플래그를 먼저 빼야할지 정하는 과정에서 어려움을 겪었다. answer값과 new를 조정하여 해결하였다.  
import sys

n , k = map(int,sys.stdin.readline().split())
graph = list(map(int,sys.stdin.readline().split()))   
use = [0] * (k+1)       # 멀티탭을 사용하는 인덱스는 1 갱신하여 저장 (처음엔 0으로 초기화)
count = 0                # 플러그를 빼는 최소 횟수   
for i in range(k):
    if sum(use) < n:
        use[graph[i]]=1         # 처음 멀티탭에 자리가 남아있을 경우 
    else:
        if use[graph[i]] == 1:      # 멀티탭이 꽂혀있는 플러그가 다시 나왔을 경우 continue
            continue
        else:
            answer = -1         # 멀티 탭에 꽂혀있지 않은 플러그가 나올 경우 꽂혀있는 플러그 중 당장 뺄 플러그 값을 넣어준다. (해당 인덱스 이후부터의 플러그에서 멀티탭에 꽂혀있는 플러그 중 가장 멀리있는 플러그 )
            new = []            # new 안에는 꽂혀있는 플러그 값을 넣음, 중복되는 값을 넣지 않는다.  
            for j in range(i+1,k):      # 해당 플러그 이후에 나오는 값의 범위로 지정  
                if use[graph[j]] == 1:
                    if graph[j] not in new:
                        answer = graph[j]
                        new.append(answer)
            if answer == -1:                # 해당 플러그(i) 이후에 순서의 플러그들에, 현재 꽂혀있는 플러그 값이 없을 경우 (아무 플러그나 빼주어도 상관없다.)
                for h in range(1,k+1):
                    if use[h] == 1:
                        use[h] = 0
                        use[graph[i]]=1
                        count+=1
                        break
            elif len(new)< n:           # 해당 플러그(i) 이후 순서의 플러그들에, 꽂혀 있는 플러그 값이 0보다크고 n개 보단 작을 경우 (new에 들어가있지 않은 플러그 중 하나를 뺀다.)
                for q in range(1,k+1):
                    if use[q] == 1 and q not in new:
                        use[q] = 0
                        use[graph[i]] = 1
                        count+=1
                        break   
            else:       # 해당 플러그(i) 이후 순서의 플러그들에, 꽂혀 있는 플러그 값이 다 들어있을 경우(answer값에 들어있는 플러그를 빼고 해당 플러그를 넣어준다. answer-> 현재 꽂혀있는 플러그 중 가장 늦은 순서의 값)
                use[answer] = 0
                use[graph[i]] = 1
                count+=1
print(count)

    