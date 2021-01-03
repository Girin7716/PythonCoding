# 퇴사 / p377 / DP(못품)
# 책에서 푼 방법
n = int(input())
t = []
p = []
dp = [0] * (n+1)
max_value = 0

for _ in range(n):
    x,y = map(int,input().split())
    t.append(x)
    p.append(y)

for i in range(n-1,-1,-1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time<= n:
        dp[i]=max(p[i]+dp[time],max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)

# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200