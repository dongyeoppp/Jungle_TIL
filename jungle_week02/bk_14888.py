# 연산자 끼워넣기   
# 연산자 순서는 고정하고 숫자만 바꿔준다. dfs 알고리즘을 사용했다.  
import sys
maxi = -float('inf')
mini = float('inf')
n = int(sys.stdin.readline())

number_list = list(map(int, sys.stdin.readline().split()))          

add, sub, mul, div = list(map(int, sys.stdin.readline().split()))           

def dfs(num, idx, add,sub,mul,div):
    global maxi, mini
    if n == idx:            # dfs 종료 조건 으로 재귀 함수가 호출 될 때마다 idx변수에 +1을 더해서 n(숫자 개수) 와 같아지면 재귀 함수를 종료한다.  
        maxi = max(maxi,num)
        mini = min(mini,num)            # 재귀 함수를 호출할때마다 최댓값과 최솟값을 갱신해준다.  
        return
    else:
        if add > 0:
            dfs(num+number_list[idx],idx+1,add-1,sub,mul,div)       # 재귀함수를 호출할때마다 해당 연산기호에 -1  ,num+number_list[idx]은 현재값과 다음값을 연산  
        if sub > 0:
            dfs(num-number_list[idx],idx+1,add,sub-1,mul,div)
        if mul > 0:
            dfs(num*number_list[idx],idx+1,add,sub,mul-1,div)
        if div > 0:
            dfs(int(num/number_list[idx]),idx+1,add,sub,mul,div-1)          # int(num/number_list[idx])으로 처리할 경우 num 값이 음수일 경우에도 몫이 잘 출력된다.  


dfs(number_list[0],1,add,sub,mul,div)       # 주어진 숫자의 첫번째 값과 index =1로 dfs함수를 처음 실행한다.  
        
print(maxi)                 # 재귀 함수가 다 끝났을 경우 maxi,mini값은 전역변수이므로 업데이트 된 값이 들어있다.  
print(mini)