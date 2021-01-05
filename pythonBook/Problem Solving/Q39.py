# 화성 탐사 / p388 / 최단 경로 문제

import sys
import heapq

INF = int(1e9)
dx = [-1,0,1,0]
dy = [0,-1,0,1]

for tc in range(int(input())):
    N = int(input())
    graph = []
    for i in range(N):
        graph.append(list(map(int,input().split())))
    distance = [[INF for _ in range(N)] for _ in range(N)]

    x,y = 0,0
    distance[x][y] = graph[x][y]
    q=[]
    heapq.heappush(q,(x,y,distance[x][y]))
    while q:
        x,y,dist = heapq.heappop(q)
        if dist > distance[x][y]:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0>nx or nx>=N or 0>ny or ny>=N:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q,(nx,ny,cost))

    print(distance[N-1][N-1])

# import sys
# import heapq
#
# input = sys.stdin.readline
# INF = int(1e9)
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
#
# for tc in range(int(input())):
#     N = int(input())
#     graph = []
#     for i in range(N):
#         graph.append(list(map(int,input().split())))
#
#     distance = [[INF] * N for _ in range(N)]
#
#     x,y=0,0
#     q = [(x,y,graph[x][y])] # x,y로가는 비용이 graph[x][y]
#     distance[x][y] = graph[x][y]    # 큐로 넣을때마다 최단거리로 삽입(값이 더 작다면)
#
#     # 다익스트라
#     while q:
#         x,y,dist = heapq.heappop(q)
#         if distance[x][y] < dist:   # 이미 봤다
#             continue
#         # 현재 노드와 연결된 다른 인접한 노드들을 확인
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx<0 or nx>=N or ny<0 or ny>=N:
#                 continue
#             cost = dist + graph[nx][ny]
#             if cost < distance[nx][ny]:
#                 distance[nx][ny] = cost
#                 heapq.heappush(q,(nx,ny,cost))
#
#     print(distance[N-1][N-1])

# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4