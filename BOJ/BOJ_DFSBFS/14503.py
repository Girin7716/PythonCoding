# 로봇 청소기
import sys
input = sys.stdin.readline

N,M=map(int,input().split())
r,c,d = map(int,input().split())

board = []
for i in range(N):
    board.append(list(map(int,input().split())))

def turn_left(d):
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    elif d == 3:
        return 2

def clean(r,c,d):
    answer = 0

    while True:
        # 현재 위치 청소
        if board[r][c] == 0:
            answer += 1
        board[r][c] = 2

        # 왼쪽으로 회전 후 탐색
        check = False
        for i in range(4):
            d = turn_left(d)
            nx = r + dx[d]
            ny = c + dy[d]
            if nx >=0 and nx < N and ny >= 0 and ny < M and board[nx][ny] == 0:
                r = nx
                c = ny
                check = True
                break

        if check == True:   #청소를 했다면
            continue
        else:   # 청소를 못함
            # 후진이 가능
            if d == 0:
                nx = r + 1
                ny = c
            elif d == 1:
                nx = r
                ny = c - 1
            elif d == 2:
                nx = r - 1
                ny = c
            elif d == 3:
                nx = r
                ny = c + 1

            if board[nx][ny] == 1:  # 벽
                break
            else:   # 후진 가능
                r = nx
                c = ny

    return answer

# 0,1,2,3 => 북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]
print(clean(r,c,d))



