# 병사 배치하기 / p380 / DP
N = int(input())
soldier = list(map(int,input().split()))
dp = [1] * (N+2)

for i in range(N):
    for j in range(i):
        if soldier[i]<soldier[j]:
            dp[i] = max(dp[i],dp[j]+1)

#print(max(dp))
print(N-max(dp))
# 7
# 15 11 4 8 5 2 4