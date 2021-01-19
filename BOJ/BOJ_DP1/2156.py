# 포도주 시식
n = int(input())
graph = [0]
for i in range(n):
    graph.append(int(input()))
dp = [0] * (n+1)

if n == 1:
    print(graph[1])
    exit()
elif n == 2:
    print(graph[1]+graph[2])
    exit()

dp[1] = graph[1]
dp[2] = graph[1]+graph[2]

for i in range(3,n+1):
    dp[i] = max(graph[i]+graph[i-1]+dp[i-3],graph[i]+dp[i-2],dp[i-1])

if dp[n] > dp[n-1]:
    print(dp[n])
else:
    print(dp[n-1])