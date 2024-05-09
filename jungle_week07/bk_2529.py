# 부등호   
# 스택 두개를 사용하여 풀이하였다.  
import sys

k = int(sys.stdin.readline())

new = list(map(str,sys.stdin.readline().split()))  

maxi = ""   # 최댓값
mini = ""   # 최솟값
stk1 = ['0','1','2','3','4','5','6','7','8','9']
stk2 = []
for i in new:
    if i == ">":        # ">" 일 경우 stk1에서 pop한 값을 maxi에 더해주었다. 
        removed = stk1.pop()
        maxi+=removed
        while stk2:         # 이때 stk2에 값이 있다면 모두 maxi에 넣어주자  
            removed = stk2.pop()
            maxi+=removed
    else:       # 부등호가 "<"일 경우 st1에서 pop한 값을 stk2에 넣자   
        removed = stk1.pop()        
        stk2+=removed
if stk2:                # for 문 이후 stk2가 비어있지 않을 경우도 위와 동일하게 처리하였다.  
    removed = stk1.pop()
    maxi+=removed
    while stk2:
        removed= stk2.pop()
        maxi+=removed
for i in range(k+1-len(maxi)):          # maxi의 길이가 주어진 조건보다 작을 수 있으므로 k+1개 만큼이 채워지도록 maxi 값을 채워주었다.  
    removed = stk1.pop()
    maxi+=removed

# 최솟값을 구하는 과정은 위의 최댓값을 구하는 과정과 동일하다.  
new_stk1 = ['9','8','7','6','5','4','3','2','1','0']
for i in new:
    if i == "<":
        removed = new_stk1.pop()
        mini+=removed
        while stk2: 
            removed = stk2.pop()
            mini+=removed
    else:
        removed = new_stk1.pop()
        stk2+=removed
if stk2:
    removed = new_stk1.pop()
    mini+=removed
    while stk2:
        removed= stk2.pop()
        mini+=removed
for i in range(k+1-len(mini)):
    removed = new_stk1.pop()
    mini+=removed

print(maxi)
print(mini)