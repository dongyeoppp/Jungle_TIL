## 알고리즘 (백준 문제 풀이)
* 2024 - 03 - 22

파이썬 문법을 어느정도 알고 있다고 생각하여 쉬운 문제부터 먼저 풀어보는 시간을 가졌다.  

* input값 받는 시간 줄이기 
```
n = input()
```  
```
n = sys.stdin.readline().strip()    # 이 방법이 더 빠르다@!
```

* 재귀 함수로 최대공약수 구하기   
```
def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

print(gcd(8,22))    # 2를 출력
```

* 재귀 함수로 recur 순수한 재귀 함수 구현  
```
from stack improt Stack
def recur(n):
    s = Stack(n)

    while True:
        if n>0:
            s.push(n)
            n= n-1
            continue
        if not s.is_empty():
            n = s.pop()
            print(n)
            n = n-2
            continue
        break
```


* 함수 안에서 전역변수 설정
    * global 사용  
    ```
    n  = 0
    def go():
        global n
        n+=1
    go()
    print(n) # 1 출력
    ```

* 9020번 "골드바흐의 추측" [문제](https://www.acmicpc.net/problem/9020) / [내풀이](https://www.acmicpc.net/source/75489624)  
    * 후기 
        * 시간초과 결과가 계속 나와 시간을 많이 쓰게 되었다.
        ```
        n = int(input())
            
        def isPrime(number):            # 소수이면 true 값을 return
            if number == 1:
                return False
            for i in range(2,number):
                if number % i == 0:
                    return False
            return True

        for i in range(n):      # 짝수 입력값만 입력됨. 반으로 나눠서 for문 출력
            num = int(input())
            new_num1 = num // 2
            new_num2 = num // 2
            for k in range(num//2):
                if isPrime(new_num1) and isPrime(new_num2):     # num1과 num2가 소수인 경우
                    print(f"{new_num2} {new_num1}")             # print문 출력
                    break
                else:
                    new_num1 +=1 
                    new_num2 -=1    # 차이가 가장 작아야 하기 때문에 가운데 값으로 나눠주었고 소수가 아닐경우엔 각각+1, -1 해주었다.
        ```

* 1914번 "하노이 탑" [문제](https://www.acmicpc.net/problem/1914) / [내풀이](https://www.acmicpc.net/source/75509319)
    * 후기  
        * 이해하는데 굉장히 어려웠다. 재귀함수를 사용하여 문제를 해결했다.  
        * 하노이 탑의 원판을 옮기는 횟수는 규칙을 가지고 있어 수식으로 표현이 가능했다. -> count = 2**n-1 (원판이 3개일 경우 최소 7번 옮긴다.)  
        * 방법1
        ```
        import sys

        num = int(sys.stdin.readline().strip())     # input 값 받기 => num
        def hanoi(num, start, mid, last):            
        # start는 원판이 꽂혀있는 막대 위치,  last는 원판을 옮길 위치, mid는 원판을 경유할 위치
            if num <= 20:               # numr값이 20이하일 경우에만 함수안에 print문 실행(제한을 하지 않을 시 초과오류 발생)
                if num == 1:
                    print(f"{start} {last}")        # 원판이 1개일 경우 start 위치에서 last 위치로 경유 없이 옮길 수 있으므로 바로 print문을 실행시킨다.
                else:
                    hanoi(num-1, start, last, mid)  # 제일 아래 있는 원판을 last로 보내기 위해 그 위의 n-1개의 원판을 mid로 옮겨야 한다. 
                    print(f"{start} {last}")    # 마지막 원판을 start에서 last로 보낸다.
                    hanoi(num-1, mid, start, last)  # 경유지 mid에 있는 n-1개의 원판을 last로 보낸다. 여기까지의 과정을 반복하며 원판을 옮긴다.
        print(2**num-1)
        hanoi(num,1,2,3)
        ```  
        * 방법2
        ```
        import sys

        num = int(sys.stdin.readline().strip())    
        count = 0
        def hanoi(num, start, last):            
            if num <= 20:              
                if num == 1:
                    print(f"{start} {last}")
                    global count
                    count +=1         
                else :
                    hanoi(num-1, start,6-start-last)   
                    print(f"{start} {last}") 
                    count +=1     
                    hanoi(num-1, 6-start-last, last)  
        hanoi(num,1,3)
        print(count)
        ```
        * start, mid, last를 원판을 꽂는 막대기로 가정하고 원판이 있는 위치와 보내야하는 위치를 가정하여 함수에 값을 변경해주었다.
