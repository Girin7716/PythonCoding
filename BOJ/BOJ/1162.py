# 도로포장
import sys
import heapq
input = sys.stdin.readline

N,M,K = map(int,input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e13)
# distance = [INF] * (N+1)
distance = [[INF for _ in range(N+1)] for _ in range(K+1)]
for i in range(M):
    a,b,cost = map(int,input().split())
    graph[a].append((cost,b))
    graph[b].append((cost,a))

# distance[k][n] => k개 포장했을때 n번 노드의 최소 거리
# print(distance)

pq = []
heapq.heappush(pq,(0,1,0))  # dist,node,포장갯수
while pq:
    dist,now,cnt = heapq.heappop(pq)
    if cnt > K or distance[cnt][now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[0]
        if cost < distance[cnt][i[1]]:  # 포장 안함
            distance[cnt][i[1]] = cost
            heapq.heappush(pq,(cost,i[1],cnt))
        cost = dist
        if cnt<=K-1 and cost < distance[cnt+1][i[1]]:    #포장함
            distance[cnt+1][i[1]] = cost
            heapq.heappush(pq,(cost,i[1],cnt+1))

# for i in range(len(distance)):
#     for j in range(len(distance[i])):
#         print(distance[i][j],end=' ')
#     print()

min_value = INF
for i in range(K+1):
    min_value = min(min_value,distance[i][N])
print(min_value)

# 4 4 2
# 1 2 10
# 2 4 10
# 1 3 1
# 3 4 100

# 6 6 2
# 1 2 10
# 2 4 10
# 1 3 1
# 3 4 100
# 4 5 10
# 5 6 100

# 4 4 19
# 1 2 10
# 2 4 10
# 1 3 1
# 3 4 100

# 2 2 1
# 1 2 10
# 2 1 51

# 3 2 1
# 1 2 1000
# 2 3 1