# 특정 거리의 도시 찾기 / p339 / DFS,BFS 문제
from collections import deque

N,M,K,X = map(int,input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
distance = [-1 for _ in range(N+1)]
distance[X] = 0

queue = deque()
queue.append(X)
while queue:
    start = queue.popleft()
    for next in graph[start]:
        if distance[next] == -1:
            distance[next]=distance[start]+1
            queue.append(next)

answer = []
for i in range(len(distance)):
    if distance[i] == K:
        answer.append(i)
if answer == []:
    print(-1)
else:
    for i in range(len(answer)):
        print(answer[i])

# 밑의 방법 => 메모리 초과
# from collections import deque
#
# N,M,K,X = map(int,input().split())
#
# # graph 연결
# graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
# for i in range(M):
#     a,b = map(int,input().split())
#     graph[a][b] = 1
# distance = [0 for _ in range(N+1)]
#
# queue = deque()
# queue.append(X)
# while queue:
#     start = queue.popleft()
#     for x in range(len(graph[start])):
#         if graph[start][x] == 1:
#             if distance[x] == 0:
#                 distance[x]+=distance[start] + 1
#                 queue.append(x)
# answer = []
# for i in range(len(distance)):
#     if distance[i] == K:
#         answer.append(i)
#
# if answer == []:
#     print(-1)
# else:
#     for i in range(len(answer)):
#         print(answer[i])




# input
# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

# 4 3 2 1
# 1 2
# 1 3
# 1 4

# 4 4 1 1
# 1 2
# 1 3
# 2 3
# 2 4