# 숨바꼭질 / p390 / 최단 경로 문제
import heapq

N, M = map(int,input().split())
INF = int(1e9)
graph = [[]for _ in range(N)]
distance = [INF] *(N)

for i in range(M):
    a,b= map(int,input().split())
    graph[a-1].append((b-1,1))  # end,cost
    graph[b-1].append((a-1,1))  # end,cost

q = []
heapq.heappush(q,(0,0)) # 1번 node == 0
while q:
    x, dist = heapq.heappop(q)
    for i in graph[x]:
        if distance[i[0]] < dist:
            continue
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(i[0],cost))

#print(max(distance))
max_value = max(distance[1:])
print(distance[1:].index(max_value)+2,end= ' ')
print(max_value,end=' ')
print(distance[1:].count(max_value))

# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2