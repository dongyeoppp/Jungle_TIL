# 나무 자르기  
# 완전 탐색 활용
# 첫번째 방법은 시간초과로 통과하지 못했다. 
# import sys               

# n, m = map(int,sys.stdin.readline().split())
# tree_list = list(map(int,sys.stdin.readline().split()))
# tree_list.sort(reverse=True)

# cut = tree_list[0]-m

# while True:
#     result = 0
#     for i in tree_list:
#         if cut < i:
#             result += i - cut
#             if result > m:
#                 break
#     if result == m:
#         print(cut)
#         break
#     else:
#         cut+=1 

# 두번째 풀이는 완전탐색을 이용한 코드이다.
import sys

n, m = map(int,sys.stdin.readline().split())
tree_list = list(map(int,sys.stdin.readline().split()))

start = 1
end = max(tree_list)    # start와 end 값을 지정해준다. start와 end 사이의 값들이  절단기를 설정할 수 있는 값의 범위라고 생각하자.     

while start <= end:     
    mid = (start+end) //2       # start와 end 값의 중간 값을 mid로 지장하고 값의 범위를 줄여나간다.
    result = 0 
    for i in tree_list:
        if i > mid :
            result += i - mid       # 나무의 길이가 절단기에 설정된 값보다 클 경우 result에 값을 더해준다.
            if result >= m:
                start = mid +1      # 잘린 나무 길이의 합이 m 보다 커지게 되면 for문을 바로 종료하고 범위를 좁혀준다. 절단기 설정 값을 높여 줘야하므로 start 값을 다시 지정한다.
                break
    if result < m :     # 만약 잘린 나무 길이의 합이 m 보다 작다면 절단기 설정 값을 낮춰줘야하므로 end값을 다시 지정하여 절단기 설정 값을 낮춰준다. 
        end = mid - 1
print(end)      # start가 end값 보다 커질 경우 while문을 종료하고 마지막으로 설정된 end값이 절단기 설정값의 최대값이 된다. 
                # 나무 절단기의 최댓값을 찾는 것이므로 end가 최종 답으로 설정됩니다. 
     
    


    