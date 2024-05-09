# AC   
# deque를 사용하여 풀이하였다.  
import sys 
from collections import deque  
t = int(sys.stdin.readline())

for i in range(t):
    st = sys.stdin.readline().strip()       # 'R', 'D' 문자열 받기 
    n = int(sys.stdin.readline())  
    new = sys.stdin.readline().strip()
    new1 = new[1:-1]    # 괄호 제거 
    new2 = deque(new1.split(","))   # ','을 기준으로 나눠 숫자 문자열을 deque로 리스트에 넣기 
    count = 0       # R의 개수를 센다
    save = 0        # error를 출력했는지 체크한다.  
    for j in st:
        if j == "R":
            count+=1
        else:   
            if new2 == deque([]) or new2 == deque(['']):    
                print('error')      # deque에 값이 없는데 문자열이 D일 경우 
                save += 1
                break
            else:
                if count %2 ==1:        # count가 홀수일 경우 뒤에서 수를 뺀다
                    new2.pop()
                else:
                    new2.popleft()      # count가 짝수일 경우 앞에서 수를 뺀다. 
    if (new2 == deque([]) or new2 == deque([''])) :
        if save == 0:
            print("[]")     # error를 출력하지 않았을 경우 [] 출력  
        else:
            continue
    else:
        if count % 2 == 1:
            new2.reverse()      # count가 홀수일 경우 리스트를 뒤집어서 출력 
        print('['+','.join(map(str,new2))+']')      # 공백 없이 값들을 리스트에 넣어서 문자열로 출력 