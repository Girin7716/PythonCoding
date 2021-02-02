# 집합의 표현
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
        return parent[x]
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())

parent = [i for i in range(n+1)]
for i in range(m):
    o,a,b = map(int,input().split())
    if o == 0:
        union_parent(parent,a,b)
    else:   # o == 1
        if find_parent(parent,a) != find_parent(parent,b):
            print('NO')
        else:
            print('YES')