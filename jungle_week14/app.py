#  # z
# import sys

# n,r,c = map(int,sys.stdin.readline().split())

# new = [[0]* 2**n for i in range(2**n)]
# row = 0
# col = 0
# count = 0
# def recur(row,col):
#     if
#         col+=2**n//2
#     elif i ==0:
#         row+=2**n//2
#     elif i ==0:
#         col+=2**n//2
#     elif i ==0:
#         col+=2**n//2
# re(0,0)


# for i in new:
#     print(i)

##############################################################################

# 트리의 지름   

# import sys

# n = int(sys.stdin.readline())
# tree= [[] for i in range(n+1)]
# tree1 = [[] for i in range(n+1)]
# new = []
# for i in range(n-1):
#     a, b, c = map(int,sys.stdin.readline().split())
#     tree[a].append((b,c))
#     tree[b].append((a,c))
#     tree1[a].append((b,c))
# for i in range(1,len(tree1)):
#     if tree1[i] == []:
#         new.append(i)

# def dfs(tree,start,end):
#     global n
#     stack = []
#     count = 0
#     visited = [False] * (n)
#     for i in tree[start]:
#         stack.append(i)
#         visited[i] = True
#     while stack:
#         node, weight = stack.pop()

##############################################################################


# 휴게소 세우기   

# import sys 
# from collections import deque
# n , m , l = map(int, sys.stdin.readline().split())  
# new = list(map(int,sys.stdin.readline().split()))

##############################################################################


# 로프   
##############################################################################


# 수 이어 쓰기  

##############################################################################

# 벌집2  

##############################################################################

# 계란으로 계란치기  

# import sys

# n = int(sys.stdin.readline())
# egg= []
# for i in range(n):
#     power, weight  = map(int,sys.stdin.readline().split())
#     egg.append((power,weight))
# result = -1
# check = set()
# def back(depth,cnt):
#     global result
#     if depth == n:
#         result = max(result,cnt)
#         return result
#     else:


##############################################################################



# 기타 레슨  

# import sys

# n, m = map(int,sys.stdin.readline().split())
# new = list(map(int,sys.stdin.readline().split()))

# start = 0
# end = len(new)-1
# mid = (start+end) // 2
# result = []
# for i in range(m-1):
#     if sum(new[start:mid+1]) < sum(new[mid+1:end+1]):
#         print("111",new[start:mid+1])
#         result.append(sum(new[start:mid+1]))
#         if i == m-2:
#             result.append(sum(new[mid+1:end+1]))
#         start = mid+1
#         mid = (start+end) // 2
        
#     else:
#         result.append(sum(new[mid+1:end+1]))
#         if i == m-2:
#             result.append(sum(new[start:mid+1]))
#         end = mid
#         mid = (start+end) // 2
# print(max(result))


##############################################################################
    
# 로봇 청소기   

# import sys
# from collections import deque
# n , m = map(int,sys.stdin.readline().split())
# room = []
# row, col, d = map(int,sys.stdin.readline().split())
# for i in range(n):
#     room.append(list(map(int,sys.stdin.readline().split())))


# def bfs(room,row,col,d):
#     global n,m
#     que = deque()
#     que.append((row,col,d))
#     count = 1
#     visited = [[False]*m for i in range(n)]
#     visited[row][col] = True
#     up = [0,1,0,-1]     
#     down = [-1,0,1,0]
#     while que:
#         check = True
#         re_row, re_col, re_d = que.popleft()        # re_d 체크 
#         for i in range(4):
#             answer = (4- re_d + i) % 4      # 회전 방향 다시 체크하기 
#             x = re_row + up[answer]
#             y = re_col + down[answer]
#             if 0<= x < n and 0<= y < m and room[x][y] != 1 and not visited[x][y]:
#                 que.append((x,y,re_d))
#                 visited[x][y] = True
#                 count+=1
#                 check = False
#                 break
#     return count

# print(bfs(room,row,col,d))


##############################################################################


# 상자넣기  

# import sys

# n = int(sys.stdin.readline())

# box = list(map(int,sys.stdin.readline().split()))

# stk1 = [0]
# for i in box:
#     if stk1[-1] < i:
#         stk1.append(i)
#     else:
#         while stk1[-1] >= i and i not in stk1:
#             stk1.pop()
#         if i not in stk1:
#             stk1.append(i)

