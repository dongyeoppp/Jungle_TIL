# 퍼즐 게임 챌린지 
# 이분탐색으로 풀이 
def solution(diffs, times, limit):
    left = 1
    right = max(diffs)
    while left <= right:
        level = (left+right) // 2
        # time = 푸는데 걸리는 시간 
        time = 0
        for i in range(len(diffs)):
            # 숙련도가 난이도보다 높을 경우 
            if diffs[i] <= level:
                time += times[i]
            else:
                # 숙련도가 난이도보다 낮을 경우 
                time += sum(times[i-1:i+1])*(diffs[i] - level)+times[i]
        if time > limit:
            left = level + 1
        else:
            right = level - 1 
    return left
                
        