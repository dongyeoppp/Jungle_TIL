# [pccp 모의고사 1] 4번
# 운영체제  
# 우선순위 큐를 이용하여 풀이  
import heapq
def solution(program):
    # 우선순위 정렬 , 호출시간 정렬 이후 반대로 정렬 
    program.sort()
    new_program = sorted(program,key = lambda x:x[1])
    new_program = new_program[::-1]
    
    answer = [0] * 11
    heap = []
    time = new_program[-1][1]
    
    while new_program:
        while new_program and time >= new_program[-1][1]:
            heapq.heappush(heap,new_program.pop())
        if heap: 
            now = heapq.heappop(heap)
            answer[now[0]] += time - now[1]
            time += now[2]
            # 모든 프로그램이 종료되는 시각 측정 
            if not new_program and not heap:
                answer[0] += time
        else:
            time+=1

    # heap에 값이 남아 있을 수 있으므로 반복문을 한번 더 수행 
    while heap:
        now = heapq.heappop(heap)
        answer[now[0]] += time - now[1]
        time += now[2]
        # 모든 프로그램이 종료되는 시각 측정 
        if not new_program and not heap:
            answer[0] += time
    return answer