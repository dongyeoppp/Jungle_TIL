# 신입 사원   
# greedy 알고리즘을 사용하여 풀이하였다. 첫시도는 for문을 두번 넣어 시간초과가 나왔다. 수정하여 해결하였다.  
# 첫 시도   

# import sys
# t = int(sys.stdin.readline())

# for i in range(t):
#     n = int(sys.stdin.readline())
#     graph=[]
#     count = n
#     for j in range(n):
#         graph.append(list(map(int,sys.stdin.readline().split())))
#     graph.sort()
#     for k in range(1,n):
#         for h in range(0,k):
#             if graph[k][1] > graph[h][1]:             # 서류 심사 성적을 기준으로 정렬 한후 각각 하나씩 비교하였다, 이건 그리디 알고리즘이 아닌 것 같다.
#                 count-=1
#                 break
#     print(count)
        
import sys
t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    graph=[]
    for j in range(n):
        graph.append(list(map(int,sys.stdin.readline().split())))
    graph.sort()            # 서류 심사 성적을 기준으로 정렬 
    count = 1           # count -> 신입사원의 최대 인원수 (서류 심사 성적이 1등일 경우는 무조건 포함되므로 1로 설정)
    start = graph[0][1]
    for k in range(1,n):
        if start > graph[k][1]:     # 면접 성적이 이전 신입사원의 면접 성적 보다 높다면 신입사원의 최대 인원수에 포함 된다. (서류 심사 성적은 이전 신입사원을 제외하면 1등이므로)  
            count +=1               
            start = graph[k][1]     # 기준이 되는 start 면접성적을 갱신해주면서 비교를 진행한다.  
    print(count)