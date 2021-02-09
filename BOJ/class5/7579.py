# 앱
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
byte = [0] + list(map(int,input().split()))
cost = [0] + list(map(int,input().split()))

sc = sum(cost)

dp = [[0 for _ in range(sc+1)] for _ in range(N+1)]

result = sc

for i in range(1,N+1):
    for j in range(sc+1):
        if cost[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],byte[i]+dp[i-1][j-cost[i]])
        if dp[i][j] >= M:
            result = min(result,j)

if M== 0:
    print(0)
else:
    print(result)