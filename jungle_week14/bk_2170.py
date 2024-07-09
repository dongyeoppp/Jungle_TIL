# 선 긋기  

import sys 

n = int(sys.stdin.readline())
line = []
for i in range(n):
    line.append(list(map(int,sys.stdin.readline().split())))
line.sort()         # 시작 지점을 기준으로 정렬 

end = -1000000001        # 처음에 겹치는 부분이 없을 경우로 들어가야하므로 end를 최대한 작은 수로 설정한다.
start= -1000000001       # 처음에 end - start값이 result에 더해지는데 아무것도 더해지면 안되므로 end와 같은수로 설정함  
result = 0

for s,t in line:
    # 겹치는 부분이 없을 때 
    if  end < s:
        result += (end-start)       
        start = s
        end = t
    else:
        # 겹치는 부분이 있을 경우 
        end = max(end,t)

result+= end-start  # 마지막 경우도 더해줘야 함

print(result)