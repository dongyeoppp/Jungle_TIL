# 참외밭   

import sys

k = int(sys.stdin.readline())
new = []
for i in range(6):
    new.append(list(map(int,sys.stdin.readline().split())))
low = []
col = []
idx = 0
for i in new:
    if i[0] == 1 or i[0] == 2:
        low.append((i[1],idx))      # 가로 길이에 해당하는 값과 해당 index값을 넣음
        
    else:
        col.append((i[1],idx))      # 세로 길이에 해당하는  해당 index값을 넣음 
    idx+=1
col.sort()
low.sort()      # col과 low 리스트를 정렬하여 마지막에 가장 길이 긴 길이가 위치할 수 있도록 함

answer = set()
answer.add(col[-1][1])
answer.add((col[-1][1]+1)%6)
answer.add((col[-1][1]-1)%6)
answer.add(low[-1][1])
answer.add((low[-1][1]+1)%6)
answer.add((low[-1][1]-1)%6)        # 가장 긴 길이의 가로,세로를 answer 집합에 넣고 이후에 해당 변과 이웃하게 위치하는 변의 인덱스 값을 넣는다. 

# answer집합안에 들어있지 않은 가로 세로 길이가 작은 사각형의 가로 세로 길이가 된다.  
low_min = 0
for i in low:
    if i[1] not in answer:
        low_min = i[0]      
        break
col_min  = 0
for i in col:
    if i[1] not in answer:
        col_min = i[0]
        break
# 가장 큰 사각형에서 가장 작은 사각형을 빼서 넓이를 구한후 해당 넓이에 k를 곱해 출력한다. 
print(k*(low[-1][0]*col[-1][0] - low_min*col_min))