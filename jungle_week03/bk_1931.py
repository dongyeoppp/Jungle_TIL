# 회의실 배정   
# greedy 알고리즘    
# 끝나는 시간을 기준으로 회의 시간 데이터를 정렬한다. 빨리 끝날수록 회의를 더 많이 진행 할 수 있다.  
# 시작 시간과 끝나는 시간이 같은 경우 에외 케이스가 발생할 수 있으므로 끝나는 시간이 같을 경우 시작시간이 짧은 것을 먼저 정렬한다. 
# 2
# (2,2)
# (1,2)
# 출력 -> 2 ..(1,2), (2,2)
# 이 경우 (1,2)를 먼저 정렬하지 않으면 (2,2)만 경우에 수에 포함되게 된다. ((2,2)의 끝나는 시간이 (1,2)의 시작 시간 보다 크기 때문에 무시된다.)
import sys 

n = int(sys.stdin.readline())
time = []
for i in range(n):
    start, end =  map(int,sys.stdin.readline().split())
    time.append((start,end))            
time.sort()                 # start -> 시작 시간을 기준으로 정렬
time.sort(key=lambda x:x[1])        # end -> 끝나는 시간을 기준으로 다시 정렬   

result = [(-1,-1)]
for i in time:
    if result[-1][1] <= i[0]:     # 이전 회의의 끝나는 시간보다 다음 회의 시작시간이 더 클 경우   
        result.append(i)
print(len(result)-1)




    





