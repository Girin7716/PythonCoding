# 파티
import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int,input().split())
graph = [[] for _ in range(N+1)]
r_graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))
    r_graph[b].append((a,w))
INF = int(1e9)

distance = [INF] * (N+1)
r_distance = [INF] * (N+1)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) # weight,node
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    heapq.heappush(q, (0, start))  # weight,node
    r_distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        for i in r_graph[now]:
            cost = dist + i[1]
            if r_distance[i[0]] > cost:
                r_distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    for i in range(1,N+1):
        distance[i] += r_distance[i]
    print(max(distance[1:]))

dijkstra(X)


# 4 8 2
# 1 2 4
# 1 3 2
# 1 4 7
# 2 1 1
# 2 3 5
# 3 1 2
# 3 4 4
# 4 2 3