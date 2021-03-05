# 합승 택시 요금

# 다익스트라
import heapq

def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF
    graph = [[] for _ in range(n+1)]

    for fare in fares:
        x,y,z = fare
        graph[x].append([y,z])
        graph[y].append([x,z])

    def dijkstra(start,end,n):
        q = []
        distance = [INF] * (n + 1)
        heapq.heappush(q,(0,start))
        distance[start] = 0
        while q:  # 큐가 비어있지 않다면
            # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(q)
            # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            if distance[now] < dist:
                continue
            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            for i in graph[now]:
                cost = dist + i[1]
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
        return distance[end]

    for i in range(1,n+1):
        rem = 0
        rem += dijkstra(s,i,n)+dijkstra(i,a,n)+dijkstra(i,b,n)
        answer = min(answer,rem)

    return answer


'''
정확성: 50.0
효율성: 48.3
합계: 98.3 / 100.0
'''
# 플로이드 워셜
# def solution(n, s, a, b, fares):
#     INF = int(1e9)
#     answer = INF
#
#     graph = [[INF] * (n+1) for _ in range(n+1)]
#     # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
#     for x in range(1, n + 1):
#         for y in range(1, n + 1):
#             if x == y:
#                 graph[x][y] = 0
#     # 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
#     for fare in fares:
#         # A에서 B로 가는 비용은 C라고 설정
#         x, y, z = fare
#         graph[x][y] = z
#         graph[y][x] = z
#     # 점화식에 따라 플로이드 워셜 알고리즘을 수행
#     for k in range(1, n + 1):
#         for x in range(1, n + 1):
#             for y in range(1, n + 1):
#                 graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])
#
#     for i in range(1,n+1):
#         rem = 0
#         if graph[s][i] == INF or graph[i][a] == INF or graph[i][b] == INF:
#             continue
#         else:
#             rem += graph[s][i]
#             rem += graph[i][a]
#             rem += graph[i][b]
#
#         answer = min(answer,rem)
#
#     return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))