# 이모티콘 할인 행사 
# 중복 순열을 사용하여 풀이 
from itertools import product 
def solution(users, emoticons):
    def user():
        answer = []
        # 모든 할인율 조합
        for i in all_combinations:
            result1 = 0
            result2 = 0
            for j in users:
                price = 0
                for k in range(len(i)):
                    # 이모티콘 할인율이 user의 할인율 기준 보다 높을 경우 
                    if j[0] <= i[k]:
                        price += emoticons[k] * (1-i[k]/100)
                # 일정 가격 이상일 경우 서비스 가입
                if price >= j[1]:
                    result1+=1
                # 아닐 경우 이모티콘 판매액 증가 
                else:
                    result2+=price
            # answer에 모든 할인율에 대한 결과값을 추가 
            answer.append((result1,result2))
        return answer
    
    discount_rates = [40, 30, 20, 10]
    # 가능한 모든 할인율 조합 생성 (repeat이란 속성 값을 사용함)
    all_combinations = list(product(discount_rates, repeat=len(emoticons)))
    answer = user()
    # 판매액을 기준으로 정렬 
    new_answer = sorted(answer,key = lambda x:x[1])
    # 서비스 가입자 기준으로 정렬 
    new_answer.sort()
    result1, result2 = new_answer.pop()
    return [result1,result2]