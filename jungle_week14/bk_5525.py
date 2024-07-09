# IOIOI

import sys 

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
string = sys.stdin.readline().strip()

count = 0
idx = 0
result = 0
while idx < m-2:
    if string[idx:idx+3] == "IOI":      # "IOI" 를 찾은 경우  
        count+=1
        idx+=2
        if count == n:      # result + 1
            result+=1
            count-=1
    else:       # "IOI"를 못 찾은 경우 
        idx+=1
        count =0 # 다시 count 초기화 
print(result)
        