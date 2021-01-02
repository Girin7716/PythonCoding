# 정수 삼각형 / p376 / DP
# 책에서 푼 방법
# n = int(input())
# dp = []
#
# for _ in range(n):
#     dp.append(list(map(int,input().split())))
# print(dp)
# # 다이나믹 프로그래밍으로 두 번째 줄부터 내려가면서 확인
# for i in range(1,n):
#     for j in range(i+1):
#         if j == 0:
#             up_left = 0
#         else:
#             up_left = dp[i-1][j-1]
#         # 바로 위에서 내려오는 경우
#         if j == i:
#             up = 0
#         else:
#             up = dp[i-1][j]
#         # 최대 합을 저장
#         dp[i][j] = dp[i][j] + max(up_left, up)
#
# print(max(dp[n-1]))
#

# 내가 푼 방법
N = int(input())
data = []
dummy = [[0 for _ in range(i+1)] for i in range(N)]
for i in range(N):
    data.append(list(map(int,input().split())))
dummy[0][0] = data[0][0]
for i in range(N):
    for j in range(i+1):
        # check left ==> [?+1][?]
        if i+1 < N and dummy[i+1][j] < dummy[i][j] + data[i+1][j]:
            dummy[i+1][j] = dummy[i][j] + data[i+1][j]
        # check right ==? [?+1][?+1]
        if i+1<N and j+1<N and dummy[i+1][j+1] < dummy[i][j] + data[i+1][j+1]:
            dummy[i+1][j+1] = dummy[i][j] + data[i+1][j+1]

print(max(dummy[N-1]))

# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5