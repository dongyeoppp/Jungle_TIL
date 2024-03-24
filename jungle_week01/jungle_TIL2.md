## 알고리즘 (백준 문제 풀이) 및 cs(computer system 1.4장까지 정리)
* 2024 - 03 -23     
* 9663번 N-Queen 문제 -> 재귀함수, 백트래킹  
    * 첫 번째 시도 코드  
        ```
        import sys

        n = int(sys.stdin.readline().strip())
        queen_list = []
        count = 0

        for j in range(n):
            new = [0] * n
            queen_list.append(new)
                                    # n * n 행렬 만들기 
        def prime(k, h):
            # print(k,h)
            global n, queen_list
            for i in range(k):         
                if queen_list[i][h] == 1:           # 같은 열에 있을 경우 제외 
                    return False
            for j in range(1,h+1):      
                if queen_list[k-j][h-j] == 1:       # 왼쪽 대각선에 있을 경우 제외
                    return False
            for w in range(1,n-h):
                if queen_list[k-w][h+w] == 1:       # 오른쪽 대각선에 있을 경우 제외
                    return False
            return True

        def queen(r):               # r은 같은 행을 의미  
            global count    
            if r == n:
                count += 1      # r == 4 가 되었을 경우 모든 행에 퀸을 놓았으므로 count 값을 올려줌
            for i in range(n):
                if prime(r, i):     # TRUE 반환할 경우
                    queen_list[r][i] = 1        # 해당 행에 퀸을 배치하고 다음행으로 이동
                    queen(r + 1)                   # 다음행에서 다시 함수 재귀   
                    queen_list[r][i] = 0           # 모든 경우에 대한 검사를 마치면 퀸을 놓은 위치에 값 제거 , 백 트래킹!
        queen(0)
        print(count)
        ```  
        * 이중 리스트를 만들어서 구현하였는데 시간초과 결과가 나와 성공하지 못했다. 구글 답안을 참고하였더니 하나의 리스트만으로 구현하면 시간이 줄어들 것 같아서 코드를 수정해 보았다.  
        * 하나의 리스트를 만들어 구현해보았다.  (queen_list[i] = j 일경우 (i,j)에 퀸을 놓았다고 가정하여 푼다 -> 이 방법은 이해가 잘 되지 않아 포기함. 시간도 더 걸리는것 같다.)   
        * 두번째 풀이 코드   
            ```
            import sys
            n = int(sys.stdin.readline())
            count = 0
            check_col = [False] * n     # 같은 열에 퀸이 있는지 검사
            check_left = [False] * (2*n-1)      # 왼쪽 대각선에 퀸이 있는지 검사
            check_right = [False] * (2*n-1)     # 오른쪽 대각선에 퀸이 있는지 검사

            def queen(row):
                global n, count
                if row == n :       # 마지막행을 지나 row 가 n이 되었을때 -> 경우의 수 하나 찾음 -> count  + 1
                    count +=1
                for col in range(n):                                                                            # 왼쪽 대각선이 겹치는 경우는 행과 열의 합이 같음을 이용.
                    if not check_col[col]  and  not check_left[row+col] and not check_right[col - row + n -1]:      # 오른쪽 대각선이 겹치는 경우는 행과 열의 차이가 같음을 이용(음수 값이 나올 수 있으므로 (n-1)값을 더하여 이용)
                        check_col[col] = check_left[row+col] = check_right[col-row+n-1] = True        # 퀸이 겹치는 자리에 없을 경우 true값을 넣어줌
                        queen(row+1)        # rowr값에 +1을 해주어 다음 행 검사로 넘어감. 재귀 함수 사용
                        check_col[col] = check_left[row+col] = check_right[col-row+n-1] = False     # 행 검사를 하며 퀸을 놓을 수 있는 경우가 나오면 False 값을 넣어 리스트의 값들을 초기화
            queen(0)
            print(count)
            ```

* 리스트 정렬하기  
    ```
    a = [1,4,3,2]
    a.sort()        # print(a.sort())를 바로 출력하면 none을 출력하므로 주의해야한다.
    print(a)    # [1,2,3,4] 리스트를 오름차순으로 출력한다.

    b = [1,5,4,2]
    b.sort(reverse=True)        
    print(b)    # [5,4,2,1] 리스트를 내림차순으로 출력한다.
    ```

* CS(ComputerSystem) ~ 1.4장까지 학습하여 정리하였다.  
    * [cs.week01](https://github.com/dongyeoppp/Jungle_TIL/blob/main/jungle_week01/ComputerSystem1.md) 

