# 예산 
#### 다시 풀어보자 !!
# import sys

# n = int(sys.stdin.readline())

# new = list(map(int,sys.stdin.readline().split()))
# new.sort(reverse=True)
# maxi = int(sys.stdin.readline())
# result = 0
# sumList = sum(new)
# if sumList <= maxi:
#     result = max(new)
# else:
#     answer= 0
#     for i in range(len(new)-1):
#         answer += (new[i]-new[i+1])*(i+1)
#         if sumList - answer > maxi:
#             continue
#         else:
#             result = new[i+1]+(maxi-(sumList - answer))//(i+1)
#             break
# print(result)
        
## 이분 탐색을 사용하여 풀이하였다. 
import sys

n = int(sys.stdin.readline())

new = list(map(int,sys.stdin.readline().split())) 

maxi = int(sys.stdin.readline())
start = 1
end = max(new)
result= 0
if sum(new)<=maxi:
    result= max(new)
else:
    while start <= end:
        mid = (start+end)//2
        summ = 0
        for i in new:
            if i>mid:
                summ+=mid
            else:
                summ+=i
        if summ > maxi:
            end = mid-1
        elif summ <= maxi:
            result=mid
            start = mid+1
print(result)