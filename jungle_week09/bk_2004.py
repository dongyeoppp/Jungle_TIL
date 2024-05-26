# 조합 0의 개수   
# 해당 펙토리얼에서 2와5의 개수를 세서 0의 개수를 구한다. 2와 5를 곱했을 경우 10이 나와서 0이 붙는다.
# 25의 경우 25//2 = 12, 12 //2 = 6, 6 //2 =3 , 3 // 2 = 1 ==> 12 + 6 + 3 + 1 = 22 이므로 25!에 들어있는 2의 개수는 22개이다. 
# 12!의 경우  12 //2 = 6, 6 //2 =3 , 3 // 2 = 1 ==> 10 , 13!의 경우  13 //2 = 6, 6 //2 =3 , 3 // 2 = 1  ==> 10 이므로 이 조합의 계산에서 2의 개수는 22 - 10 - 10 = 2이다. 
# 5의 개수도 위와 같이 구하고 2의 개수와 5의 개수 중 최솟값이 뒤에 붙는 0의 개수가 된다.   
import sys

n,m = map(int,sys.stdin.readline().split())

def factorial_zero_count(a,t):
    count = 0
    while a >= t:
        count += a//t
        a = a//t
    return count 

count_2 = factorial_zero_count(n,2) - factorial_zero_count(m,2) -factorial_zero_count(n-m,2)
count_5 = factorial_zero_count(n,5) - factorial_zero_count(m,5) -factorial_zero_count(n-m,5)
print(min(count_2,count_5))