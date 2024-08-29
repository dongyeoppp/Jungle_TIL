# 안전지대 
def solution(board):
    dx = [1,-1,0,0,1,1,-1,-1]
    dy = [0,0,1,-1,1,-1,1,-1]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                for k in range(8):
                    x = dx[k] + i
                    y = dy[k] + j
                    # 지뢰 근처 지역이 0일 경우 -1로 바꾸어 줌 
                    if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 0:
                        board[x][y] = -1
    result = 0
    # 남은 0 개수 체크 
    for i in board:
        result+= i.count(0)
    return result        