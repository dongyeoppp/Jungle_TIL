# 영어 끝말잇기

def solution(n, words):
    new = []
    # count로 몇 번째 단어에서 틀렸는지를 체크 
    count = 1
    # 틀린 단어가 있을 경우 check = False
    check = False
    for i in words:
        # 끝말잇기의 첫단어 
        if count == 1 :
            count+=1
            new.append(i)
        else:
            # 끝말잇기 통과 
            if i not in new and new[-1][-1] == i[0]:
                count+=1
                new.append(i)
            # 끝말잇기 실패 
            else:
                # 끝말잇기 실패 시 check = True
                check = True
                break
    # result1 = 틀린사람 번호      
    result1 = count % n
    if result1 == 0:
        result1 = n
    # result2 = 틀린사람이 몇번째에 탈락했는지 
    result2 = count // n 
    if count % n != 0:
        result2 += 1 
    if check:
        return [result1,result2]
    # 아무도 틀리지 않았을 경우 
    else:
        return [0,0]