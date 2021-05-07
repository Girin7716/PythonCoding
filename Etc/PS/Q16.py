# 연구소
import sys
from itertools import combinations
from collections import deque
import copy
input = sys.stdin.readline

N,M = map(int,input().split())
board = []
for i in range(N):
    board.append(list(map(int,input().split())))

virus = []
comb = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            comb.append((i,j))
        elif board[i][j] == 2:
            virus.append((i,j))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs():
    answer = 0
    temp = copy.deepcopy(board)
    q = deque()
    for v in virus:
        q.append(v)

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx,ny))
    for i in range(N):
        answer += temp[i].count(0)

    return answer


answer = 0
for cb in combinations(comb,3):
    a,b,c = cb
    board[a[0]][a[1]] = 1
    board[b[0]][b[1]] = 1
    board[c[0]][c[1]] = 1

    answer = max(answer,bfs())

    board[a[0]][a[1]] = 0
    board[b[0]][b[1]] = 0
    board[c[0]][c[1]] = 0

print(answer)
