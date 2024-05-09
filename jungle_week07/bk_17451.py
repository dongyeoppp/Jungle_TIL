# 평행 우주   
# 처음 풀이는 max값을 기준으로 행성을 돌면서 조건을 걸어주었다. 시간초과가 나왔다.  
# import sys

# n = int(sys.stdin.readline())
# new = list(map(int,sys.stdin.readline().split()))
# count = 1
# while True:
#     answer = max(new) * count
#     check = True
#     save = answer
#     for i in new:
#         answer -= answer % i
#         if answer < i:
#             check = False
#             break
#         if answer == max(new):
#             break
#     if check == True:
#         print(save - save%new[0])
#         break
#     else:
#         count+=1

# 행성의 순서를 뒤집어서 확인하였다. for문 하나로 그리디하게 문제를 풀이하여 통과했다.   
import sys

n = int(sys.stdin.readline())
new = list(map(int,sys.stdin.readline().split()))
speed = new[-1]     # 마지막 행성의 속도 부터 
for i in new[::-1]:
    if speed <= i : # 도착한 행성의 속도가 현재 속도 보다 높을 경우 speed 값을 그냥 갱신해준다.  
        speed =i
    else:
        if speed % i != 0:      # 도착한 행성의 속도가 현재 속도의 배수가 아닐 경우 
            speed = (speed//i+1)* i     # 도착한 행성의 배수 중 최소값을 speed로 갱신  (ex) 현재 speed가 500, i = 400이라면 400의 배수 중 500보다 크면서 가장 작은 수가 speed가 된다.)
        else:
            speed = (speed//i)*i
print(speed)