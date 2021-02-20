# # 텀 프로젝트
import sys
from _collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(sys.stdin.readline())
    graph = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    indegree = [0] * (n + 1)

    for v in graph[1:]:
        indegree[v] += 1

    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    visit = [False] * (n+1)
    noCycleNode = set()
    while q:
        a = q.popleft()
        noCycleNode.add(a)

        indegree[graph[a]] -= 1
        if indegree[graph[a]] == 0:
            q.append(graph[a])

    print(len(noCycleNode))