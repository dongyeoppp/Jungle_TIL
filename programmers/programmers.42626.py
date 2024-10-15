# 더 맵게 

import heapq
def solution(scoville, K):
    # scoville 리스트를 우선순위 큐로 설정 
    heapq.heapify(scoville)
    count = 0
    while True:
        answer1 = heapq.heappop(scoville)
        # 가장 작은 값이 k 보다 크거나 같으면 return 
        if answer1 >= K:
            return count
        # 리스트에 값이 한개 이하일 경우 -1 리턴 (모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우)
        if scoville == []:
            return -1
        answer2 = heapq.heappop(scoville)
        heapq.heappush(scoville,answer1+answer2*2)  
        # 음식을 섞는 최소 횟수 카운트
        count += 1
        