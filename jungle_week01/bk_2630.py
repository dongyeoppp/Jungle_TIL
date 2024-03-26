# 색종이 만들기 

import sys

n = int(sys.stdin.readline())
num_list = []
for i in range(n):
    num_list.append(list((map(int,sys.stdin.readline().split()))))

white = 0
blue = 0
def check(x,y,n):               # 해당 범위 안에서 값이 다 똑같은지 검사, 똑같다면 true를 하나라도 다른게 있다면 false를 리턴  
    base = num_list[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if num_list[i][j] != base:
                return False
    return True

def paper(x,y,n):
    global white, blue
    if check(x,y,n):            # check()함수가 true일 경우 지정한 범위의 첫 요소 값에 따라 count+1
        if num_list[x][y] == 1:
            blue +=1
        else:
            white +=1
        return          # check가 완료된 함수일 경우 더 이상 재귀 하지 않는다.      
    else:           
        paper(x,y,n//2)        # n의 값을 줄여주면서 범위를 작아지게 한다.  네부분으로 나누었을 때 해당 영역의 첫 인덱스 자리를 지정해준다.    
        paper(x+n//2,y,n//2)
        paper(x,y+n//2,n//2)
        paper(x+n//2,y+n//2,n//2)

paper(0,0,n)
print(white)
print(blue)