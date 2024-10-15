# 벡터 매칭

# a와 b 점이 있을 경우, a(x1,y1)과 b(x2,y2)의 벡터는 (x1-x2,y1-y2)로 표현 가능 
# 벡터의 합은 모든 벡터의 x좌표와 y좌표를 더한 값이 됨
# ex) c(x1-x2,y1-y2), d(x3-x4,y3-y4) 두 벡터가 존재할 경우 합 벡터는 (x1-x2+x3-x4,y1-y2+y3-y4)
import sys
import math
from itertools import combinations
input = sys.stdin.readline

t = int(input())

# 벡터의 길이 구하기 
def vector(x,y):
    return math.sqrt(math.pow(x,2)+math.pow(y,2))

for i in range(t):
    graph = []
    n = int(input())
    sum_x = 0
    sum_y = 0
    for j in range(n):
        p_x, p_y = map(int,input().split())
        # 좌표를 받을 때 같이 모든 정점의 x좌표의 합과 y좌표의 합을 저장 
        sum_x += p_x
        sum_y += p_y
        graph.append((p_x,p_y))
    # 모든 정점을 반으로 나누어 생각 -> 20개의 점이 있을 때 10개씩 묶임 -> 이때 묶인 10개를 벡터의 도착지점, 나머지 10개의 점을 벡터의 시작 시점이라고 생각 
    new = list(combinations(graph,n//2))
    
    result = float('inf')
    for j in new:
        x = 0
        y = 0
        for k in j:
            # 도착지점의 벡터들을 모두 더함 
            x += k[0]
            y += k[1]
        # 합 벡터 구하기 
        x -= (sum_x-x)
        y -= (sum_y-y)
        # 합 벡터의 가장 작은 값 저장 
        result = min(result,vector(x,y))
    print(result)

