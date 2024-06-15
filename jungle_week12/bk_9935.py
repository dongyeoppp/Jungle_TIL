# 문자열 폭발 
# 스택을 사용하여 풀이하였다. 
import sys

base_str = sys.stdin.readline().strip()     # 기존 문자열   
bomb_str = list(map(str,sys.stdin.readline().strip()))      # 폭발 문자열 

stk = []
for i in base_str:
    stk.append(i)
    # print(stk[-len(bomb_str):])   // 리스트의 끝에서 len(bomb_str)번째 부터 마지막 요소 까지 출력 
    if stk[-len(bomb_str):] == bomb_str:        # 리스트의 끝에서 len(bomb_str)번째 부터 마지막 요소와 폭발 문자열 비교
        for j in range(len(bomb_str)):      # 폭발 문자열이라면 stack에서 폭발 문자열 길이만큼 pop()
            stk.pop()
            
if stk == []:       # 스택이 비어있을 경우 
    print("FRULA")
else:               # 스택이 비어있지 않을 경우 리스트를 문자열 형태로 바꾸어 출력 
    print(*stk,sep="")