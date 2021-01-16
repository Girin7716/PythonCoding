# 특정한 최단 경로
import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)
N, E = map(int,input().split())
graph = [[] for _ in range(N+1)]
for i in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2 = map(int,input().split())

def dijkstra(start):
    distance = [INF] * (N+1)
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start)) # cost, node

    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

    return distance

one = dijkstra(1)
rem_v1 = dijkstra(v1)
rem_v2 = dijkstra(v2)

result = min(one[v1]+rem_v1[v2]+rem_v2[N],one[v2]+rem_v2[v1]+rem_v1[N])
print(result if result < INF else -1)

# 4 6
# 1 2 3
# 2 3 3
# 3 4 1
# 1 3 5
# 2 4 5
# 1 4 4
# 1 3