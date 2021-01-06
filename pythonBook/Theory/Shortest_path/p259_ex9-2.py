# 미래 도시
## 책에서 푼 방법
INF = int(1e9)
n,m = map(int,input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x,k = map(int,input().split())

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)


# ## 내가 푼거
# # 입력 받기 및 그래프 설정
# INF = int(1e9)
# N,M = map(int,input().split())
#
# graph = [[INF]*(N+1) for _ in range(N+1)]
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if i==j:
#             graph[i][j] = 0
#
# for i in range(M):
#     a,b = map(int,input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1
#
# X,K = map(int,input().split())
#
# for k in range(1,N+1):
#     for a in range(1,N+1):
#         for b in range(1,N+1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
#
# # 수행된 결과를 출력
# result = graph[1][K] + graph[K][X]
#
# if result >= INF:
#     print(-1)
# else:
#     print(result)
#
# case 1
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# case 3
# 4 2
# 1 3
# 2 4
# 3 4