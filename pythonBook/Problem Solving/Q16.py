# 연구소 / p341 / DFS, BFS 문제
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

def safe_area(graph, a, b, c):  # a,b,c 는 새울 벽 위치
    graph[a[0]][a[1]] = 1
    graph[b[0]][b[1]] = 1
    graph[c[0]][c[1]] = 1

    queue = deque()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # queue에 바이러스 위치 넣기
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 2:
                queue.append((i, j))
    # bfs 돌리기
    rem = []
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                rem.append((nx,ny))
                queue.append((nx, ny))

    # 0인 safe_area 개수 세기
    cnt = 0
    for i in graph:
        for j in i:
            if j == 0:
                cnt += 1

    # graph 복구
    graph[a[0]][a[1]] = 0
    graph[b[0]][b[1]] = 0
    graph[c[0]][c[1]] = 0
    for x,y in rem:
        graph[x][y] = 0
    return cnt

comb = []
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 0:
            comb.append((i,j))

max_safe = 0
for x in list(combinations(comb,3)):
    rem = safe_area(graph,x[0],x[1],x[2])
    if max_safe < rem:
        max_safe = rem

print(max_safe)

# max_safe = 0
# max_wall = 0
# wall = []
# for i in range(len(graph)):
#     for j in range(len(graph[i])):
#         if graph[i][j] == 0 and max_wall<4:
#             wall.append((i,j))
#             max_wall+=1
#         if max_wall > 3:
#             rem = safe_area(graph, wall[0], wall[1], wall[2])
#             if max_safe < rem:
#                 max_safe = rem
#             wall.pop()
#             max_wall -= 1
# print(max_safe)
#


# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0

# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2

# 8 8
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
