# 예상 대진표   

#입출력 예
#   N	A	B	answer
#   8	4	7	3

def solution(n,a,b):
    count = 1
    while True:
        if (a+1)//2 == (b+1)//2:        # 두 참가자가 붙게 되는 경우 
            return count
        a = (a+1) // 2
        b = (b+1) // 2
        count+=1