# 만들 수 없는 금액 / p314 (못 품)
N = int(input())
data = list(map(int,input().split()))

data.sort() # 1 1 2 3 9
count = 1

for x in data:
    if count < x:
        break
    count += x

print(count)

