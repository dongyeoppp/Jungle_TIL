# 양궁 대회

from itertools import combinations
def solution(n, info):
    # 어피치 보다 한 발만 더 던지면 해당 점수를 획득할 수 있으므로 점수를 획득하기 위한 new 리스트를 만든다.
    new = []
    count = 0 
    for i in info:
        new.append((i+1,count))
        count+=1
    # 어피치와 라이언의 점수 차이를 반환한다. (라이언의 점수가 더 높지 않다면 -2 반환)
    def point_check(combination):
        new1 = set()
        ryan_point = 0
        for i in combination:
            new1.add(i[1])
            ryan_point += (10-i[1])

        peach_point = 0
        for i in range(0,10):
            if i not in new1 and info[i] != 0:
                peach_point += (10-i)
        if ryan_point > peach_point:
            return ryan_point - peach_point
        else:
            return -2
    # 조합을 사용하여 어피치보다 라이언의 점수가 높을 경우를 모두 구한다. 
    result = -1
    save = []
    for i in range(1,n+1):
        answer = list(combinations(new,i))
        for j in answer:
            answer2 = 0
            for k in j:
                answer2+=k[0]
            # 화살을 다 쏘지 않았더라도 점수 차이가 가장 많이 날 수 있음을 고려한다. 
            # 점수 차이가 같더라도 combinations로 순서가 보장 되므로 가장 낮은 점수를 맞이 맞춘 경우를 따로 고려하지 않았다. 
            if answer2 <= n:
                diff = point_check(j)
                if  diff >= result:
                    result = diff
                    save = j
    last = [0]*11
    # 라이언이 이기지 못할 경우 [-1] 반환 
    if save == []:
        return [-1]
    
    last_count = n
    for i in save:
        last[i[1]] = i[0]
        last_count -= i[0]
    # 화살을 다 쏘지 않은 경우의 점수 차가 가장 많이 날 경우 마지막 인덱스에 남은 화살을 모두 넣어 리스트를 반환한다. 
    if last_count != 0:
        last[-1] += last_count
    return last
        