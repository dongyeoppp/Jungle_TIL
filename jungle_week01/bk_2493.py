# 탑 

# 첫번째 시도 시간초과..  스택을 통해 다시 구현해보자  

# import sys

# n = int(sys.stdin.readline())
# arr = list(map(int,sys.stdin.readline().split()))

# count = n-1

# answer =""
# for i in range(n-1,0,-1):
#     count = i-1
#     while count >= 0:
#         print(count,i)
#         if arr[i] <= arr[count]:
#             answer += f"{count+1} "
#             break
#         else:
#             count-=1 
#             if count <=0:
#                 answer += "0 "
#                 break
# answer+="0"
# print(answer[::-1])

# 두번째 코드이다. 스택을 구현하려고 노력하였으나 시간복잡도는 최악의 경우 O(n^2)으로 동일한 것 같다. 

# import sys
# n = int(sys.stdin.readline())
# arr = list(map(int,sys.stdin.readline().split()))
# count = n-1
# answer ="0 "
# for i in range(1,n):
#     count = 0
#     stack=[]
#     while True:
#         if i == count:
#             if stack == []:
#                 answer += "0 "
#                 break
#             else:
#                 removed = stack.pop()
#                 answer += f"{removed+1} "
#                 break
#         else:
#             if arr[i] <= arr[count]:
#                 stack.append(count)
#                 count+=1
#             else:
#                 count+=1
# print(answer[:-1])


# 이진탐색을 이용하여 시간복잡도를 줄였다.  
import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

stack = []
result = [0] * n        # 결과를 반영할 result리스트의 원소를 0 으로 초기화  
for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:        # 스택에 값이 존재할 때 현재 arr값보다 이전 arr의 값이 작은 경우 stack 해당 index를 제거 
        stack.pop()
    if stack:   # 스택에 남아 있는 요소가 있으면 result에 해당 인덱스에 값을 넣어줌  
        result[i] = stack[-1]+1
    stack.append(i) # 해당 인덱스를 다시 stack에 추가

    # ex) 탑의 높이가 6 9 5 7 4 일경우 index=1에서 값이 9, index값이 1이상일경우는 인덱스가 0 인(높이가 6) 탑에 도달 할 수 없으므로 스택에서 0 인덱스는 제거해준다.

print(" ".join(map(str,result)))        # result 리스트의 요소를 map()을 이용하여 문자열로 바꾸어준다. join을 통해 공백으로 구분하여 출력  



