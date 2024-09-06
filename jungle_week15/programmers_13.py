# 택배 배달과 수거하기
# 시간초과 발생
def solution(cap, n, deliveries, pickups):
    result = 0
    distance = n-1
    while distance >= 0:
        delivery = 0
        pickup = 0 
        # distance를 1씩 줄이며 다 보기 때문에 시간초과가 나오는 듯
        while distance >= 0 and deliveries[distance] == 0 and pickups[distance] ==0:
            distance -= 1
        result += ((distance+1)*2)
        for j in range(distance,-1,-1):
            answer1 = deliveries[j]
            answer2 = pickups[j]
            if delivery == cap and pickup == cap:
                break
            if answer1 != 0:
                if cap - delivery >= answer1:
                    delivery+=answer1
                    deliveries[j] = 0
                else:
                    deliveries[j] -= cap-delivery
                    delivery = cap
            if answer2 != 0:
                if cap - pickup >= answer2:
                    pickup+=answer2
                    pickups[j] = 0
                else:
                    pickups[j] -= cap - pickup
                    pickup = cap
    return result


# 다시 푼 풀이  

def solution(cap, n, deliveries, pickups):
    result = 0
    delivery = 0
    pickup = 0 
    for i in range(n-1,-1,-1):
        delivery += deliveries[i]
        pickup += pickups[i]
        # 배달하거나 수거할 택배 상자가 남아 있을 경우 택배 상자가 남지 않을 때 까지 배달하러 가야함 
        while delivery > 0 or pickup > 0:
            delivery -= cap
            pickup -= cap
            result += (i+1) *2
    return result