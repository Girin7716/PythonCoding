# 어두운 길 / p397 / 그래프 이론 문제
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

N,M = map(int,input().split())
edges = []
total=0
for i in range(M):
    edges.append(list(map(int,input().split())))
    total+=edges[i][2]

edges.sort(key = lambda x:x[2])

parent = [i for i in range(N)]

result = 0
cnt = 0
for a,b,cost in edges:
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        cnt+=1
    if cnt==N:
        break
print(total-result)


# 7 11
# 0 1 7
# 0 3 5
# 1 2 8
# 1 3 9
# 1 4 7
# 2 4 5
# 3 4 15
# 3 5 6
# 4 5 8
# 4 6 9
# 5 6 11