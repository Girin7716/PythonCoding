# 거스름돈
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
list = [500,100,50,10]

for coin in list:
    count+= n//coin
    n %= coin

print(count)

# 시간 복잡도 O(K) -> 입력값 N과 무관함