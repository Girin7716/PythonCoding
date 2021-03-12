# 녹색 옷 입은 애가 젤다지?
# dijkstra
import heapq
import sys
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 1
while True:
    N = int(input())
    if N == 0:
        break
    graph = [list(map(int,input().split())) for i in range(N)]
    dist = [[int(1e9) for _ in range(N)] for _ in range(N)]
    pq = []
    dist[0][0] = graph[0][0]
    heapq.heappush(pq,(dist[0][0],0,0))

    while pq:
        cost,x,y = heapq.heappop(pq)
        if x == N - 1 and y == N - 1:
            print("Problem {}: {}".format(cnt, cost))
            cnt += 1
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or dist[nx][ny] <= cost+graph[nx][ny]:
                continue

            dist[nx][ny] = cost + graph[nx][ny]
            heapq.heappush(pq,(dist[nx][ny],nx,ny))




# BFS
# from collections import deque
#
# cnt = 1
# while True:
#     N = int(input())
#     if N == 0:
#         break
#     graph = []
#     for i in range(N):
#         graph.append(list(map(int,input().split())))
#     visited = [[int(1e9) for _ in range(N)] for _ in range(N)]
#
#     dx = [1,0,-1,0]
#     dy = [0,1,0,-1]
#
#     q = deque()
#     q.append((graph[0][0],0,0)) #sum of cost, x, y
#     visited[0][0] = graph[0][0]
#     while q:
#         cost,x,y = q.popleft()
#         if x == N-1 and y == N-1:
#             continue
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny] <= cost+graph[nx][ny]:
#                 continue
#             visited[nx][ny] = graph[nx][ny] + cost
#             q.append((visited[nx][ny],nx,ny))
#
#     print("Problem {}: {}".format(cnt,visited[-1][-1]))
#     cnt+=1