# 로봇 청소기
from itertools import permutations
from collections import deque

while True:
    q = []
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    board = []
    ox,oy = -1,-1
    for i in range(h):
        board.append(list(input()))
        for j in range(w):
            if board[i][j] == 'o':
                ox,oy = i,j
            if board[i][j] == '*':
                q.append((i,j))

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    def bfs(x,y,dist_x,dist_y):
        global w,h
        dist = [[0 for _ in range(w)] for _ in range(h)]
        q = deque()
        q.append((x,y))
        sx,sy = x,y
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx == dist_x and ny == dist_y:
                    dist[nx][ny] = dist[x][y] + 1
                    return dist[nx][ny]
                if nx < 0 or nx >= h or ny < 0 or ny >=w or board[nx][ny] == 'x' or dist[nx][ny] != 0:
                    continue
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))
        return int(1e9)

    per = list(permutations(q,len(q)))
    result = int(1e9)

    for pe in per:
        temp = 0
        temp += bfs(ox,oy,pe[0][0],pe[0][1])
        for i in range(len(pe)-1):
            if result <= temp:
                break
            temp += bfs(pe[i][0],pe[i][1],pe[i+1][0],pe[i+1][1])
        result = min(result,temp)
    if result >= int(1e9):
        print(-1)
    else:
        print(result)
# 4 4
# ..o.
# ****
# ****
# .**.
