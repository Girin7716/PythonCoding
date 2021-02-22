# 게임 개발
from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
weight = [[]]
indegree = [0] * (N+1)
reverse_graph = [[] for _ in range(N+1)]

for i in range(1,N+1):
    weight.append(list(map(int,input().split())))
    for j in range(1,len(weight[i])-1):
        indegree[i] += 1
        graph[weight[i][j]].append(i)
        reverse_graph[i].append(weight[i][j])

q = deque()

#result = [int(1e9)] * (N+1)
result = [-1] * (N+1)
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
            #result[next] = min(result[next],result[now]+weight[next][0])
            #result[next] = max(result[next], result[now] + weight[next][0])
            for i in reverse_graph[next]:
                result[next] = max(result[next],result[i] + weight[next][0])


for i in result[1:]:
    print(i)

# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

# 5
# 10 -1
# 10 1 4 5 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1