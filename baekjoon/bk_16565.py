# N 포커
# 포함 - 배제의 원리 사용하여 풀이
import sys

# 조합의 수 구하기
from math import comb   

n = int(sys.stdin.readline())

result = 0
for i in range(1,n//4+1):
    # 13개의 숫자 중 "포카드" 쌍을 만들 숫자의 개수 * 나머지 카드를 뽑을 경우의 수  
    answer = comb(13,i) * comb(52-i*4,n-i*4)
    # 홀 수 일 경우 
    if i%2 == 1:            
        result += answer
    # 짝 수 일 경우 
    else:
        result -= answer
print(result % 10007)