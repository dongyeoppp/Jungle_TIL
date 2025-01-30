# 방 번호
# 배열  
import sys

input = sys.stdin.readline
# 문자열로 입력값을 받을 경우 strip()을 사용하여 개행 문자 '/n'을 제거해야 Error가 나지 않는다.
n = input().strip()
# 중복된 숫자가 몇개 나오는지 체크
#  가장 많이 나온 횟수 -> max_num / 가장 많이 나온 숫자 -> save
new =  [0] * 10
save = -1
max_num = -1
for i in n:
    if int(i) == 6 or int(i) == 9:
        new[9] += 1
        if new[9] > max_num:
            max_num = new[9]
            save = 9
    else:
        new[int(i)] += 1
        if new[int(i)] >= max_num:
            max_num = new[int(i)]
            save = int(i)

if save == 6 or save == 9:
    if max_num % 2 == 0:
        print(max_num // 2)
    else:
        print(max_num // 2+1)
else:
    print(max_num)

