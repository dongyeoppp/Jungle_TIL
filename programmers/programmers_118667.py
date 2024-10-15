# 두 큐 합 같게 만들기

from collections import deque
def solution(queue1, queue2):
    count = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    # 반복문안에서 큐의 합을 계속 구하면 시간초과 발생 
    answer1 = sum(queue1)
    answer2 = sum(queue2)
    # 큐의 길이는 300000까지 임으로 이 이상을 반복하면 반복문 종료 
    while count <= 300000:
        # 듀 큐의 합이 같을 경우 
        if answer1 == answer2:
            return count
        # queue1의 합이 더 클 경우 
        elif answer1 > answer2:
            removed = queue1.popleft()
            queue2.append(removed)
            answer1 -= removed
            answer2 += removed
        # queue2의 합이 더 클 경우 
        elif answer1 < answer2:
            removed = queue2.popleft()
            queue1.append(removed)
            answer1 += removed
            answer2 -= removed
        count +=1 
    # 반복문이 끝났지만 두 큐의 합이 같지 않으므로 -1 리턴 
    return -1