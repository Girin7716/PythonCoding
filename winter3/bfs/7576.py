#7576 토마토
from collections import deque

M,N = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

queue = deque()

def bfs(queue):
    max = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0<=nx<N and 0<=ny<M):
                continue
            if box[nx][ny] != 0:
                continue
            if box[nx][ny] == 0:
                box[nx][ny]=box[x][y]+1
                if max < box[nx][ny]:
                    max = box[nx][ny]
                queue.append((nx,ny))

    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return -1
    if max==0:
        return 0
    return max-1



for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i,j))

result = bfs(queue)
print(result)

# 시간 복잡도가 망한듯
# from collections import deque
#
# M,N = map(int,input().split())
# box = [list(map(int, input().split())) for _ in range(N)]
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# time = 0
# before_zero = 0
# queue = deque()
#
# while True:
#     zero_cnt = 0
#     check = 0
#     for x in range(N):
#         for y in range(M):
#             if box[x][y] == 1:
#                 queue.append((x, y))
#             if box[x][y] == 0:
#                 zero_cnt += 1
#
#     if zero_cnt == 0:
#         print(time)
#         break
#     if zero_cnt == before_zero:
#         print("-1")
#         break
#
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if not (0<=nx<N and 0<=ny<M):
#                 continue
#             if box[nx][ny] == 1 or box[nx][ny] == -1:
#                 continue
#             if box[nx][ny] == 0:
#                 box[nx][ny] = 1
#     before_zero = zero_cnt
#     time += 1