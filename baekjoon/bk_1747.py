# 소수 & 팰린드롬

# import sys

# n = int(sys.stdin.readline())

# def prime(n):
#     if n == 1:
#         return False
#     for i in range(2,int(n ** (1/2))+1):
#         if n % i == 0:
#             return False
#     return True

# while True:
#     if prime(n) and str(n) == str(n)[::-1]:
#         print(n)
#         break
#     else:
#         n +=1

## 에라토스테네스의 채 
import sys

n = int(sys.stdin.readline())

def is_prime(n):
    arr = [True] * n
    arr[0] = False
    arr[1] = False
    for i in range(2,n):
        if arr[i]:
            j = 2
            while (i * j) < n:
                arr[i*j] = False
                j+=1
    return [k for k in range(n) if arr[k]]      # 소수만을 담은 리스트를 반환 
arr = is_prime(1003002)     # n의 범위가 1000000까지이므로 소수의 최댓값은 1003001

for i in arr:
    if i>=n  and str(i) == str(i)[::-1]:
        print(i)
        break