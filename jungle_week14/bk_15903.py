# 카드 합체 놀이  

import sys 
import heapq

n, m = map(int,sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split()))

heapq.heapify(card)     # card 리스트를 heaq으로 변환 (기본이 최소 힙)

for i in range(m):
    answer1 = heapq.heappop(card)
    answer2 = heapq.heappop(card)
    add_num = answer1+answer2
    heapq.heappush(card,add_num)
    heapq.heappush(card,add_num)

print(sum(card))