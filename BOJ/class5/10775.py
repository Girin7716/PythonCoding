# 공항
import sys
input = sys.stdin.readline

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

G = int(input())
P = int(input())
gate = []
parent = [i for i in range(G+1)]
for _ in range(P):
    x = int(input())
    gate.append(x)

def solution():
    answer = 0
    for g in gate:
        prem = find_parent(parent, g)
        answer += 1
        if g == prem:
            union_parent(parent, g, g - 1)
        elif prem == 0:
            answer -= 1
            break
        else:
            union_parent(parent, prem, prem - 1)
    return answer

print(solution())
