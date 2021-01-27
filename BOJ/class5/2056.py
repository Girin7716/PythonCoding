# 작업
#896
from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
data = []
for i in range(N):
    data.append(list(map(int,input().split())))

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for i in range(1,N+1):
    for j in range(data[i-1][1]):
        graph[data[i-1][j+2]].append(i)
        indegree[i] += 1

q = deque()
dp = [0] * (N+1)
for i in range(1,N+1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = data[i-1][0]
while q:
    now = q.popleft()
    for i in graph[now]:
        dp[i] = max(dp[i],dp[now]+data[i-1][0])
        indegree[i]-=1
        if indegree[i] == 0:
            q.append(i)
print(max(dp))


# 1308ms
# from collections import deque
# import sys
#
# def find_parent(parent,x):
#     if parent[x] != x:
#         return find_parent(parent,parent[x])
#     return parent[x]
#
# def union_parent(parent,a,b):
#     a = find_parent(parent,a)
#     b = find_parent(parent,b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# input = sys.stdin.readline
# N = int(input())
# data = []
# for i in range(N):
#     data.append(list(map(int,input().split())))
#
# graph = [[] for _ in range(N+1)]
# indegree = [0] * (N+1)
# parent = [i for i in range(N+1)]
#
# for i in range(1,N+1):
#     for j in range(data[i-1][1]):
#         graph[data[i-1][j+2]].append(i)
#         indegree[i] += 1
#
# q = deque()
# dp = [0] * (N+1)
# for i in range(1,N+1):
#     if indegree[i] == 0:
#         q.append(i)
#         dp[i] = data[i-1][0]
# max_value = -1
# while q:
#     now = q.popleft()
#     for i in graph[now]:
#         union_parent(parent,now,i)
#         dp[i] = max(dp[i],dp[now]+data[i-1][0])
#         if max_value < dp[i]:
#             max_value = dp[i]
#         indegree[i]-=1
#         if indegree[i] == 0:
#             q.append(i)
#
# result = [0] * (N+1)
# for i in range(1,N+1):
#     x = find_parent(parent,i)
#     if result[parent[x]] < dp[i]:
#         result[parent[x]] = dp[i]
#
# print(max(result))


# 연결이 안되어 있는 그래프의 경우
# 7
# 5 0
# 1 0
# 3 0
# 6 0
# 1 0
# 8 0
# 4 0

# 7
# 5 0
# 1 1 1
# 3 0
# 6 1 1
# 1 2 2 4
# 8 2 2 4
# 4 3 3 5 6