# 신기한 소수   

import sys

n = int(sys.stdin.readline())

# 소수 판별 
def isPrime(number):
    for i in range(2,int(number**(1/2))+1):
        if number % i  == 0:
            return False
    return True

# 숫자 자릿수를 더해가며 소수 판별 (백트래킹)
def add(answer):
    # 자릿수가 n이고 소수일 경우 answer 출력 
    if len(answer) == n :
        if isPrime(int(answer)):
            print(int(answer))
            return 
        else:
            return
    for i in range(1,10):
        if isPrime(int(answer)):
            # 한 자리수 추가하여 재귀 반복
            answer+=str(i)
            add(answer)
            # 재귀가 끝나면 추가한 숫자 제거 
            answer = answer[:len(answer)-1]

for i in range(2,10):
    add(str(i))
















