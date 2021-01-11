# 최단경로
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
V,E = map(int,input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for i in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

distance = [INF] * (V + 1)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(distance[start],start))

    while q:
        dist,now = heapq.heappop(q)
        for next in graph[now]:
            cost = dist + next[1]
            if distance[next[0]] > cost:
                distance[next[0]] = cost
                heapq.heappush(q,(cost,next[0]))


dijkstra(K)

for i in range(1,V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])

# 5 6
# 1
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6