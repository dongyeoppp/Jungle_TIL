# 같은 나머지  
# gcd로 최대공약수를 구하여 풀이한다. 
import sys
import math
n = int(sys.stdin.readline())
new = list(map(int,sys.stdin.readline().split()))

gap_list = []
for i in range(len(new)):
    for j in range(i,len(new)):
        gap = new[i] - new[j]
        gap_list.append(gap)
result = gap_list[0]

for i in range(1,len(gap_list)):
    result = math.gcd(result, gap_list[i])

print(result)