# 전깃줄
N = int(input())
wire = []
for _ in range(N):
    wire.append(list(map(int,input().split())))

wire.sort()
dp = [1] * (N)

for i in range(N):
    for j in range(i):
        if wire[i][1] > wire[j][1]:
            dp[i] = max(dp[i],dp[j]+1)
print(N-max(dp))
