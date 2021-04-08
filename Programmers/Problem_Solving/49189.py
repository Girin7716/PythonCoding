# 가장 먼 노드
from collections import deque

def solution(n, edges):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n + 1)
    number = [0] * (n + 1)
    for edge in edges:
        a,b = edge
        graph[a].append(b)
        graph[b].append(a)

    q = deque()
    q.append(1)
    visited[1] = True
    max_value = 0

    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] is True:
                continue
            visited[i] = True
            q.append(i)
            number[i] = number[now] + 1
            if number[i] > max_value:
                max_value = number[i]

    for n in number:
        if n == max_value:
            answer+=1

    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))