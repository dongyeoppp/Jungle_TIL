# 사냥꾼   
# 이분탐색을 사용하지 않고 푼 코드이다. dequeue를 사용하여 풀었지만 시간초과가 나왔다.  

# import sys
# from collections import deque
# m, n, l = map(int,sys.stdin.readline().split())

# attack_list = list(map(int,sys.stdin.readline().split()))
# attack_list.sort()
# animal_list = []

# for i in range(n):
#     a,b = map(int,sys.stdin.readline().split())
#     if b<=l:
#         animal_list.append((a,b))  
# check=[False]*len(animal_list) 
# count =0
# for i in  attack_list:
#     idx=0
#     for j in animal_list:
#         if abs(j[0]-i)+j[1]<=l and not check[idx]:
#             count+=1
#             check[idx]=True
#         idx+=1
# print(count)

# 이분탐색을 이용하여 구현하였다.  
import sys

m, n, l = map(int,sys.stdin.readline().split())

attack_list = list(map(int,sys.stdin.readline().split()))
attack_list.sort()      # 이분 탐색을 위해 정렬
animals_list = []
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    animals_list.append((a,b))

count = 0       # 동물을 잡을때마다 +1
for i in animals_list:          # 동물을 기준으로 for문을 돌림
    max = i[0]-i[1]+l       #(x,y는 동물의 좌표) |x-사냥꾼의x좌표|+y <= 사정거리 -> 수식을 이용하여 사냥꾼좌표를 기준으로 max와 min값을 구함
    min = i[0]+i[1]-l
    start = 0   # 시작 인덱스
    last = len(attack_list)-1   # 마지막  인덱스  

    while start <= last:        # 해당 동물을 잡을 수 있는 범위 안에 사냥꾼이 있는지 확인
        mid = (start+last)//2       
        if min<= attack_list[mid]<=max:         # 사냥꾼이 해당 범위 내에 있을 경우
            count+=1
            break
        elif attack_list[mid] < min:        # 사냥꾼의 위치(x좌표)가 min값보다 작을 경우 샤냥꾼 위치 조정(x좌표 값이 더 클 경우를 고려해야함.) 
            start = mid+1
        else:
            last = mid-1                    # 사냥꾼의 위치가 max보다 클 경우 사냥꾼 위치 조정 (x좌표 값이 더 작을 경우 고려해야함)
print(count)
