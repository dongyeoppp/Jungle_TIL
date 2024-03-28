# 더하기 사이클  

import sys

n  = sys.stdin.readline().strip()
if int(n) < 10:
        n = "0"+n
first = n
count = 0
while True:
    base = int(n[0])+int(n[1])
    base = str(base)
    n = n[1]+ base[-1]
    count +=1
    if first== n:
          break
print(count)


# 문자열을 사용하여 풀이하였다. 나머지 연산을 사용한 풀이도 있었다.  