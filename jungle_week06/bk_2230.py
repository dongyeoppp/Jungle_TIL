# 수 고르기 
# combinations을 사용하여 풀이하였지만 메모리 초과가 났다. 메모리 초과가 나오는 이유는 한 배열에 너무 많은 값이 들어갔을 경우 발생한다고 한다.  
# import sys
# from itertools import combinations
# n,m = map(int,sys.stdin.readline().split())
# new = []
# for i in range(n):
#     a = int(sys.stdin.readline())
#     new.append(a)
# answer = list(combinations(new,2))
# result = float('inf')
# for i in answer:
#     if abs(i[0]-i[1]) >= m:
#         result = min(result,abs(i[0]-i[1]))
# print(result)  

# 투 포인터를 사용하여 풀이하였다. 
import sys
n,m = map(int,sys.stdin.readline().split())
new = []
for i in range(n):
    a = int(sys.stdin.readline())
    new.append(a)
new.sort()      # 정렬을 통해 시간 복잡도를 줄여줄 수 있다. 오름차순으로 정렬한 경우, 두 값의 차이가 m보다 크면 그 이후에 나오는 값의 차이는 더 클 것이므로 확인하지 않아도 된다.   
result = new[-1] - new[0]           # result값은 가장 큰 값과 가장 작은 값의 차이보다 클 수 없다. 
start = 0       # 두 개의 포인터 생성
end = 1
while start<n and end<n:            # start 나 end가 인덱스 범위를 벗어낫을 경우 종료  
    if new[end] - new[start] < m:       # 두 값의 차이가 m보다 작을 경우 // start값을 고정하고 end값을 더해주며 비교한다. 
        end+=1
    elif new[end] - new[start] == m:        # 차이가 m과 같을 경우 반복문을 종료하고 m을 출력하도록 한다. / 
        result= m
        break
    else:                   # 두 값의 차이가 m보다 클 경우 // 두 값의 차이를 저장하고 start값을 갱신해주어 고정하는 값을 바꿔준다.  
        result = min(result,new[end]-new[start])        
        start+=1
print(result)