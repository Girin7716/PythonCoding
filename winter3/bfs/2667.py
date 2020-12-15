from collections import deque

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int,input())))
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    danji = 0
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    danji+=1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0<=nx<N and 0<=ny<N):
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                danji+=1
    return danji

result = []
cnt = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt += 1
            result.append(bfs(i,j))

result.sort()
print(cnt)
for i in range(len(result)):
    print(result[i])
