# 컵라면
import sys
import heapq
input = sys.stdin.readline

n = int(input())

new = []

for i in range(n):
    deadline, cup = map(int,input().split())
    new.append((deadline,cup))
# 데드라인 기준으로 정렬
new.sort()

answer= []
for i in new:
    heapq.heappush(answer,i[1])
    if i[0] < len(answer):
        # 데드라인을 넘긴다면 컵라면 수가 가장 작은 것을 pop
        heapq.heappop(answer)
print(sum(answer))