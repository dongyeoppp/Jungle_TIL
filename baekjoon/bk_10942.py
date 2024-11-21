# 팰린드롬?

import sys

input = sys.stdin.readline

n = int(input())

number = list(map(int,input().split()))

# 수 나열의 가장 자리수가 같은지 확인
def check(s,e):
    if number[s-1] == number[e-1]:
        return True
    return False

# 팰린드롬을 발견하면 dp 배열에 값을 1로 초기화 
# 발견한 팰린드롬을 기준으로 앞,뒤에 하나씩 수를 추가하며 팰린드롬을 확인
# 팰린드롬 규칙이 맞지 않을 경우 반복문 종료 
def save(x,y):
    while True:
        x = x - 1
        y = y + 1
        if 1 <= x <= n and 1<= y <= n and check(x,y):
            dp[x][y] = 1
        else:
            return 
        
# dp 배열 0으로 초기화하여 생성 
dp = [[0]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    # 팰린드롬이 한 자리일 경우 
    dp[i][i] = 1
    x = i
    y = i
    save(x,y)
    # 팰린드롬이 두 자리일 경우 
    new_x = i
    new_y = i+1
    if 1<= new_x <=n and 1<= new_y <= n and check(new_x,new_y):
        dp[new_x][new_y] = 1
        save(new_x,new_y)

m = int(input())
for i in range(m):
    s, e = map(int,input().split())
    print(dp[s][e])
