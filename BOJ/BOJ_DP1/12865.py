# 평범한 배낭

import sys

input = sys.stdin.readline

N, K = map(int,input().split())

weights = [0]
values = [0]
for _ in range(N):
    w, v = map(int,input().split())
    weights.append(w)
    values.append(v)

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(K,0,-1):
        if j - weights[i] >= 0:
            dp[i][j] = max(dp[i - 1][j], values[i] + dp[i - 1][j - weights[i]])
        else:
            dp[i][j] = dp[i-1][j]
print(max(dp[N]))