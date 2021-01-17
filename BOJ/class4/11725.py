# 트리의 부모 찾기
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (N+1)

q = deque()
q.append(1)
visited[1] = -1 # root

while q:
    now = q.popleft()
    for i in graph[now]:
        if visited[i] != 0:
            continue
        visited[i] = now
        q.append(i)
for i in range(2,N+1):
    print(visited[i])



