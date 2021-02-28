# 경쟁적 전염 / p344 / DFS&BFS, BFS

import heapq

N, K = map(int,input().split())
board = []
for i in range(N):
    board.append(list(map(int,input().split())))
S,X,Y = map(int,input().split())

def get_virus(board,pq,N,pr):
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                heapq.heappush(pq,(pr,board[i][j],i,j))

pq = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]

time = 0
get_virus(board,pq,N,time+1)
while pq:
    time,virus,x,y = heapq.heappop(pq)
    if time == S+1:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and board[nx][ny] == 0:
            board[nx][ny] = virus
            heapq.heappush(pq,(time+1,board[nx][ny],nx,ny))

print(board[X-1][Y-1])
# 시간 초과
# import heapq
#
# N, K = map(int,input().split())
# board = []
# for i in range(N):
#     board.append(list(map(int,input().split())))
# S,X,Y = map(int,input().split())
#
# def get_virus(board,pq,N):
#     for i in range(N):
#         for j in range(N):
#             if board[i][j] != 0:
#                 heapq.heappush(pq,(board[i][j],i,j))
#
# pq = []
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# for i in range(S):  # S초까지 반복
#     get_virus(board,pq,N)
#     while pq:
#         virus,x,y = heapq.heappop(pq)
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<N and 0<=ny<N and board[nx][ny] == 0:
#                 board[nx][ny] = virus
#
# print(board[X-1][Y-1])


#input
# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2

# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 1 2 2