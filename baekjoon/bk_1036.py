# 36진수

import sys
input = sys.stdin.readline

n = int(input())
new = []
for i in range(n):
    new.append(input().strip())
k = int(input())

strings = ""
# 문자열 처리를 위해 주어진 36진수를 모두 한 문자열 strings에 추가 
for i in new:
    strings+=i
    strings+="."
all = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
diff = []
# 각각의 문자를 "Z"로 하나씩 변환해보고, Z로 변환한 문자열을 10진수로 변환한 값을 diff에 저장
for i in all:
    new = strings.replace(i,"Z")
    answer = new.split(".")
    count = 0
    for j in answer:
        if j != "":
            count += int(j,36)
    diff.append((count,i))
# 오름차순 정렬
diff.sort()
# "Z"로 변환했을 때 값이 가장 큰 k개의 단어를 모두 "Z"로 변환 
for i in range(k):
    item, key = diff.pop()
    strings = strings.replace(key,"Z")
# 변환된 문장을 10진수로 변환 (= 최댓값)
new_list = strings.split(".")
result = 0
for i in new_list:
    if i != "":
        result += int(i,36)
# 36진수로 변환
def change_36(result):
    # result가 0인 경우 예외 처리해야함!
    if result == 0:
        return 0
    answer = ""
    while result != 0:
        answer += all[result % 36]
        result = result // 36
    return answer[::-1]
print(change_36(result))