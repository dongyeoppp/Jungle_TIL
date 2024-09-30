# 키패드 누르기 
def solution(numbers, hand):
    result = ""
    keypad = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
    current_left = "*"
    current_right = "#"
    
    # 키패드에서 두개의 번호 사이의 거리 계산
    def path(current,end):
        for i in range(len(keypad)):
            for j in range(len(keypad[0])):
                if keypad[i][j] == current:
                    low = i
                    col = j
        for k in range(len(keypad)):
            if keypad[k][1] == end:
                end_low = k
                end_col = 1
        return abs(low-end_low) + abs(col-end_col)
    
    for i in numbers:
		    # 번호가 1 or 4 or 7일 경우
        if i == 1 or i == 4 or i == 7:
            result+="L"
            current_left = i
        # 번호가 3 or 6 or 9일 경우
        elif i == 3 or i == 6 or i == 9:
            result += "R"
            current_right = i
        else:
		        # 중간에 있는 번호 일 경우 거리 계산하여 더 거리가 짧은 손가락이 눌릴 수 있도록함
            if path(current_left,i) < path(current_right,i):
                result+="L"
                current_left = i
            elif path(current_left,i) > path(current_right,i):
                result+="R"
                current_right = i
            else:
		            # 거리가 같을 경우 hand값을 기준으로 정함
                if hand == "left":
                    result+="L"
                    current_left = i
                else:
                    result+="R"
                    current_right = i
    return result