# 계단 오르기
N = int(input())

data = []
dp = [0] * 301 # python에서 리스트 append의 시간 복잡도는 O(1)
for i in range(N):
    data.append(int(input()))
if N==1:
    print(data[N-1])
    exit()
elif N==2:
    print(data[N-1]+data[N-2])
    exit()
dp[0] = data[0]
dp[1] = max(data[0]+data[1],data[1])
dp[2] = max(data[0]+data[2],data[1]+data[2])
for i in range(3,N):
    dp[i] = max(dp[i-2]+data[i],dp[i-3]+data[i]+data[i-1])
print(dp[N-1])