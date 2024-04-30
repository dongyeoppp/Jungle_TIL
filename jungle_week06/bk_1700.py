# 멀티탭 스케줄링

import sys

n, k = map(int, sys.stdin.readline().split())
tap = list(map(int, sys.stdin.readline().split()))

plug = [False] * (k+1)      # 멀티탭에 해당 인덱스값이 꽂혀있으면 true
count = 0       # 멀티탭을 뽑으면 count+1
new = 0         # tap의 index값
for i in tap:
    if plug.count(True) < n:        # 멀티탭에 꽂을 자리가 남아있을 경우
        plug[i] = True
        new += 1
    else:                           # 빈 멀티탭 구멍이 없을 경우
        if plug[i]:            # 사용하려는 플러그가 꽂혀 있는 경우
            new += 1
            continue
        else:                       # 사용하려는 플러그가 꽂혀 있지 않은 경우
            save = 0
            last_use = []
            for j in tap[new+1:]:       # 꽂으려고 하는 플러그 이후에 무슨 플러그가 있는지 봐야한다.
                # 꽂혀있는 plug를 last_use라는 리스트에 넣는다. 중복값은 넣지 않는다.
                if plug[j] and j not in last_use:
                    save += 1         # save값은 last_use의 길이
                    last_use.append(j)
            if save == n:               # 꽂혀있는 플러그들이 last_use에 모두 들어가 있을 때 -> last_use에 가장 나중에 들어간 plug를 빼기
                plug[last_use[-1]] = False
                count += 1
                plug[i] = True
                new += 1
            elif save > 0:              # 꽂혀있는 플러그 중 하나라도 last_use에 들어가 있을 때  -> 멀티탭에 꽂혀있는데 last_use에 안 들어가 있는 플러그 아무거나 빼기
                for h in range(1, k+1):
                    if plug[h] and h not in last_use:
                        plug[h] = False
                        count += 1
                        plug[i] = True
                        break
                new += 1
            else:                   # 꽂혀있는 플러그 중 아무것도 last_use에 없을 때 -> 아무거나 빼도 상관없다
                for h in range(1, k + 1):
                    if plug[h] == True:
                        plug[h] = False
                        count += 1
                        plug[i] = True
                        break
                new += 1

print(count)