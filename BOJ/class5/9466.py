# 텀 프로젝트

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,x)
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(int(input())):
    n = int(input())
    student = [0] + [i for i in range(1,n+1)]
    selected = [0] + list(map(int,input().split()))

    print(n,student,selected)


