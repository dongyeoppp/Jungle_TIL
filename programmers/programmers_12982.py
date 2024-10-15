# 예산

def solution(d, budget):
    d.sort()
    sum_price = sum(d)
    count = len(d)
    # 모든 부서를 지원하는 금액이 지원해 줄 수 있는 금액보다 작을 때 까지 가장 큰 값을 d 리스트에서 pop한다.  
    while sum_price > budget:
        answer = d.pop()
        sum_price -= answer
        # 남은 부서 의 개수 = count
        count -= 1
    return count 
