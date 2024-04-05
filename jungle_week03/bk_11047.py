# 동전 0  
# greedy 알고리즘 사용하기   
import sys

n,k = map(int,sys.stdin.readline().split())
coin = []
for i in range(n):
    coin.append(int(sys.stdin.readline()))
coin.sort(reverse=True)         # coin 리스트에 내림차순으로(가격이 큰거부터) 화폐단위를 정렬  
count = 0
for j in coin:
    if j <= k :
        count += k // j     # 해당 화페가 k보다 작을 때 나눠서 몫을 count(화폐의 수 +)
        k=k%j       # 나머지를 계속 갱신해주며 남은 금액을 넣어준다.  
    if k ==0:         # 나머지가 0이 될 경우 count 값을 print 해준다.
        break
print(count)


