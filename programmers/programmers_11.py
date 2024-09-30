# 입국심사 
# 이분탐색을 이용하여 풀이
def solution(n, times):
    start = 1
    # 모든 사람이 심사를 받는데 걸리는 시간의 최댓값 
    end = max(times) * n
    # start 값이 end보다 커질 때 까지 while문 수행한 이후 start 값을 리턴 
    while start <= end :
        mid = (start+end) // 2
        # count => mid 시간동안 심사를 받을 수 있는 사람의 수 
        count = 0
        for i in times:
            count += mid // i
            if count >= n :
                break
        # mid 시간 동안 심사 받을 수 있는 사람 수 가 n 보다 크거나 같을 경우 (최솟값을 구해야하므로 같을 경우도 포함)
        if count >= n:
            end = mid -1
        # mid 시간 동안 심사 받을 수 있는 사람 수가 n 보다 작을 경우 
        elif count < n:
            start = mid + 1
    return start
    