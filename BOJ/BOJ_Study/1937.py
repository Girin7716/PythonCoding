# 욕심쟁이 판다
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
rem = [[0 for _ in range(n)] for _ in range(n)]
K = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(i,j):
    if rem[i][j] != 0:
        return rem[i][j]
    rem[i][j] = 1
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or board[i][j] >= board[nx][ny]:
            continue
        rem[i][j] = max(rem[i][j],dfs(nx,ny)+1)
    return rem[i][j]

for i in range(n):
    for j in range(n):
        if rem[i][j] == 0:
            K = max(K,dfs(i,j))
print(rem)
print(board)
print(K)