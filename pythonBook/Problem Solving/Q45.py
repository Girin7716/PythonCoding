# 최종 순위 / p399 / 그래프 이론 문제
from collections import deque

for tc in range(int(input())):
    n = int(input())
    graph =[[0 for _ in range(n+1)] for _ in range(n+1)]
    indegree = [0 for _ in range(n + 1)]
    t = list(map(int,input().split()))
    for i in range(n):
        for j in range(i+1,n):
            graph[t[i]][t[j]] = 1
            indegree[t[j]] += 1

    m = int(input())
    for i in range(m):
        a,b = map(int,input().split())
        if graph[a][b] == 1:
            graph[a][b] = 0
            graph[b][a] = 1
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[a][b] = 1
            graph[b][a] = 0
            indegree[b] += 1
            indegree[a] -= 1

    q = deque()
    result = []
    cycle = False
    certain = True
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
            result.append(i)

    for i in range(n):
        if len(q)==0:
            cycle = True
            break
        if len(q)>=2:
            certain = False
            break
        now = q.popleft()
        for i in range(1,n+1):
            if graph[now][i] == 1:
                graph[now][i] = 0
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
                    result.append(i)
    if cycle is True:
        print("IMPOSSIBLE")
    elif certain is False:
        print("?")
    else:
        for i in result:
            print(i,end=' ')
        print()

# from collections import deque
#
# for tc in range(int(input())):
#     n = int(input())
#     INF = int(1e9)
#     graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
#     indegree = [0 for _ in range(n+1)]
#     t = list(map(int,input().split()))
#     for i in range(n):
#         for j in range(i+1,n):
#             graph[t[i]][t[j]] = 1
#             indegree[t[j]] += 1
#     m = int(input())
#     for i in range(m):
#         a,b=map(int,input().split())
#         if graph[a][b]:
#             graph[a][b] = 0
#             graph[b][a] = 1
#             indegree[a] += 1
#             indegree[b] -= 1
#         else:
#             graph[a][b] = 1
#             graph[b][a] = 0
#             indegree[a] -= 1
#             indegree[b] += 1
#
#     q = deque()
#     result = []
#     for i in range(1,n+1):
#         if indegree[i] == 0:
#             q.append(i)
#     cycle = False
#     certain = True
#
#     for i in range(n):
#         if len(q) == 0:
#             cycle = True
#             break
#         if len(q)>=2:
#             certain = False
#             break
#         now = q.popleft()
#         result.append(now)
#         for i in range(1,n+1):
#             if graph[now][i]:
#                 indegree[i] -= 1
#                 if indegree[i] == 0:
#                     q.append(i)
#     if cycle is True:
#         print("IMPOSSIBLE")
#     elif certain is False:
#         print("?")
#     else:
#         for i in result:
#             print(i,end= ' ')
#         print()

# 3
# 5
# 5 4 3 2 1
# 2
# 2 4
# 3 4
# 3
# 2 3 1
# 0
# 4
# 1 2 3 4
# 3
# 1 2
# 3 4
# 2 3