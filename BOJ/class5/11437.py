# LCA
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
depth = [0 for _ in range(N+1)]
parent = [0 for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

q = deque()
q.append(1)
depth[1] = 1
parent[1] = 1
visited[1] = True
while q:
    now = q.popleft()
    for i in tree[now]:
        if visited[i] == False:
            q.append(i)
            visited[i] = True
            depth[i] = depth[now]+1
            parent[i] = now

M = int(input())
for _ in range(M):
    a, b = map(int,input().split())
    while a!=b:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    print(a)