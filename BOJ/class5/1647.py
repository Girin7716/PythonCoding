# 도시 분할 계획
import heapq
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

graph = [[] for _ in range(N+1)]
parent = [i for i in range(N+1)]
q = []
for i in range(M):
    a,b,cost = map(int,input().split())
    heapq.heappush(q,(cost,a,b))

result = 0
road = 0
max_road = -1
while road != N-1:
    cost,a,b = heapq.heappop(q)

    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        max_road = max(max_road,cost)
        road+=1

print(result - max_road)