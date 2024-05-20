# 치킨 배달
# 처음에 반례를 찾지 못해 틀렸다.     
# import sys
# n , m = map(int,sys.stdin.readline().split())
# city= []
# for i in range(n):
#     new = list(map(int,sys.stdin.readline().split()))
#     city.append(new)
# inf = float('inf')
# chicken = []
# home = []
# for i in range(n):
#     for j in range(n):
#         if city[i][j] == 1:
#             home.append([inf,i,j])
#         elif city[i][j] == 2:
#             chicken.append([inf,i,j])

# for i in chicken:
#     chicken_distance = 0
#     for j in home:
#         chicken_distance += abs(i[1]-j[1]) + abs(i[2]-j[2])
#     print(chicken_distance)
#     i[0] = chicken_distance

# chicken.sort()
# new_chicken = chicken[:m]
# result=0
# for i in home:
#     for j in new_chicken:
#         if abs(i[1]-j[1]) + abs(i[2]-j[2]) < i[0]:
#             i[0] = abs(i[1]-j[1]) + abs(i[2]-j[2])
#     result+=i[0]
# print(result)

# combinations을 사용하여 풀이하였다.  
import sys
from itertools import combinations
n , m = map(int,sys.stdin.readline().split())
city= []
for i in range(n):
    new = list(map(int,sys.stdin.readline().split()))
    city.append(new)

chicken = []       
home = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append((i,j))          # 집의 좌표를 담는다.
        elif city[i][j] == 2:
            chicken.append((i,j))       # 치킨의 좌표 담는다. 

new_chicken = list(combinations(chicken,m))         # 현재 있는 치킨 집의 개수에서 m개씩만 있을 모든 경우를 고려한다. 

result = [] # 경우의 수 마다 나오는 치킨 거리를 모두 넣는다. 
for i in new_chicken:
    all_distance = 0
    for j in home:
        distance = float('inf')
        for k in i:
            if abs(j[0]-k[0]) + abs(j[1]- k[1]) < distance:
                distance = abs(j[0]-k[0]) + abs(j[1]- k[1])         # 현재 집에서 갈 수 있는 치킨 집 중 최단거리를 구한다. = distance
        all_distance+=distance      # 위에서 구한 최단거리를 각 경우의 수마다의 치킨거리를 의미하는 all_distance에 더해준다. 
    result.append(all_distance)     # combinations로 묶은 각각의 경우의 수에 해당하는 치킨 거리를 result에 추가한다. 
print(result)
print(min(result))      # result에 들어있는 값 중 최소 값을 출력(이 최소값이 나온 경우가 수익이 가장 많이나오는 치킨 집의 배치가 된다.) 