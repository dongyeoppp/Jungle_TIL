# 바닥 장식 (2주차 시험) 
# 문자열로 받아 split하는 방법을 생각했다.

import sys

n , m = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(sys.stdin.readline().strip())

count = 0
for i in range(n):
    result = graph[i].split("|")
    for j in result:
        if j != "":     # 'ㅣ'를 기준으로 'ㅡ'을 세었다.
            count +=1       # 'ㅡ'타일 count +1
for i in range(m):
    new = []
    for j in range(n):
        new+=graph[j][i]        # 같은 열에 있는 타일을 받음  
        new1 = ""           
    for k in range(len(new)):
        new1+=new[k]            # 같은열의 타일만 문자열로 받음  
    result = new1.split("-")    # 'ㅡ'을 기준으로 나눠 카운트 
    for h in result:
        if h !="":
            count+=1                # 'ㅣ'타일 count +1
print(count)