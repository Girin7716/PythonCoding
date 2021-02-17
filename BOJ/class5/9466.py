# # 텀 프로젝트
import sys
from _collections import deque

tc = int(sys.stdin.readline())
for _ in range(tc):
    n = int(sys.stdin.readline())

    graph = [0] + list(map(int, sys.stdin.readline().rstrip().split()))


    indegree = [0] * (n + 1)
    for v in graph[1:]:
        indegree[v] += 1

    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    visit = [False] * (n+1)
    noCycleNode = set()
    while q:
        a = q.popleft()
        noCycleNode.add(a)

        indegree[graph[a]] -= 1
        if indegree[graph[a]] == 0:
            q.append(graph[a])

    print(len(noCycleNode))

# import sys
# sys.setrecursionlimit(10**8)
# input = sys.stdin.readline
#
# def dfs(node):
#     global cnt
#
#     visited[node] = True
#     next = graph[node]
#
#     if visited[next] == False:  # 방문 안했으면 next 방문하기
#         dfs(next)
#     elif fin[next] == False:    # next를 이미 방문했지만, 방문이 종료되지 않은 정점이라면 cycle
#         temp = next
#         while True:
#             cnt+=1
#             temp = graph[temp]
#             if temp == next:
#                 break
#
#     fin[node] = True
#
# for _ in range(int(input())):
#     n = int(input())
#     selected = [0] + list(map(int,input().split()))
#     cnt = 0
#     graph = {}
#     for i in range(1,n+1):
#         graph[i] = selected[i]
#
#     visited = [False for _ in range(n+1)]
#     fin = [False for _ in range(n+1)]
#
#     for i in range(1,n+1):
#         if visited[i] is False:
#             dfs(i)
#
#     print(n-cnt)