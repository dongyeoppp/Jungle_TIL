# 요격 시스템
# 그리디 알고리즘 

def solution(targets):
    # 각 미사일의 끝나는 지점을 기준으로 정렬 
    targets.sort(key = lambda x: x[1])
    count = 0
    end = 0
    for i in targets:
        # 만약 end 값보다 다음 미사일의 시작 지점이 클 경우 
        # 요격 +1, end 값 갱신 
        if i[0] >= end:
            count+=1
            end = i[1]
    return count
            