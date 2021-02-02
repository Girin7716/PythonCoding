# 음악프로그램
from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for i in range(M):
    data = list(map(int,input().split()))
    for j in range(1,data[0]):
        graph[data[j]].append(data[j+1])
        indegree[data[j+1]]+=1

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

if len(result) != N:
    print(0)
else:
    for r in result:
        print(r)