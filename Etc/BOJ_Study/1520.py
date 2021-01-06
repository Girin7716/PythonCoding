# 내리막 길
import sys
N,M = map(int,sys.stdin.readline().split())
board = []
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))
travel = [[-1 for _ in range(M)] for _ in range(N)]

# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    if x==0 and y==0:
        return 1
    if travel[x][y] != -1:
        return travel[x][y]

    travel[x][y]=0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if board[nx][ny] > board[x][y]:
            travel[x][y]+=dfs(nx,ny)
    return travel[x][y]


print(dfs(N-1,M-1))