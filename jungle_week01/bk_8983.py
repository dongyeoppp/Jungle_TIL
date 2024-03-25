# 사냥꾼  
# 이진탐색을 사용하지 않음. 41점 맞은 코드 . 이진탐색 방법을 고려해 봐야함  
import sys

n, m, l = map(int,sys.stdin.readline().split())

hunt_list = list(map(int,sys.stdin.readline().split()))     # 사수 위치 hunt_list
animal_list = []

for i in range(m):
    animal_list.append(list(map(int,sys.stdin.readline().split())))     # 동물의 좌표 리스트 animal_list

catch = 0
catch_list = []     # 해당 동물을 잡았는지 check
for i in hunt_list:
    for j in animal_list:
        if abs(j[0]-i)+j[1]<=l and j not in catch_list:     # 거리와 한 번 잡았는지 여부를 check함  
            catch +=1
            catch_list.append(j)
    if catch == len(animal_list):       # 모든 사수 위치를 돌기전에 동물을 모두 잡으면 for 문 종료 
            break
print(catch)

# 이진 탐색을 활용한 방법 , 하지만 위 코드와 똑같이 백준에서 100점 통과되지 않았다.
# import sys


# def binary_search(arr, target):
#      start = 0
#      end = len(arr)
#      while start < end:
#           mid = (start+end)//2
#           if arr[mid][0] > target:
#                end = mid
#           else:
#                start = mid +1
#      return start 

# n, m, l = map(int,sys.stdin.readline().split())

# hunt_list = list(map(int,sys.stdin.readline().split()))
# hunt_list.sort()
# animal_list = []

# for i in range(m):
#     animal_list.append(list(map(int,sys.stdin.readline().split())))
# animal_list.sort()

# catch = 0
# catch_list = []
# for i in hunt_list:
#     start_index = binary_search(animal_list, i-l)
#     end_index = binary_search(animal_list, i+l+1)
#     for j in range(start_index,end_index):
#         if abs(animal_list[j][0]-i)+animal_list[j][1]<=l and animal_list[j] not in catch_list:
#             catch +=1
#             catch_list.append(animal_list[j])
#     if catch == len(animal_list):
#             break
# print(catch)

                



