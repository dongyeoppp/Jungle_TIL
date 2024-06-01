# 두 용액   
# 투 포인터를 사용해서 풀이하였다.  
 
# import sys

# n = int(sys.stdin.readline())

# new = list(map(int,sys.stdin.readline().split()))   
# new.sort()  # 정렬 

# start = 0
# end = len(new)-1
# result = float('inf')
# answer1=0
# answer2 = 0
# while start != end:
#     if abs(new[start]+new[end]) == 0:   # 두 용액의 특성값의 합이 0 일 경우 break
#         answer1 = new[start] 
#         answer2 = new[end]
#         break
#     elif abs(new[start]+new[end] > 0):      # 두 용액의 특성값의 합이 양수 일 경우 end -1
#         if abs(new[start]+new[end]) < result :
#             result = abs(new[start]+new[end])
#             answer1 = new[start] 
#             answer2 = new[end]
#         end -=1
#     else:
#         if abs(new[start]+new[end]) < result :          # 두 용액의 특성값의 합이 음수 일 경우 start +1
#             result = abs(new[start]+new[end])
#             answer1 = new[start] 
#             answer2 = new[end]
#         start +=1 
# print(answer1, answer2)

import sys

n = int(sys.stdin.readline())

new = list(map(int,sys.stdin.readline().split()))
new.sort(key=lambda x: abs(x))      # lambda를 사용해서 절대값이 작은 순서로 정렬하였다. 
result = float('inf')
answer1=0
answer2=0
for i in range(len(new)-1):     # 절대값으로 정렬했으므로 리스트의 앞,뒤 값만 비교하여 최소값을 구했다. 
    if abs(new[i]+new[i+1]) < result:
        result = abs(new[i]+new[i+1])
        answer1= new[i]
        answer2= new[i+1]
if answer1 < answer2:
    print(answer1,answer2)
else:
    print(answer2,answer1)