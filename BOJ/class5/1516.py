# 게임 개발
from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
weight = [[]]
indegree = [0] * (N+1)

for i in range(1,N+1):
    weight.append(list(map(int,input().split())))
    for j in range(1,len(weight[i])-1):
        indegree[i] += 1
        graph[weight[i][j]].append(i)

q = deque()

result = [int(1e9)] * (N+1)
for i in range(1,N+1):
    if indegree[i] == 0:
        q.append(i)
        result[i] = weight[i][0]


while q:
    now = q.popleft()

    for next in graph[now]:
        indegree[next] -= 1

        if indegree[next] == 0:
            q.append(next)
            result[next] = min(result[next],result[now]+weight[next][0])


for i in result[1:]:
    print(i)