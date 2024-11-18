# 카펫

def solution(brown, yellow):
    # 세로 길이 -2 
    col = 1
    # col값에 따른 가로 길이 - 2
    row = (brown-(col*2)-4) // 2
    
    # col값을 1씩 증가시키면서 완전탐색 
    while True:
        # yellow 격자 갯수보다 작을 경우 
        if col * row < yellow:
            col += 1
            row = (brown-(col*2)-4) // 2
        # yellow 격자 갯수보다 클 경우 
        elif col * row > yellow:
            col +=1
            row = (brown-(col*2)-4) // 2
        else:
            break
    return [row+2,col+2]