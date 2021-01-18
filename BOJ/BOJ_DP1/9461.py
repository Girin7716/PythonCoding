# 파도반 수열

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for _ in range(int(input())):
    N = int(input())
    if dp[N] != 0:
        print(dp[N])
        continue
    for i in range(6,N+1):
        if dp[i]!=0:
            continue
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[N])