# 정확한 순위 / p386 / 최단 경로 문제
N,M = map(int,input().split())
INF = int(1e9)
graph = [[INF for _ in range(N)] for _ in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1
for i in range(N):
    graph[i][i] = 0

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

result = 0
for i in range(N):
    count = 0
    for j in range(N):
        if graph[i][j] != INF or graph[j][i] != INF:
          count+=1
    if count == N:
        result+=1

print(result)

# N, M = map(int,input().split())
# INF = int(1e9)
# graph = [[INF for _ in range(N)] for _ in range(N)]
#
# for i in range(M):
#     a,b = map(int,input().split())
#     graph[a-1][b-1] = 1
#     graph[i][i] = 0
#
# for k in range(N):
#     for a in range(N):
#         for b in range(N):
#             graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
#
# result = 0
# for i in range(N):
#     count = 0
#     for j in range(N):
#         if graph[i][j] != INF or graph[j][i]!=INF:
#             count += 1
#     if count == N:
#         result +=1
#
# print(result)

# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4