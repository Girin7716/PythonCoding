# 벽 부수고 이동하기
import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
graph = []
for i in range(N):
    temp = input().strip()  # 공백 제거
    graph.append(temp)

#(x,y,벽 부셨는지 확인)
dx = [1,0,-1,0]
dy = [0,1,0,-1]
INF = int(1e9)
dist = [[INF for _ in range(M)] for _ in range(N)]
dist[0][0] = 1
def bfs():
    q = deque()
    q.append((0,0,1))   #x,y,broke

    while q:
        x,y,broke = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if dist[nx][ny] < dist[x][y]:
                continue
            if graph[nx][ny] == '1' and broke == 1:
                q.append((nx,ny,0))
                dist[nx][ny] = dist[x][y] + 1
            elif graph[nx][ny] == '0':
                q.append((nx,ny,broke))
                dist[nx][ny] = dist[x][y] + 1

    if dist[N-1][M-1] == INF:
        return -1
    else:
        return dist[N-1][M-1]

print(bfs())

# 6 4
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000


# 4 4
# 0111
# 1111
# 1111
# 1110

# 5 5
# 01000
# 01000
# 00000
# 00011
# 00010