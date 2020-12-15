# 2178번 미로탐색
from collections import deque

N,M = map(int,input().split())
graph = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(N):
    graph.append(list(map(int,input())))

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0<=nx<N and 0<=ny<M):
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[N-1][M-1]

print(bfs(0,0))
# from collections import deque
#
# N,M = map(int,input().split())
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
#
# graph = []
# for i in range(N):
#     graph.append(list(map(int,input())))
#
# queue = deque()
# queue.append((0,0))
# while queue:
#     x,y = queue.popleft()
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx <=-1 or nx>=N or ny<=-1 or ny >= M:
#             continue
#         if graph[nx][ny] == 0:
#             continue
#         if graph[nx][ny] == 1:
#             graph[nx][ny] = graph[x][y] + 1
#             queue.append((nx,ny))
#
# print(graph[N-1][M-1])