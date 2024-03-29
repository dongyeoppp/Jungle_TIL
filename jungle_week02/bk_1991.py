# 트리 순회  

import sys 
n = int(sys.stdin.readline())
new = dict()        # 사전안에 연결되어 있는 노드 담기  

for i in range(n):
    a,b,c = sys.stdin.readline().split()
    new[a] = [b,c]
def front(root):        # 전위 순회
    if root != '.':
        print(root,end="")      # 루트
        front(new[root][0])     # 왼쪽 노드 
        front(new[root][1])     # 오른쪽 노드
def mid(root):
    if root != '.':
        mid(new[root][0])       # 왼쪽 노드
        print(root,end="")      # 루트      
        mid(new[root][1])       # 오른쪽 노드  
def last(root):
    if root != '.':
        last(new[root][0])      # 왼쪽 노드  
        last(new[root][1])      # 오른쪽 노드  
        print(root,end="")      # 루트  
front('A')
print()
mid('A')
print()
last('A')