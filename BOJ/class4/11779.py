# 최소비용 구하기2
import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))
start, end = map(int,input().split())
distance = [INF] * (n+1)
distance[start] = 0
path = [-1 for i in range(n+1)]

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))   #weight, node
    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                path[i[0]] = now
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

print(distance[end])

rem = []
rem.append(end)

while True:
    if end == start:
        break
    rem.append(path[end])
    end = path[end]

rem.sort()
print(len(rem))
for i in rem:
    print(i,end= ' ')

# 5
# 10
# 1 2 2
# 1 3 3
# 1 3 4
# 1 4 1
# 4 5 2
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5