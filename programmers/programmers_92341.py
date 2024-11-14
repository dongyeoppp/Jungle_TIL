# 주차 요금 계산 

import math
def solution(fees, records):
    # 각각의 차량의 입차 시간 저장 
    new = dict()
    # 각각의 차량의 누적된 주차 시간 계산 
    cars_time = dict()
    # 두 문자열의 시간차이 계산 
    def time_calculation(out_time, in_time):
        out_times = out_time.split(":")
        out_time_hour = int(out_times[0])
        out_time_min = int(out_times[1])
        in_times = in_time.split(":")
        in_time_hour = int(in_times[0])
        in_time_min = int(in_times[1])
        if out_time_min < in_time_min:
            out_time_min += 60
            out_time_hour -= 1
        return (out_time_hour - in_time_hour) * 60 + (out_time_min - in_time_min)
    
    for i in records:
        car = i.split(" ")
        # 처음 들오는 차량일 경우 
        if car[1] not in cars_time:
            cars_time[car[1]] = 0
        # 차량이 입차할 경우 차량의 입차 시간 저장 
        if car[2] == "IN":
            new[car[1]] = car[0]
        # 차량이 출차할 때 저장되어 있는 입차 시간과의 시간 차이 계산하여 cars_time 딕셔너리에 저장 
        else:
            cars_time[car[1]] += time_calculation(car[0],new[car[1]])
            # 차량이 출차했을 경우 구분 
            new[car[1]] = -1
    # 차량이 출차하지 않았을 경우 23:59에 출차했음으로 간주 
    for i in new:
        if new[i] != -1 :
            cars_time[i] += time_calculation("23:59",new[i])
    # 사전을 키값을 기준으로 오름 차순 정렬 
    cars_time = sorted(cars_time.items(), key = lambda x:int(x[0]))
    result = []
    for i in cars_time:
        if fees[0] >= i[1]:
            result.append(fees[1])
        else:
            # ceil함수를 이용해 값을 올림 
            answer = fees[1] + math.ceil((i[1]-fees[0])/fees[2]) * fees[3]
            result.append(answer)
    return result