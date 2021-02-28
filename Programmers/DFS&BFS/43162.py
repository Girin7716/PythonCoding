# 네트워크
from collections import deque

def bfs(i,visited,graph):
    q = deque()
    q.append(i)
    while q:
        now = q.popleft()
        visited[now] = True

        for following in graph[now]:
            if visited[following] is True:
                continue
            q.append(following)

def solution(n, computers):
    answer = 0
    parent = [i for i in range(n+1)]
    graph = [[] for _ in range(n)]
    visited = [False] * n

    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j] == 1:
                graph[i].append(j)

    for i in range(n):
        if visited[i] is True:
            continue
        answer += 1
        bfs(i,visited,graph)

    return answer


print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))