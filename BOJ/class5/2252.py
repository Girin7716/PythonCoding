# 줄 세우기
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
result = []
for i in range(1,N+1):
    if indegree[i] == 0:
        q.append(i)
        result.append(i)

while q:
    now = q.popleft()

    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
            result.append(i)

for x in result:
    print(x,end=' ')