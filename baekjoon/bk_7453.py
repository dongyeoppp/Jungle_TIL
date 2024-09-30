# 합이 0인 네 정수
# 투 포인터로 풀이
# 주어진 행렬에 1행 -> a배열 / 2행 -> b배열  / 3행 -> c배열  / 4행 -> d배열 
# python으로 실행 했을 경우 시간초과.. pypy로 제출하여 성공함 

import sys

n = int(sys.stdin.readline())

a = []
b = []
c = []
d = []
for i in range(n):
    new1 = list(map(int,sys.stdin.readline().split()))
    a.append(new1[0])
    b.append(new1[1])
    c.append(new1[2])
    d.append(new1[3])

ab = []
cd = []
# 4가지 배열을 2개의 배열로 줄인 이후 정렬 
for i in range(n):
    for j in range(n):
        ab.append(a[i]+b[j])
        cd.append(c[i]+d[j])

ab.sort()
cd.sort()

# 투포인터 사용 
left = 0
right = len(ab)-1
result = 0
while left < len(ab) and right >= 0:
    # 합이 0 보다 클 경우 
    if ab[left] + cd[right] > 0:
        right -= 1
    # 합이 0 보다 작을 경우 
    elif ab[left] + cd[right] < 0:
        left += 1
    # 합이 0일 경우 
    else:
        base_right = right
        base_left = left
        # 같은 수가 존재 할 수 있음으로 체크해야 함 
        while right >= 0 and ab[base_left] + cd[right] == 0:
            right -=1
        while left < len(ab) and ab[left] + cd[base_right] == 0:
            left+=1
        # 합이 0일 경우 개수 체크한 후 더 함 
        result += (left - base_left) * (base_right - right)
print(result)



