# ACM Craft
from collections import deque
import sys
import copy

input = sys.stdin.readline

for tc in range(int(input())):
    N, K = map(int, input().split())
    indegree = [0] * (N + 1)
    delays = list(map(int, input().split()))

    graph = [[] for _ in range(N + 1)]
    for i in range(K):
        a, b = map(int, input().split())
        indegree[b] += 1
        graph[a].append(b)
    W = int(input())

    rem = copy.deepcopy(delays)
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            delays[i - 1] = max(delays[i - 1], delays[now - 1] + rem[i - 1])
            if indegree[i] == 0:
                q.append(i)

    print(delays[W-1])


