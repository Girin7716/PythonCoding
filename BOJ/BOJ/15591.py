# MooTube(Silver)
import sys
from collections import deque
input = sys.stdin.readline

N,Q = map(int,input().split())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    p,q,r = map(int,input().split())
    graph[p].append((r,q))
    graph[q].append((r,p))

def bfs(k,v):
    queue = deque()
    visited = [False] * (N+1)
    answer = 0

    queue.append(v)

    while queue:
        now = queue.popleft()
        visited[now] = True
        for cost,nxt in graph[now]:
            if visited[nxt] is True:
                continue

            if cost >= k:
                answer+=1
                queue.append((nxt))

    return answer


for i in range(Q):
    k,v = map(int,input().split())
    print(bfs(k,v))



# 4 3
# 1 2 3
# 2 3 2
# 2 4 4
# 1 2
# 4 1
# 3 1

# 5 3
# 1 2 3
# 2 3 2
# 2 4 4
# 2 5 4
# 1 2
# 4 1
# 3 1