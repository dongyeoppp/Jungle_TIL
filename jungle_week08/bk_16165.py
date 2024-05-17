# 걸그룹 마스터 준석이 
# 두개의 리스트를 만들어 풀이하였다.    
import sys

n,m = map(int,sys.stdin.readline().split()) 
g_grup = []       # 걸그룹 이름 
g_member = []       # 걸그룹 인원

for i in range(n):
    g_name = sys.stdin.readline().strip()
    g_grup.append(g_name)
    g_count = int(sys.stdin.readline())
    g_member_base = []
    for i in range(g_count):
        member = sys.stdin.readline().strip()
        g_member_base.append(member)
    g_member_base.sort()        # 정렬해서 넣어줌 
    g_member.append(g_member_base)

for i in range(m):
    name_or_group = sys.stdin.readline().strip()
    number = int(sys.stdin.readline())
    count = 0
    if number == 1:     # 입력으로 1을 받았을 경우 
        for i in g_member:
            if name_or_group in i:
                print(g_grup[count])    
            else:
                count+=1
    else:               # 입력으로 0을 받았을 경우 
        for i in g_grup:
            if name_or_group in i:
                for i in g_member[count]:
                    print(i)
            else:
                count+=1
