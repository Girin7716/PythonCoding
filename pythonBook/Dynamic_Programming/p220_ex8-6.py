# 개미 전사
# 풀이 시간 30분 / 시간 제한 1초 / 메모리 제한 128MB
## 책에서 푼 방법 ##
n = int(input())
array = list(map(int,input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0],array[1])
for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+array[i])

print(d[n-1])

## 내가 푼 방법 ##
# N = int(input())    # 3<=N<=100
# foods = list(map(int,input().split()))  # 0<=식량의 개수<=1000
#
# dp = [0] * (N+1)
#
# dp[1] = foods[0]
# dp[2] = max(foods[0],foods[1])
#
# for i in range(3,N+1):
#     dp[i] = max(dp[i-1],dp[i-2]+foods[i-1])
#
# print(dp[N])