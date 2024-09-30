# N으로 표현

def solution(N, number):
    dp = [set() for i in range(9)]
    dp[1].add(N)
    # n 과 number가 같을 경우 (x 사용횟수가 1일 경우 )
    if N == number:
        return 1
    # n 사용횟수가 2 이상일 경우 
    # 사칙연산으로 나올 수 있는 모든 수를 dp 리스트 안의 해당 인덱스의 집합에 더함 
    for i in range(2,9):
        for j in range(1,i):
            for k in dp[j]:
                for h in dp[i-j]:
                    dp[i].add(int(str(N)*i))
                    dp[i].add(k+h)
                    dp[i].add(k*h)
                    if h >= k and k != 0:
                        dp[i].add(h-k)
                        dp[i].add(h//k)
                    elif k >= h and h != 0:
                        dp[i].add(k-h)
                        dp[i].add(k//h)
        # number가 존재할 경우 
        if number in dp[i]:
            return i
    # 최솟값이 8보다 클 경우 
    return -1
                