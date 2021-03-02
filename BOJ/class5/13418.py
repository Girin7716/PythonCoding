# 학교 탐방하기
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

def minist():
    global N
    parent = [i for i in range(N + 1)]

    edges.sort()

    minst = 0
    cnt = 0
    for edge in edges:
        if cnt == N - 1:
            break

        cost, a, b = edge

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            minst += cost
            cnt += 1

    return minst

def maxist():
    global N
    parent = [i for i in range(N + 1)]

    edges.sort(reverse=True)

    maxst = 0
    cnt = 0
    for edge in edges:
        if cnt == N-1:
            break
        cost,a,b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            maxst += cost
            cnt += 1

    return maxst

N,M = map(int,input().split())
edges = []
rem = 0
for i in range(M+1):
    # 건물1, 건물2, 오르막(1) or 내리막(0)
    a,b,c = map(int,input().split())
    if c == 0:  c = 1
    else: c = 0

    if a == 0 or b == 0:
        rem = c
        continue

    edges.append((c,a,b))

minst = minist()
min_fatigue = (minst+rem)**2
maxst = maxist()
max_fatigue = (maxst+rem)**2
print(max_fatigue - min_fatigue)