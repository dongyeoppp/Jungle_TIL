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

# 장난감 조립  
# import sys 

# n = int(sys.stdin.readline())

# m = int(sys.stdin.readline())
# graph = [[] for i in range(n+1)]
# for i in range(m):
#     a,b,c = map(int,sys.stdin.readline().split())
#     graph[a].append((b,c))
# indgree= []
# for i in range(1,len(graph)):
#     if graph[i] == []:
#         indgree.append(i)
# dp = [[0]*(n+1) for i in range(n+1)]
# for i in indgree:
#     for j in range(1,n):
#         if i>=j:
#             dp[i][j] +=1
    
# print(dp)
# print(graph)
# count = -1
# for i in graph:
#     count+=1
#     if i !=[]:
#         for j in range(len(i)):
#             print(count,i[j][0])
#             dp[count][i[j][0]] += dp[count-1][i[j][0]] * i[j][1]
# print(dp)   


