# 빙산

from collections import deque
import sys
input = sys.stdin.readline

N,M=map(int,input().split())
board = []
for i in range(N):
    board.append(list(map(int,input().split())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def check_near_zero(rem):
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx >= 0 and nx < N and ny >= 0 and ny < M and board[nx][ny] == 0:
                        cnt += 1
                rem.append((i,j,cnt))

def melting(rem):
    while rem:
        x,y,cnt = rem.popleft()
        board[x][y] -= cnt
        if board[x][y] <= 0:
            board[x][y] = 0

def bfs(x,y,cnt):
    q = deque()
    q.append((x,y))
    visited[x][y] = cnt

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M and visited[nx][ny] == 0 and board[nx][ny]!=0:
                visited[nx][ny] = cnt
                q.append((nx,ny))


def is_separate():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and visited[i][j] == 0:
                cnt+=1
                bfs(i,j,cnt)

    return cnt

time = 0

while(True):
    time += 1
    rem = deque()   # near_zero 저장 큐
    check_near_zero(rem)
    melting(rem)
    visited = [[0 for _ in range(M)] for _ in range(N)]
    flag = is_separate()

    if flag >= 2:
        print(time)
        break
    elif flag == 0:
        print(0)
        break

# naive (메모리초과)
# import sys
# import copy
# from collections import deque
# input = sys.stdin.readline
#
# N, M = map(int,input().split())
#
# board = []
# for i in range(N):
#     board.append(list(map(int,input().split())))
#
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
#
# def after_year():
#     temp = copy.deepcopy(board)
#
#     for i in range(N):
#         for j in range(M):
#             if board[i][j] != 0:
#                 cnt = 0
#                 for k in range(4):
#                     nx = i + dx[k]
#                     ny = j + dy[k]
#                     if nx >= 0 and nx < N and ny >= 0 and ny < M and board[nx][ny] == 0:
#                         cnt+=1
#                 temp[i][j] = board[i][j] - cnt
#                 if temp[i][j] < 0:
#                     temp[i][j] = 0
#     return temp
#
# def bfs(x,y,cnt):
#     q = deque()
#     q.append((x,y))
#
#     while q:
#         x,y = q.popleft()
#         visited[x][y] = cnt
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx>=0 and nx<N and ny>=0 and ny<M and visited[nx][ny] == 0 and board[nx][ny]!=0:
#                 q.append((nx,ny))
#
# # return 0,1,2 -> 0 : all melt, 1 : one thing, 2 : more than 2
# def is_separate():
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             if board[i][j] != 0 and visited[i][j] == 0:
#                 cnt += 1
#                 bfs(i,j,cnt)
#
#     if cnt > 2:
#         return 2
#     else:
#         return cnt
#
# time = 0
# while(True):
#     visited = [[0 for _ in range(M)] for _ in range(N)]
#     board = after_year()
#     time+=1
#     flag = is_separate()
#     if flag == 0:
#         print(0)
#         break
#     elif flag == 2:
#         print(time)
#         break