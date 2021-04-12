# 청소년 상어
import copy
import sys
input = sys.stdin.readline

board = [[] for _ in range(4)]
for i in range(4):
    temp = list(map(int,input().split()))
    for j in range(0,8,2):
        board[i].append((temp[j],temp[j+1]-1))  #fishnum, dir

# 방향 : 1~8 -> 0,7
dir = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
answer = 0

def findFish(board,fishNum):
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == fishNum:
                return (i,j)
    return None,None

def fishesMove(board):
    for i in range(1,17):
        x,y = findFish(board,i)
        if x is None and y is None:
            continue

        while True:
            d = board[x][y][1]
            nx = x + dir[d][0]
            ny = y + dir[d][1]
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or board[nx][ny][0] == -1:  # 움직일 수 없음
                d = (d + 1) % 8
                board[x][y] = (i,d)
            else:
                board[x][y] = (i,d)
                break

        if board[nx][ny][0] == 0:  # 물고기가 없음
            board[x][y],board[nx][ny] = (0,0),board[x][y]
        else:  # 해당 자리 물고기와 자리 바꾸기
            board[x][y],board[nx][ny] = board[nx][ny],board[x][y]

def sharkPosition(board,x,y,d):
    pos = []
    while True:
        nx = x + dir[d][0]
        ny = y + dir[d][1]
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            break
        if board[nx][ny] == (0,0):
            x,y=nx,ny
            continue
        pos.append((nx,ny,board[nx][ny][1]))
        x,y=nx,ny

    return pos


def dfs(x,y,total,board):
    global answer
    board = copy.deepcopy(board)

    total += board[x][y][0]
    board[x][y] = (-1,board[x][y][1])

    fishesMove(board)

    pos = sharkPosition(board,x,y,board[x][y][1])

    answer = max(answer,total)
    remDir = board[x][y][1]
    for p in pos:
        nx,ny,nd = p
        board[x][y] = (0,0)
        dfs(nx,ny,total,board)
        board[x][y] = (-1,remDir)

dfs(0,0,0,board)
print(answer)

# 괜히 시간복잡도 좋게할려고했다가 실패..
# import copy
#
# fishes = {}
# board = [[] for _ in range(4)]
# for i in range(4):
#     temp = list(map(int,input().split()))
#     for j in range(0,8,2):
#         board[i].append(temp[j])
#         fishes[temp[j]] = (i,j//2,temp[j+1]-1)   # x,y,dir
#
# # 방향 : 1~8 -> 0,7
# dir = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
# answer = 0
# # print(fishes)
#
# def fishesMove(board,fishes):
#     # global i
#     for i in range(1, 17):
#         if fishes[i] == (-1, -1, -1):
#             continue
#         x, y, d = fishes[i]
#         while True:
#             nx = x + dir[d][0]
#             ny = y + dir[d][1]
#             if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or board[nx][ny] == -1:  # 움직일 수 없음
#                 d = (d + 1) % 8
#             else:
#                 fishes[i] = (x, y, d)
#                 break
#
#         if board[nx][ny] == 0:  # 물고기가 없음
#             board[x][y] = 0
#             board[nx][ny] = i
#             fishes[i] = (nx, ny, d)
#         else:  # 해당 자리 물고기와 자리 바꾸기
#             fishes[board[x][y]], fishes[board[nx][ny]] = (nx, ny, fishes[board[x][y]][2]), (
#             x, y, fishes[board[nx][ny]][2])
#             board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
#
# def sharkMove(board,x,y,d,fishes):
#     pos = []
#
#     while True:
#         nx = x + dir[d][0]
#         ny = y + dir[d][1]
#         if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
#             break
#         sd = fishes[board[nx][ny]][2]
#         pos.append((nx,ny,sd))
#         x,y=nx,ny
#
#     return pos
#
#
#
# def dfs(x,y,total,board,fishes):
#     global answer
#     board = copy.deepcopy(board)
#     fishes = copy.deepcopy(fishes)
#
#     total += board[x][y]
#     nowFish = board[x][y]
#     sharkDir = fishes[board[x][y]][2]
#     fishes[board[x][y]] = (-1,-1,-1)
#     board[x][y] = -1
#
#     fishesMove(board,fishes)
#
#     pos = sharkMove(board,x,y,sharkDir,fishes)
#     if pos == []:
#         return
#
#     answer = max(answer, total)
#     for p in pos:
#         board[x][y] = 0
#         dfs(p[0],p[1],total,board,fishes)
#         fishes[nowFish] = p
#         board[x][y] = -1
#
#
# # # 상어가 (0,0)의 물고기를 먹음
# # shark = (0,0)   # 상어의 좌표
# # sharkDir = fishes[board[0][0]][2]
# # fishes[board[0][0]] = (-1,-1,-1)
# # answer += board[0][0]
# # board[0][0] = -1    # 상어는 -1
# dfs(0,0,0,board,fishes)
# print(answer)