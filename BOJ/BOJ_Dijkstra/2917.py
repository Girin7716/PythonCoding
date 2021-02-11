# 늑대 사냥꾼
import heapq
from collections import deque

N,M = map(int,input().split())
board = []
tree_dist = [[0 for _ in range(M)] for _ in range(N)]
tree = []
for i in range(N):
    board.append(list(input()))
    for j in range(M):
        if board[i][j] == '+':  # tree
            tree.append((i,j))
        if board[i][j] == 'V':
            R,C = i,j
        if board[i][j] == 'J':
            finx,finy = i,j

# 각각의 좌표에서 나무의 최소 거리 구하기
q = deque(tree)
dx = [1,0,-1,0]
dy = [0,1,0,-1]

# while q:
#     x,y = q.popleft()
#     for d in range(4):
#         nx,ny = x+dx[d],y+dy[d]
#         if not (0<=nx<N and 0<=ny<M):   continue
#         if tree_dist[nx][ny] != 0: continue
#         tree_dist[nx][ny] = tree_dist[x][y] + 1
#         q.append((nx,ny))
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M and tree_dist[nx][ny] == 0:
            tree_dist[nx][ny] = tree_dist[x][y] + 1
            q.append((nx,ny))

for A,B in tree:
    tree_dist[A][B] = 0

# for i in range(len(tree_dist)):
#     for j in range(len(tree_dist[i])):
#         print(tree_dist[i][j],end=' ')
#     print()

q = []
min_dist = -tree_dist[R][C]
heapq.heappush(q,(min_dist,R,C))
visited = [[0]*M for i in range(N)]
visited[R][C] = tree_dist[R][C]
result = 0
while q:
    min_dist,R,C = heapq.heappop(q)
    min_dist = -min_dist
    for i in range(4):
        nx = R + dx[i]
        ny = C + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            rem = min(min_dist,tree_dist[nx][ny])
            if visited[nx][ny] < rem:
                visited[nx][ny] = rem
                heapq.heappush(q,(-rem,nx,ny))

print(visited[finx][finy])

# for i in range(len(visited)):
#     for j in range(len(visited[i])):
#         print(visited[i][j],end=' ')
#     print()

# 4 4
# +...
# ...+
# ....
# V..J

# 4 4
# +...
# ...+
# .J..
# ...V