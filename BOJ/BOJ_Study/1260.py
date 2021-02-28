def dfs(v):
    print(v, end=' ')
    visited[v] = 1
    for i in range(N + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)


N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# DFS&BFS -> 스택 or 재귀
dfs(V)
print()
# BFS -> 큐
queue = [V]
visited = [0 for _ in range(N + 1)]
visited[V] = 1
while queue:
    v = queue.pop(0)
    print(v, end=' ')
    for i in range(N + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            visited[i] = 1
            queue.append(i)
