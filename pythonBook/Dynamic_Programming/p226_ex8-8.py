# 효율적인 화폐 구성
# 풀이 시간 30분 / 시간 제한 1초 / 메모리 제합 128MB
## 책에서 푼 방법 ##
n,m = map(int,input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i],m+1):
        if d[j-array[i]] != 10001:  # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j],d[j-array[i]]+1)

# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])

## 내가 푼 방법 ##
# N,M=map(int,input().split())    # 1<=N<=100, 1<=M<=10000
# money_type = []
# for i in range(N):
#     money_type.append(int(input()))
#
# dp = [10001] * (10001)
#
# for i in money_type:
#     dp[i] = 1
#
# for i in range(money_type[0],M+1):
#     if i in money_type:
#         continue
#     min = 100000
#     for j in money_type:
#         if min > dp[i-j]:
#             min = dp[i-j]
#     dp[i] = min + 1
#
# if dp[M] > 10000:
#     print(-1)
# else:
#     print(dp[M])

