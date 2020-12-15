#2606 바이러스
from collections import deque

N = int(input())
M = int(input())

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for i in range(M):
    x,y=map(int,input().split())
    if i==0:
        a,b=x,y
    graph[x][y] = 1
    graph[y][x] = 1
for i in range(len(graph)):
    print(graph[i])

def bfs(a,b):
    cnt = 0
    queue = deque()
    queue.append((a,b))
    while queue:
        x,y = queue.popleft()


    return cnt

print(bfs(a,b))