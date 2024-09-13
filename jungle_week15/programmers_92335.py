# k진수에서 소수 개수 구하기
def solution(n, k):
    answer = ""
    # k 진수 구하기 
    while n >= k:
        new = n % k
        answer = str(new)+answer
        n = n // k
    answer = str(n) + answer
    
    # 소수 판별 
    def prime(num):
        for i in range(2,int(num**(1/2))+1):
            if num % i == 0:
                return False
        return True
        
    # '0'을 기준으로 나눔
    check = answer.split("0")
    count = 0
    for i in check:
        if i != "" and i != "1":
            num = int(i)
            if prime(num):
                count+=1
    return count