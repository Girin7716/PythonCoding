# 주사위 굴리기
import sys

input = sys.stdin.readline
N,M,x,y,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
moveInput = list(map(int,input().split()))
dice = [0 for _ in range(6)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(K):
    dir = moveInput[i] - 1
    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx <0 or nx>= N or ny < 0 or ny >= M:
        continue

    if dir==0:  # 동
        dice[0],dice[3],dice[5],dice[2] = dice[3],dice[5],dice[2],dice[0]
    elif dir==1: # 서
        dice[0],dice[2],dice[5],dice[3] = dice[2],dice[5],dice[3],dice[0]
    elif dir==2:    # 북
        dice[5],dice[4],dice[0],dice[1] = dice[4],dice[0],dice[1],dice[5]
    elif dir==3:    # 남
        dice[5],dice[1],dice[0],dice[4] = dice[1],dice[0],dice[4],dice[5]   # swap 개념인듯..?
        # dice[5] = dice[1]
        # dice[1] = dice[0]
        # dice[0] = dice[4]
        # dice[4] = dice[5]

    if board[nx][ny] == 0:
        board[nx][ny] = dice[5]
    else:
        dice[5] = board[nx][ny]
        board[nx][ny] = 0

    x, y = nx, ny
    print(dice[0])