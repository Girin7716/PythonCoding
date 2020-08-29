# 미로 탈출
## 책에서 푼 방법 ##
# from collections import deque
#
# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# # 이동할 네 방향 정의(상,하,좌,우)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#
#     while queue:
#         x, y = queue.popleft()
#         # 현재 위치에서 네 방향으로 위치 확인
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 미로 찾기 공간을 벗어난 경우 무시
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             # 벽인 경우 무시
#             if graph[nx][ny] == 0:
#                 continue
#             # 해당 노드르 처음 방문하는 경우에만 최단 거리 기록
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
#
#     # 가장 오른쪽 아래까지의 최단 거리 반환
#     return graph[n - 1][m - 1]
#
#
# print(bfs(0, 0))

## 내가 푼 방법 ##
# 못 풀었음 #
from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= N or ny <= -1 or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[N-1][M-1]

print(bfs(0, 0))
