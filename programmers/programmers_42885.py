# 구명보트
# 투 포인터로 풀이
# 보트에는 최대 2명만 탈 수 있음!!!
def solution(people, limit):
    people.sort() 
    count = 0
    left = 0
    right = len(people) -1
    while left <= right:
        count +=1
        weight = people[right]
        right -=1
        # 가장 적게 나가는 사람 + 가장 많이 나가는 사람의 합이 limit 보다 작을 경우 두 명 태우기 
        if people[left] + weight <= limit:
            left+=1
    return count