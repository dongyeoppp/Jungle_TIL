# [1]차 다트 게임

def solution(dartResult):
    number = ["0","1","2","3","4","5","6","7","8","9"]
    point = ["S","D","T"]
    answer = 0
    result = 0
    save = 0
    for i in range(len(dartResult)):
        # 숫자 일 경우 
        if dartResult[i] in number:
            # 숫자가 10인 경우 예외 처리 
            if dartResult[i+1] == "0":
                continue
            elif dartResult[i-1] == "1":
                result+=answer
                save = answer
                answer = 10
            else:
                result+=answer
                save = answer
                answer = int(dartResult[i])
        # s, d, t 중 하나 일 경우
        elif dartResult[i] in point:
            if dartResult[i] == "D":
                answer = answer ** 2
            elif dartResult[i] == "T":
                answer = answer ** 3
            else:
                continue
        # 옵션 *,# 중 하나 일 경우 
        else:
            if dartResult[i] == "*":
                result -= save
                result += save * 2
                answer = answer * 2
            elif dartResult[i] == "#":
                answer = answer * (-1)
    return result+answer
                
            
            