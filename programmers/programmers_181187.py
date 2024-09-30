# 두 원 사이의 정수 쌍

import math
def solution(r1, r2):
    answer = 0
    for i in range(1,r2):
        # floor -> 내림 , sqrt -> 제곱근, pow -> 제곱 
        x2 = math.floor(math.sqrt(math.pow(r2,2)-math.pow(i,2)))
        # r1이 i 보다 작을 경우 squrt 계산을 할 수 없으므로 따로 분리해서 처리한다. 
        if i <= r1:
            # ceil -> 올림 
            x1 = math.ceil(math.sqrt(math.pow(r1,2)-math.pow(i,2)))
            if x1 < 1:
                answer += x2
            else:
                answer += (x2-x1+1)
        # r1이 i 보다 작을 경우 x2의 값보다 작은 경우만 더해준다. 
        else:
            answer += x2    
    # 4사분면의 한 사분면만 구한 값에 4를 곱한다.
    answer *= 4
    # x축과 y축 위의 점들을 더해준다. 
    answer += (r2 -r1 +1) *4
    return answer