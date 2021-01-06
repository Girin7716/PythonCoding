# 숫자 카드 게임
## min() 함수를 이용한 답암
n,m= map(int,input().split())

result = 0
for i in range(n):
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(result,min_value)

print(result)

## 내가 푼 방법 ##
# N,M = map(int,input().split())
# data = []
# for i in range(N):
#     min = 10001
#     rem = list(map(int,input().split()))
#     rem.sort()
#     data.append(rem[0])
#
# data.sort()
# print(data[N-1])
