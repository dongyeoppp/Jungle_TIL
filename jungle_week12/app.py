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


# 휴게소 세우기   

# import sys 
# from collections import deque
# n , m , l = map(int, sys.stdin.readline().split())  
# new = list(map(int,sys.stdin.readline().split()))


# 로프   

# 수 이어 쓰기  

# 벌집2  

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



        







    
    


    
    