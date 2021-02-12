# 행렬 곱셈 순서
import sys
input = sys.stdin.readline

N = int(input())
d = []
for i in range(N):
    r,c = map(int,input().split())
    d.append(r)
    if i==N-1:
        d.append(c)
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for diagonal in range(1,N):
    for i in range(1,N-diagonal+1):
        j=i+diagonal
        dp[i][j] = 2**31
        for k in range(i,j):
            dp[i][j] = min(dp[i][j],dp[i][k]+dp[k+1][j]+(d[i-1]*d[k]*d[j]))

print(dp[1][N])