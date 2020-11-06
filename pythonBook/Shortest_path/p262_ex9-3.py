# 전보
# 책에서 푼 방법
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m,start = map(int,input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra(strat):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance,d)
print(count-1,max_distance)

# # 내가 푼 방법
# import heapq
# import sys
#
# N,M,C = map(int,input().split())
# INF = int(1e9)
#
# graph = [[] for i in range(N+1)]
# distance = [INF] *(N+1)
#
# for _ in range(M):
#     a,b,c = map(int, input().split())
#     # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
#     graph[a].append((b,c))
#
# def dijkstra(start):
#     q = []
#     # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
#     heapq.heappush(q,(0,start))
#     distance[start] = 0
#     while q: #큐가 비어있지 않다면
#         # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
#         dist, now = heapq.heappop(q)
#         # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
#         if distance[now] < dist:
#             continue
#         # 현재 노드와 연결된 다른 인접한 노드들을 확인
#         for i in graph[now]:
#             cost = dist + i[1]
#             # 현재 노드를 거쳣, 다른 노드로 이동하는 거리가 더 짧은 경우
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q,(cost,i[0]))
#
# # 다익스트라 알고리즘 수행
# dijkstra(C)
#
# result_a = 0
# result_b = 0
# # 모든 노드로 가기 위한 최단 거리 출력
# for i in range(1,N+1):
#     if distance[i] != INF and distance[i] != 0:
#         result_a += 1
#         result_b = max(result_b,distance[i])
#
# print(result_a, result_b)


# 3 2 1
# 1 2 4
# 1 3 2