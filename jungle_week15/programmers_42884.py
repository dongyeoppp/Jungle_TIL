# 단속 카메라

def solution(routes):
    # 진출 지점을 기준으로 오름차순 정렬 
    new_routes = sorted(routes,key=lambda x:x[1])
    count = 1
    number = 1
    answer = new_routes[0][1]
    while number<len(routes):
        # answer에 저장된 진출 지점보다 더 값이 작을 경우
        if answer >= new_routes[number][0]:
            number+=1
        # answer에 저장된 진출 지점보다 더 값이 클 경우
        else:
            answer = new_routes[number][1]
            count+=1
    return count