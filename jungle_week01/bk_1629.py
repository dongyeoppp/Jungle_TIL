# 곱셈 

# 처음에 리스트로 나머지 값을 받았다가 시간초과가 떠서 사전형식으로 값을 출력했는데도 불구하고 시간초과가 나왔다.  
# import sys
# a, b, c = map(int,sys.stdin.readline().split())

# n =1
# dump_dict = {}
# for i in range(b):
#     n = n *a
#     if n%c not in dump_dict :
#         dump_dict[n%c] = n%c
#     else:
#         print(dump_dict[n%c])
#         break


# 지수법칙과 모듈러 연산을 사용해야 한다.   
import sys
a,b,c = map(int,sys.stdin.readline().split())

def multi(a,b):
    if b == 1:          # n=1일 경우 바로 a%c로 답을 도출할 수 있다.  
       return a%c 
    mod = multi(a,b//2)     # 제곱 되는 값을 반으로 나눠주면서 재귀를 실행한다.         
    if b % 2 == 1:          # b가 홀수일 경우엔 a를 한번 더 곱해준다 2^5 = (2^2)*(2^2)*(2)
        return mod * mod * a % c
    else:
        return mod * mod % c        # b가 짝수일 경우  2^5 = (2^2)*(2^2)
print(multi(a,b))


# 재귀적 코드 순서 
#   multi(10,11)->multi(10,5)->multi(10,2)->multi(10,1)=> 10%12 = 10 = mod
#   multi(10,11)->multi(10,5)->multi(10,2)-> b가 짝수 -> 10 * 10 % 12 = 4 = mod
#   multi(10,11)->multi(10,5)->b가 홀수 -> 4 * 4 * 10 % 12 =4 = mod
#   multi(10,11) ->b가 홀수-> 4 * 4 *10 %12 = 4를 마지막 으로 return   ,, 4번의 재귀 호출 

# print(pow(a,b,c)) 내장함수를 사용하면 쉽게 풀린다.  