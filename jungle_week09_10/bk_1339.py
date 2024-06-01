# 단어 수학  
# 처음 풀이는 단순히 가장 자릿수가 높은 문자에 1~9중 할당하지 않은 가장 큰 수를 지정해주었다.  
# ABB
# BB
# BB -> 이 경우 BB 가 더 많아 질 경우 A = 8이고 B = 9일때 가장 큰 수를 출력하는 경우가 생긴다. 자릿수 와 중복되는 문자를 고려하여 다시 풀이하였다. 
 
# import sys

# n = int(sys.stdin.readline())  
# dict = {}       # 문자열과 길이 저장 // 길이를 갱신 
# new = []
# result = set()      # 존재하는 문자 모두 저장 
# last = {}       # 존재하는 문자를 key로 저장. 해당 문자가 어떤 숫자를 배정받는지 저장 
# give = 9        # 하나씩 줄여가며 문자에 부여  

# for i in range(n):
#     new1 = sys.stdin.readline().strip()
#     new.append(new1)
#     dict[new1]=len(new1)
#     for j in new1:
#         result.add(j)
# count = 0
# for i in result:
#     last[i] = -1
#     count+=1

# new_count = 0
# save = 0

# while count > new_count:
#     answer = -1 # 최대값 저장 
#     for i in dict:
#         if dict[i] > answer:
#             answer=dict[i]
#             save = i
#     for j in dict:
#         if j == save:
#             if last[j[len(j)-dict[j]]] != -1:
#                 dict[j] -=1
#             else:
#                 last[j[len(j)-dict[j]]] = give
#                 dict[j] -=1
#                 give-=1
#                 new_count+=1
# print(last)
# sum = 0                
# for i in new:
#     st= ""
#     for j in i :
#         st += str(last[j])
#     sum+=int(st)    
# print(sum)

# 그리디한 방법으로 풀이하였다. 해당 문자열이 몇번째인지 확인한 후 그 자릿수 크기만큼 10을 곱해주어 우선순위를 체크했다. 
import sys   
n = int(sys.stdin.readline())
new = []    # 주어지는 문자열을 담음 
dict = {}     # 주어진 문자열의 우선순위를 체크하고 이후 숫자로 변환된 값을 넣는다.  
for i in range(n):
    new.append(sys.stdin.readline().strip())

for i in new:
    l = len(i)-1        # 해당 문자열의 길이 체크 
    for j in i:
        if j not in dict:
            dict[j] = 10**l     # 첫번째 문자열의 자릿수 사전으로 해당 문자에 우선순위 부여  (ABC라면 'A':10**2)
            l-=1
        else:
            dict[j] += 10**l
            l-=1
dict_sorted = sorted(dict.items(),key = lambda x:x[1], reverse=True)        # dict사전을 value값을 정렬한 리스트 생성 , 키값과 value값을 묶어 튜플 형태로 리스트에 들어간다. 

give = 9     
for i in dict_sorted:
    dict[i[0]] = give   # 우선순위가 큰 문자 부터 큰값을 부여하여 dict을 갱신한다.  
    give-=1

sum = 0
for i in new:
    st=""
    for j in i:
        st += str(dict[j])
    sum+=int(st)
print(sum)