# 문자열
# bfs

def bfs():
    mx = 0
    q = set()
    q.add((0,0,board[0][0]))
    while q:
        x,y,sentence = q.pop()
        mx = max(mx,len(sentence))
        if mx == 26:
            return 26
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if board[nx][ny] in sentence:
                continue
            q.add((nx,ny,sentence+board[nx][ny]))
    return mx

R,C = map(int,input().split())
board = []
for i in range(R):
    board.append(list(input()))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

print(bfs())

# dfs(알파벳 같은 경우는 비트마스킹으로 해결하자)
# def solve(x,y,l):
#     global ans
#     ans = max(ans,l)
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0<=nx<R and 0<=ny<C and alpha[table[nx][ny]] == 0:
#             alpha[table[nx][ny]] = 1
#             solve(nx,ny,l+1)
#             alpha[table[nx][ny]] = 0
#
# R, C = map(int,input().split())
# table = []
# for i in range(R):
#     table.append(list(map(lambda x:ord(x)-65, input().rstrip())))
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# alpha = [0] * 26
# ans = 0
# alpha[table[0][0]] = 1
# solve(0,0,1)
#
# print(ans)