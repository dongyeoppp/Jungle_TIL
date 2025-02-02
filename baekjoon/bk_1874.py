# # 스택 수열   
# # 스택을 사용하여 풀이 함. 풀이하는데 시간이 좀 걸림.. 더 연습 필요!!
import sys

input = sys.stdin.readline

n = int(input())

# 만들어야 하는 수열 answer1
answer1 = []
for i in range(n):
    answer1.append(int(input()))
# 1부터 n까지 담긴 리스트 answer2
answer2 = [i for i in range(1,n+1)]

stk = []
result = []
cnt1 = 0
cnt2 = 0 
check = True

while cnt2 < n:
    if answer1[cnt1] >= answer2[cnt2]:
        stk.append(answer2[cnt2])
        result.append("+")
        if answer1[cnt1] == answer2[cnt2]:
            cnt1+=1
            result.append("-")
            stk.pop()
        cnt2+=1
    else:
        # 주어진 수열을 만들 수 없을 경우 
        if stk.pop() != answer1[cnt1]:
            check = False
            break
        result.append("-")
        cnt1+=1
# stk에 값이 남아있을 수 있으므로 주어진 수열을 만들 수 있는지 체크 필요 
while stk:
    if stk.pop() != answer1[cnt1]:
        check = False
        break
    result.append("-")
    cnt1+=1

if not check:
    print("NO")
else:
    for i in result:
        print(i)
        


# import sys

# input = sys.stdin.readline

# n = int(input())

# answer = [int(input()) for i in range(n)]

# stk = []
# cnt = 1
# result = []
# check = True
# for i in answer:
#     while i >= cnt:
#         stk.append(cnt)
#         result.append("+")
#         cnt+=1
#     if stk and stk[-1] == i:
#         stk.pop()
#         result.append("-")
#     # 수열을 만들 수 없을 경우 체크 
#     else:
#         check = False
#         break

# if not check:
#     print("NO")
# else:
#     print("\n".join(result))   
    


