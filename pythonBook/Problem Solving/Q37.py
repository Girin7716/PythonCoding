# 플로이드 / p385 / 최단 경로 문제
N = int(input())
M = int(input())
INF = int(1e9)
graph = [[INF for _ in range(N)] for _ in range(N)]

for i in range(M):
    a,b,c = map(int,input().split())
    if graph[a-1][b-1] > c:
        graph[a-1][b-1] = c

for i in range(N):
    graph[i][i] = 0


for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(N):
    for j in range(N):
        print(graph[i][j],end=' ')
    print()

# import sys
# input = sys.stdin.readline
#
# INF = int(1e9)
# n = int(input())
# m = int(input())
# graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
#
# for i in range(n):
#     graph[i][i] = 0
#
# for i in range(m):
#     a, b, c = map(int, input().split())
#     if graph[a-1][b-1] > c:
#         graph[a-1][b-1] = c
#
# for k in range(n):
#     for a in range(n):
#         for b in range(n):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
#
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == INF:
#             graph[i][j] = 0
#         print(graph[i][j], end = ' ')
#     print()
# 5
# 14
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4