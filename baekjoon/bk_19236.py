# 청소년 상어
import sys
import copy 
input = sys.stdin.readline

fish_number = []
direction = []
for i in range(4):
    line = list(map(int,input().split()))
    fish = []
    where = []
    for j in range(0,4):
        fish.append(line[j*2])
        where.append(line[j*2+1])
    fish_number.append(fish)
    direction.append(where)

dx = [0,-1,-1,0,1,1,1,0,-1]
dy = [0,0,-1,-1,-1,0,1,1,1]

# 상어 초기 위치의 물고기 번호로 초기 결과 설정
initial_fish = fish_number[0][0]
result = initial_fish
fish_number[0][0] = -1  # 상어가 차지하는 위치를 -1로 설정

# 물고기 이동
def fish_move(fish_number, direction):
    for number in range(1, 17):
        found = False
        for i in range(4):
            for j in range(4):
                if fish_number[i][j] == number:
                    direct = direction[i][j]
                    for _ in range(8):
                        x, y = i + dx[direct], j + dy[direct]
                        if 0 <= x < 4 and 0 <= y < 4 and fish_number[x][y] != -1:
                            # 교환
                            fish_number[i][j], fish_number[x][y] = fish_number[x][y], fish_number[i][j]
                            direction[i][j], direction[x][y] = direction[x][y], direct
                            found = True
                            break
                        direct = (direct % 8) + 1
                    if found:
                        break
            if found:
                break

# 상어 이동
def shark_move(shark_row, shark_col, score, fish_number, direction):
    global result
    fish_move(fish_number, direction)
    direction_shark = direction[shark_row][shark_col]
    moved = False
    for step in range(1, 4):
        nx, ny = shark_row + dx[direction_shark] * step, shark_col + dy[direction_shark] * step
        if 0 <= nx < 4 and 0 <= ny < 4 and fish_number[nx][ny] > 0:
            moved = True
            # 물고기 이동에 대한 재귀를 계혹 해야함으로 물고기가 이동한 이후의 fish_number와 direction을 shark_move 재귀 함수의 매개변수로 넘김
            copy_fish_number = copy.deepcopy(fish_number)
            copy_direction = copy.deepcopy(direction)
            next_fish = copy_fish_number[nx][ny]
            copy_fish_number[shark_row][shark_col] = 0
            copy_fish_number[nx][ny] = -1
            shark_move(nx, ny, score + next_fish, copy_fish_number, copy_direction)
    if not moved:
        result = max(result, score)

# 상어의 첫 이동
shark_move(0, 0, result, fish_number, direction)
print(result)