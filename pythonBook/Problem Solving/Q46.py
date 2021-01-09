# 아기 상어 / p402 / 2020년 상반기 삼성전자 기출문제
from collections import deque


N = int(input())
graph = []
now_x = 0
now_y = 0
for i in range(N):
    graph.append(list(map(int,input().split())))
    for j in range(N):
        if graph[i][j] == 9:
            now_x = i
            now_y = j


eat_cnt = 0
size = 2

while True:























# from collections import deque
# INF = int(1e9)
#
# n = int(input())
# graph = []
# for i in range(n):
#     graph.append(list(map(int,input().split())))
#
# size = 2
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 9:
#             now_x,now_y = i,j
#             graph[i][j] = 0
#
# result = 0
# eat_cnt = 0
#
# def find(dist):
#     x,y = 0,0
#     min = INF
#     for i in range(n):
#         for j in range(n):
#             if dist[i][j] != -1 and 1 <= graph[i][j] and graph[i][j] < size:
#                 if dist[i][j] < min:
#                     x,y = i,j
#                     min = dist[i][j]
#     if min == INF:
#         return None
#     else:
#         return x,y,min
#
# def bfs():
#     dist = [[-1] * n for _ in range(n)]
#     q = deque()
#     q.append((now_x,now_y))
#     dist[now_x][now_y] = 0
#
#     while q:
#         x,y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<n and 0<=ny<n:
#                 if dist[nx][ny] == -1 and graph[nx][ny] <= size:
#                     dist[nx][ny] = dist[x][y] + 1
#                     q.append((nx,ny))
#     return dist
#
# while True:
#     value = find(bfs())
#     if value == None:
#         print(result)
#         break
#     else:
#         now_x,now_y = value[0],value[1]
#         result += value[2]
#
#         graph[now_x][now_y] = 0
#         eat_cnt += 1
#         if eat_cnt == size:
#             size+=1
#             eat_cnt=0
#







# 3
# 0 0 0
# 0 0 0
# 0 9 0

# 3
# 0 0 1
# 0 0 0
# 0 9 0

# 4
# 4 3 2 1
# 0 0 0 0
# 0 0 9 0
# 1 2 3 4