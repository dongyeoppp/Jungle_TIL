# 출석체크  

# 첫 시도에 시간초과로 빨리 문제를 해결하지 못했다.  

import sys 

n , k , q , m = map(int,sys.stdin.readline().split())
ran = []
sleep_list = [False] * (n+3)
sleep = list(map(int,sys.stdin.readline().split()))  
for j in sleep:
    sleep_list[j] = True    # 자고 있는 학생의 해당 인덱스를 true

check = list(map(int,sys.stdin.readline().split()))
    
for i in range(m):
    s,e = map(int,sys.stdin.readline().split())
    ran.append((s,e))

check_list = [1] * (n+3)        # check_list를 학생 수만큼 1로 초기화  
for i in check:
    if sleep_list[i]:           # 자고 있는 학생은 그대로 1 유지 
        continue
    for j in range(i,n+3,i):
        if sleep_list[j]:       # 문자를 받았지만 자고있는 학생도 1 유지  
            continue
        check_list[j] = 0       # 출석체크를 했으면 0으로 바꿈  

check_list[2] = 0       # 2 인덱스를 참고해야하므로 0으로 바꿈  
for i in range(3,n+3):
    if check_list[i]:
        check_list[i] = check_list[i-1]+1           # 자고 있는 학생 체크하여 전 인덱스에 있는 값에 +1을 더해 갱신해준다. 
    else:
        check_list[i] = check_list[i-1]             # 출석체크를 한 학생이라면 카운트 하지 않는다.  

for i in ran:
    print(check_list[i[1]]- check_list[i[0]-1])         # 범위마다 출석체크를 안한 학생수 체크  //  

    # 범위가 주어질 때마다 테이블을 갱신하지 않고 check_list에서 범위만 체크해서 출석체크를 안한 학생이 몇명인지 알 수 있었다. 