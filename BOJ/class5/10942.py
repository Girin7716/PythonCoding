# 팰린드롬?
import sys
input = sys.stdin.readline

N = int(input())
data = [0]+list(map(int,input().split()))
M = int(input())

dp = [[0 for _ in range(N+2)] for _ in range(N+2)]

for i in range(1,N+1):
    dp[1][i] = 1
#for i in range(1,N-1):
for i in range(1, N):
    if data[i] == data[i+1]:
        dp[2][i] = 1
    else:
        dp[2][i] = 0

for i in range(3,N+1):
    for j in range(1,N-i+2):
        if data[j] == data[j+i-1] and dp[i-2][j+1] == 1:  #isTrue?
            dp[i][j] = 1

# for i in range(len(dp)):
#     for j in range(len(dp[i])):
#         print(dp[i][j],end=' ')
#     print()

# 쿼리 검사
for i in range(M):
    S,E = map(int,input().split())
    print(dp[E-S+1][S])