# inf = float('inf')
# stk2 = [inf]
# new_box = box[::-1]

# for i in new_box:
#     if stk2[-1] > i:
#         stk2.append(i)
#     else:
#         while stk2[-1] <= i and i not in stk2:
#             stk2.pop()
#         if i not in stk2:
#             stk2.append(i)
# print(max(len(stk2),len(stk1))-1)
    

# import sys

# n = int(sys.stdin.readline())

# box = list(map(int,sys.stdin.readline().split()))

# dp = []


##############################################################################

# 꿀 따기   

# import sys

# n = int(sys.stdin.readline())
# honey_idx = []
# for i in range(n):
#     honey_idx.append(i)

# honey = list(map(int,sys.stdin.readline().split()))


##############################################################################

# 팰린드롬 만들기   

###############################################################################

# 극장 좌석 

# import sys

# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
# vip = []
# for i in range(m):
#     vip.append(int(sys.stdin.readline()))


###############################################################################

# 알파벳  
##dfs로 해결해보기 

# import sys
# from collections import deque
# r, c = map(int,sys.stdin.readline().split())
# alphabet = []
# for i in range(r):
#     alphabet.append(sys.stdin.readline().strip())

# def bfs(row,col):
#     que = deque([(row, col, 1, {alphabet[row][col]})])
#     # print(new) 
#     # que.append((row,col,1,new))
#     dx = [1,-1,0,0]
#     dy = [0,0,1,-1]
#     result = 0
#     while que:
#         rerow, recol, recount,renew= que.popleft()
#         result = max(result,recount)
#         for i in range(4):
#             x = rerow + dx[i]
#             y = recol + dy[i]
#             if 0<= x < r and 0 <= y < c and alphabet[x][y] not in renew:
#                 new_renew = renew.copy()
#                 new_renew.add(alphabet[x][y])
#                 que.append((x,y,recount+1,new_renew.add(alphabet[x][y])))
                
#     return result

# print(bfs(0,0))


###############################################################################


# 회전 초밥 

# import sys
# from collections import deque 
# n, d, k, c = map(int,sys.stdin.readline().split())
# que = deque()

# for i in range(n):
#     que.append(int(sys.stdin.readline()))

# result = 0
# eat = [False]*(d+1)
# eat[c] = True
# for i in range(n):
#     count =0
#     for j in range(k):
#         removed =que.popleft()
#         if not eat[removed]:
#             eat[removed] = True
#             count+=1
#         que.append(removed)
#     result = max(count,result)
# print(result)

###############################################################################

# 테트로미노 

# import sys
# from collections import deque
# n,m = map(int,sys.stdin.readline().split())
# arr = []
# for i in range(n):
#     arr.append(list(map(int,sys.stdin.readline().split())))

# def bfs(row,col):
#     que = deque()
#     visited=[[False]*m for i in range(n)]
#     result = 0
#     que.append((row,col,1))
#     visited[row][col] = True
#     dx = [1,-1,0,0]
#     dy = [0,0,1,-1]
#     result = 0
#     while que:
#         rerow, recol, depth = que.popleft()
#         result+=arr[rerow][recol]
#         if depth >=4:
#             break
#         save = 0
#         check = 0
#         for i in range(4):
#             x = rerow + dx[i]
#             y = recol + dy[i]
#             if 0<= x < n and 0<= y < m and save < arr[x][y] and not visited[x][y]:
#                 check = ((x,y))
#                 save = arr[x][y]
#         que.append((check[0],check[1],depth+1))
#         visited[check[0]][check[1]] = True
#     return result


# def fuck(row,col):
#     dx = [1,-1,0,0]
#     dy = [0,0,1,-1]
#     result = arr[row][col]
#     answer = float('inf')
#     for i in range(4):
#         x = row + dx[i]
#         y = col + dy[i]
#         if 0<= x < n and 0 <= y < m:
#             result += arr[x][y] 
#             answer = min(answer,arr[x][y])
#     return result-answer


# answer= 0
# for i in range(n):
#     for j in range(m):
#         answer = max(bfs(i,j),answer,fuck(i,j))
# print(answer)

###############################################################################

# 숫자고르기   

###############################################################################

