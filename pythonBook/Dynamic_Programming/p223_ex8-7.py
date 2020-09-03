# 바닥 공사
# 풀이시간 20분 / 시간 제한 1초 / 메모리 제한 128MB
## 책에서 푼 방법 ##
n = int(input())
d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3,n+1):
    d[i] = (d[i-1] + 2 * d[i-2]) % 796796

print(d[n])

## 내가 푼 방법 ##
# N=int(input())  # 1<=N<=1000
#
# dp = [0] * (N+1)
#
# dp[1] = 1
# dp[2] = 3
#
# for i in range(3,N+1):
#     dp[i] = (dp[i-1] + dp[i-2]*2) 796796
#
# print(dp[N])