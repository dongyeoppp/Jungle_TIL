# 카드 정렬하기   
# 가장 작은 카드 묶음 두개를 합치는 과정을 반복한다. 
# heap(우선순위 큐)을 사용하여 풀이하였다.  
import sys
import heapq
n = int(sys.stdin.readline())
heap = []
for i in range(n):
    heapq.heappush(heap,int(sys.stdin.readline()))
result = []
# if n == 1:
#     print(0)        # n-1일 경우 합칠 카드 묶음이 없음으로 0을 출력한다.  
# else:
while len(heap)>1:
    rm1 = heapq.heappop(heap)       
    rm2 = heapq.heappop(heap)       # heap리스트에서 가장 작은 카드 묶음 두개를 꺼낸다.  
    answer = rm1 + rm2              # 두 개의 카드 묶음을 더하고 다시 heap에 넣어준다.  
    result.append(answer)           # 합친 값은 계속 result라는 새로운 리스트에 넣어준다.  
    heapq.heappush(heap,answer)
    if len(heap) <= 1 :     # heap의 길이가 1이 될 경우 반복문 탈출  
        break
print(sum(result))     # result의 값을 모두 더해 출력한다. result가 빈리스트일 경우 0을 출력한다.  