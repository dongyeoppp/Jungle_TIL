# 쿼드트리              # 아직 미완료   
# # 쿼드 트리   

# import sys

# n = int(sys.stdin.readline())
# arr = []
# for i in range(n):
#     arr.append(list(map(int,sys.stdin.readline().strip())))


# row= 0
# col =0
# result = []

# def paper(x,y,m):
#     global result
#     global n
    
#     base = arr[x][y]
#     for i in range(x,x+m):
#         for j in range(y,y+m):
#             if base != arr[i][j]:
#                 return False
#     return True
# while n>=1:
#     print("n:",n)
#     if paper(row,col,n):
#         result.append(arr[row][col])
#     else:
#         n = n//2
#         paper(row,col,n)
#     if paper(row,col+n,n):
#         result.append(arr[row][col])
#     else:
#         n = n//2
#         paper(row,col+n,n)
#     if paper(row+n,col,n):
#         result.append(arr[row][col])
#     else:
#         n = n//2
#         paper(row+n,col,n)
#     if paper(row+n,col+n,n):
#         result.append(arr[row][col])
#     else:
#         n = n//2
#         paper(row+n,col+n,n)
# paper(0,0,n)
# print(result)



# import sys
# input = sys.stdin.readline

# def isAllSame(arr):
#     start = arr[0][0]
#     for a in arr:
#         for x in a:
#             if x != start:
#                 return False
#     return True

# n = int(input())
# init_video = [list(input().strip()) for _ in range(n)]

# def zip(video, size):
#     if isAllSame(video):
#         print(video[0][0], end="")
#     else:
#         print("(", end="")
#         half = size // 2
#         top = video[:half]
#         zip(list(map(lambda x:x[:half], top)), half)
#         zip(list(map(lambda x:x[half:], top)), half)
#         bottom = video[half:]
#         zip(list(map(lambda x:x[:half], bottom)), half)
#         zip(list(map(lambda x:x[half:], bottom)), half)
#         print(")", end="")


# zip(init_video, n)
