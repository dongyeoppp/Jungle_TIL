# 사냥꾼   

import sys
from collections import deque
m, n, l = map(int,sys.stdin.readline().split())

attack_list = list(map(int,sys.stdin.readline().split()))
attack_list.sort()
animal_list = []
count = 0
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    animal_list.append((a,b))

animal_list.sort(key=lambda x:x[1])
animal_list.sort()

animals_list = deque()
for i in animal_list:
    animals_list.append(i)

for i in  attack_list:
    length = len(animals_list)
    for j in range(length):
        removed = animals_list.popleft()
        if abs(removed[0]-i)+removed[1] <=l:
            count+=1
        else:
            animals_list.append(removed)
print(count)
