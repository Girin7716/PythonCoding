# 최소비용 구하기
import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = int(1e9)

graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))

start, end = map(int,input().split())
def dijkstra(start,end):
    q = []
    distance = [INF ]* (N+1)
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] <dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    print(distance[end])

dijkstra(start,end)