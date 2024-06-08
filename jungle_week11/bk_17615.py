# 볼 모으기  
# 그리디 알고리즘  
import sys

n = int(sys.stdin.readline())
rb = sys.stdin.readline().strip()
# 공의 색깔에 따른 함수 

def ball_move(color):
    save1 = False       # 공의 색깔 변환 체크 
    count1 = 0          # 공의 이동 횟수 체크 
    for i in rb:        # color인 공을 왼쪽으로 옮기는 경우 
        if i != color:  # color와 색이 같지 않은 경우 체크
            save1 = True
        else :
            if save1:
                count1+=1      # 그 전공과 색이 같지 않으면 +1
            else:
                save1 = False

    save2 = False
    count2 = 0
    for i in rb[::-1]:  # color인 공을 오른쪽으로 옮기는 경우 
        if i != color:
            save2 = True
        else :
            if save2:
                count2+=1
            else:
                save2 = False
    return min(count1,count2)   # color공을 왼쪽으로 옮기는 경우와 오른쪽으로 옮기는 경우 체크  
print(min(ball_move('R'),ball_move('B')))       # "R"인지 "B"인지 체크해서 최소값 출력 (총 네가지 경우를 구분해야한다. )