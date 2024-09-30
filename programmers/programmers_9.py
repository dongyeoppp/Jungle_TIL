# 아날로그 시계
def solution(h1, m1, s1, h2, m2, s2):
    # 시작 시간과 끝나는 시간을 초로 변환
    start_second = h1 * 3600 + m1 * 60 + s1
    end_second = h2 * 3600 + m2 * 60 + s2
    
    count = 0
    # 처음 주어진 시각의 초침이 분침,시침과 겹칠 경우 예외 처리 (00시 일 경우와 12시일 경우) 
    if start_second == 0 * 3600 or start_second == 12 * 3600:
        count += 1
    
    while start_second < end_second:
        # 시침은 1초에 1/120도 이동
        hour_angle = start_second / 120 % 360
        # 분침은 1초에 1/10도 이동
        minute_angle = start_second / 10 % 360 
        # 초침은 1초에 6도 이동 
        second_angle = start_second * 6 % 360

        start_second+=1
        # 0도 일 경우 360도 처리 
        next_hour_angle = 360 if start_second / 120 % 360 == 0 else start_second / 120 % 360
        next_minute_angle = 360 if start_second / 10 % 360 == 0 else start_second / 10 % 360
        next_second_angle = 360 if start_second * 6 % 360 == 0 else start_second * 6 % 360
        # 시침과 초침이 만났을 경우 (완전히 같거나 지나쳤을 경우를 고려)
        if (second_angle < hour_angle and next_second_angle >= next_hour_angle):
            count+=1
        # 분침과 초침이 만났을 경우 (완전히 같거나 지나쳤을 경우를 고려)
        if (second_angle < minute_angle and next_second_angle >= next_minute_angle):
            count+=1
        # 시침,분침,초침이 모두 만났을 경우 중복 count - 1 (00시와 12시일 경우)
        if next_second_angle == next_minute_angle == next_hour_angle:
            count-=1
    return count
