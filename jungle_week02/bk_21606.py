# 아침 산책  
# 서브테스크가 있는 문제로 첫 시도는 73점으로 만점을 받지 못했다.  
# 처음 코드에서는 dfs 함수를 사용해 실내 노드를 기준으로 경우의 수를 계산하였는데 실외노드로 계산을 하는 것이 더 편하다고 하여 그 쪽으로 다시 생각을 해봤다. 
 
# import sys

# n  = int(sys.stdin.readline())
# a = sys.stdin.readline().strip()
# graph = [[] for i in range(n+1)]
# for i in range(n-1):
#     x,y = map(int,sys.stdin.readline().split())
#     graph[x].append(y)
#     graph[y].append(x)
# in_out = [True]       # 실내인지 실외인지 구분하는 리스트   
# for i in a:
#     if i =='1':
#         in_out.append(True)
#     else:
#         in_out.append(False)

# def dfs(start):
#     count = 0
#     visited=[False]*(n+1)     # 처음에 이 visited 리스트를 함수 밖에 둬서 오류가 났었다.(함수 밖에둬서 계속 visited리스트가 갱신된채 dfs가 계속 실행되었다.)
#     stack= [start]
#     while stack:                 # 스택을 이용한 dfs를 구현  
#         removed = stack.pop()
#         visited[removed] = True
#         for i in graph[removed]:
#             if not visited[i]:
#                 if in_out[removed] and in_out[i]:     # 이전 노드가 실내, 현재 노드가 실내일 경우 count+1
#                     count+=1
#                 elif not in_out[removed] and in_out[i]:   # 이전 노드가 실외, 현재노드가 실내일 경우 count+1 
#                     count+=1
#                 else:
#                     stack.append(i)       # 위의 경우가 아닐경우 stack에 append   
#     return count
# result = 0
# for i in range(1,n+1):
#     if in_out[i]:
#         result += dfs(i)
# print(result)

#  
import sys
sys.setrecursionlimit(10**6)        # 재귀 최대 깊이를 최댓값으로 설정  

n  = int(sys.stdin.readline())
a = sys.stdin.readline().strip()
graph = [[] for i in range(n+1)]
in_out = [True]         # 실내 실외 구분 하는 리스트 생성  
for i in a:
    if i =='1':
        in_out.append(True)
    else:
        in_out.append(False)
result = 0
for i in range(n-1):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
    if in_out[x] and in_out[y]:
        result +=2                  # graph를 만들어줄 때 실내에서 실내로 가는 경우 result에 경우에수 +2   // 실내 - 실내 일경우 -> 실외를 거치지 않는 경우  

visited = [False] *(n+1)

def dfs(start):         # 재귀 함수로 dfs구현  
    count = 0       # 실외함수에서 시작함. 실내함수를 만날경우 count+1
    visited[start]= True
    for i in graph[start]:  
        if in_out[i]:                #  실외 - 실내 일경우  -> 실외가 하나(이상)일 경우  
            count+=1
        elif not visited[i] and not in_out[i]:      # 실외 - 실외 일 경우 // dfs연산을 재귀실행  (실외가 떨어져 있을 경우) , 실외가 두개 이상으로 인접하게 있을 경우는 실외가 하나있는 경우와 동일
            count += dfs(i)
    return count
for i in range(1,n+1):
    if not in_out[i] and not visited[i]:        # 방문하지 않은 실외노드만 dfs 함수 실행 
        result1 = dfs(i)                # dfs 연산이후 count 값 => 실외와 연결되어 있는 실내 노드  
        result += result1 *(result1-1)         # 실외노드에 실내 노드가 3개 인접해 있을 경우 == (인접한 실내노드 갯수) * (인접한 실내노드 갯수-1) = 3 * 2 =6
print(result)



