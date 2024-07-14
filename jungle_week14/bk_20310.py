# 타노스  

import sys

s = sys.stdin.readline().strip()

zero = s.count('0')//2
one = s.count('1')//2
count0 = 0
count1 = 0

new = []

for i in s:
    if i == "0":
        if count0 < zero:
            new.append(i)
            count0+=1
        else:
            count0+=1
    else:
        if count1 >= one:
            new.append(i)
            count1+=1
        else:
            count1+=1
print("".join(new))