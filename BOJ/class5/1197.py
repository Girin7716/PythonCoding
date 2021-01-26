# 최소 스패닝 트리
# 크루스칼
import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x]!=x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int,input().split())
edges = []
for _ in range(E):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

edges.sort()

parent = [i for i in range(V+1)]

result = 0
for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost

print(result)