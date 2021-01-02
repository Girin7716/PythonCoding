# 금광 / p375 / DP
# # 내가 푼 방법
from collections import deque

T = int(input())

dx = [-1,0,1] # 왼위, 왼, 왼아래
dy = [-1,-1,-1]

for i in range(T):
    queue = deque()
    n,m = map(int,input().split())
    data = [[] for i in range(n)]
    str = list(map(int,input().split()))
    for i in range(n):
        for j in range(m):
            data[i].append(str[(i*m) + j])

    answer = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        answer[i][m - 1] = data[i][m - 1]
        queue.append((i,m-1))
    while queue:
        #print(answer)
        x,y = queue.popleft()
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and answer[nx][ny] < answer[x][y] + data[nx][ny]:
                answer[nx][ny] = answer[x][y]+data[nx][ny]
                queue.append((nx,ny))

    max = 0
    for i in range(n):
        if max < answer[i][0]:
            max = answer[i][0]
    print(max)


# 책에서 푼 방법
# 테스트 케이스(Test Case) 입력
# for tc in range(int(input())):
#     n,m = map(int,input().split())
#     array = list(map(int,input().split()))
#
#     # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
#     dp = []
#     index = 0
#     for i in range(n):
#         dp.append(array[index:index+m])
#         index += m
#
#     # 다이나믹 프로그래밍 진행
#     for j in range(1,m):
#         for i in range(n):
#             print(dp)
#             # 왼쪽 위에서 오는 경우
#             if i == 0:
#                 left_up = 0
#             else:
#                 left_up = dp[i-1][j-1]
#             # 왼쪽 아래에서 오는 경우
#             if i == n-1:
#                 left_down = 0
#             else:
#                 left_down = dp[i+1][j-1]
#             # 왼쪽에서 오는 경우
#             left = dp[i][j-1]
#             dp[i][j] = dp[i][j] + max(left_up, left_down, left)
#
#
#         result = 0
#         for i in range(n):
#             result = max(result,dp[i][m-1])
#
#     print(result)




# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2