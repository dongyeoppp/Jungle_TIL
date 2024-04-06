# LCS   

import sys

n = sys.stdin.readline().strip()
m = sys.stdin.readline().strip()  
n1 = len(n)     # 문자열 길이 저장  
m1 = len(m)         
new = [[0]*(m1+1) for i in range(n1+1)]     # 같은 문자열이 나올 때 공통 부분 문자열의 길이 +1   
for i in range(1,n1+1):
    for j in range(1,m1+1):                 # new 행렬 리스트와 행의 수와 열의 수를 꼭 맞춰주어야 indexerror가 나지 않는다.  
        if n[i-1] == m[j-1]:                    # 문자열이 같을 경우 
            new[i][j] = new[i-1][j-1]+1         
        else:
            new[i][j] = max(new[i-1][j],new[i][j-1])        # 문자열이 다를 경우 .. 저장된 값을 이용하여 new 행렬 갱신   
print(new[n1][m1])

