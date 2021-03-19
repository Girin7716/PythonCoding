# 트리의 독립집합
N = int(input())
weights = list(map(int,input().split()))
tree = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

