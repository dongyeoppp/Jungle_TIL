# 소수 경로 
# 소수 판별 법과 bfs로 풀이하였다. 
import sys
from collections import deque
n = int(sys.stdin.readline())
prime = []
for i in range(n):
    prime.append(list(map(int,sys.stdin.readline().split())))

def is_prime(number):       # number까지의 소수 모두 구하기 , 에라토스테네스의 체, 인덱스가 소수이면 true표시 
    arr = [True] * number
    arr[0] = False
    arr[1] = False
    for i in range(2,number):
        if arr[i]:      # i가 소수인 경우 
            j = 2           
            while (i* j) < number:
                arr[i*j] = False        # 소수인 i의 배수는 모두 소수가 아님 체크 
                j+=1
    return arr      # index가 소수이면 true인 배열 return 

# def is_prime_num(n):      // 소수 구하기-> 이렇게 소수인지 체크하면 맞긴하지만 시간이 더 걸림  
#     for i in range(2,  int(n**(1/2))+1):      // 제곱근을 기준으로 왼쪽에 약수가 존재하지 않는다면 오른쪽에도 약수가 존재하지 않으므로 반만 봐도 됨
#         if n % i == 0:
#             return False # i로 나누어 떨어지면 소수가 아니므로 False 리턴
#     return True 

is_prime_list = is_prime(10000)     # 10000까지의 소수 리스트 

def bfs(before,after):      # 빠르게 최단거리 depth를 봐야하기 때문에 bfs사용 
    que = deque()
    count=0
    que.append((before,count))      # 숫자가 최소 몇번 바뀌는지 count로 체크 
    visited = [False] * 10000       # visited 체크 
    visited[before] = True
    while que:
        print("hi")
        re_before , recount = que.popleft()
        if re_before == after:          # 해당 숫자가 바꾸려는 소수값과 같아지면 return 
            return recount      # 숫자가 바뀐 횟수 리턴 
        str_before = str(re_before)
        for i in range(4):      # 자릿수마다 0부터 9까지 대입 
            for j in range(10):
                new = int(str_before[:i] + str(j) + str_before[i+1:])   
                if is_prime_list[new] and new >= 1000 and not visited[new]:     # 소수이고, 네자리 수이고 , 방문하지 않았다면 que에 넣는다. 
                    que.append((new,recount+1))
                    visited[new] = True
                    print(new)
    return -1       # 숫자가 after로 바뀌지 않았을 경우 

for before, after in prime:
    result = bfs(before,after)
    if result == -1:
        print("Impossible")     # impossible인 case는 이 문제에서 없긴함 
    else:
        print(result)