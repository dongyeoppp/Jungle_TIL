# 시소 짝꿍

def solution(weights):
    dic = {}
    for i in weights:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] +=1
    result = 0
    # 무게 쌍의 개수 더하기 
    for i in dic:
        # weights 리스트에 동일한 무게가 2개 이상 존재 할 경우
        if dic[i] > 1:
            result += (dic[i] * (dic[i]-1)) // 2
        # weights 리스트에 3:2 비율의 무게가 존재 할 경우 
        if i*3/2 in dic:
            result += dic[i] * dic[i*3/2]
        # weights 리스트에 1:2(2:4) 비율의 무게가 존재 할 경우 
        if i*2 in dic:
            result += dic[i] * dic[i*2]
        # weights 리스트에 4:3 비율의 무게가 존재 할 경우 
        if i*4/3 in dic:
            result += dic[i] * dic[i*4/3]
    return result
                