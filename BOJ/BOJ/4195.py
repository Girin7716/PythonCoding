# 친구 네트워크
# disjoint set
import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a!=b:
        parent[b] = a
        number[a] += number[b]

for tc in range(int(input())):
    F = int(input())
    parent = {}
    number = {}
    for f in range(F):
        a,b = input().split()
        if parent.get(a) == None:
            parent[a] = a
            number[a] = 1
        if parent.get(b) == None:
            parent[b] = b
            number[b] = 1

        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
        answer = 0
        print(number[find_parent(parent,a)])






# BFS 시간초과
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# def BFS(visited,a,b):
#     q = deque()
#     answer = 0
#     q.append(a)
#     q.append(b)
#     visited[a] = True
#     visited[b] = True
#     answer += 2
#     while q:
#         now = q.popleft()
#         for i in graph[now]:
#             if visited[i] is True:
#                 continue
#             answer += 1
#             visited[i]= True
#             q.append(i)
#
#     return answer
#
# for tc in range(int(input())):
#     F = int(input())
#     graph = {}
#     visited = {}
#
#
#     for f in range(F):
#         a,b = (input().split())
#         graph[a] = graph.get(a,[]) + [b]
#         graph[b] = graph.get(b,[]) + [a]
#         visited[a] = visited.get(a, False)
#         visited[b] = visited.get(a, False)
#         print(BFS(visited,a,b))
#
#         for v in visited:
#             visited[v] = False