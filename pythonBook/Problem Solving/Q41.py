# 여행 계획 / p393 / 그래프 이론 문제
# 내가 푼 방법
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

N,M = map(int,input().split())
graph=[]
for i in range(N):
    graph.append(list(map(int,input().split())))
travel_plan = list(map(int,input().split()))
INF = int(1e9)
parent = [i for i in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            union_parent(parent,i,j)

now = travel_plan[0]
for x in travel_plan[1:]:
    if find_parent(parent,now)!=find_parent(parent,x):
        print("NO")
        exit()
print("YES")

# # 책에서 푼 방법
# def find_parent(parent,x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent,parent[x])
#     return parent[x]
#
# def union_parent(parent,a,b):
#     a = find_parent(parent,a)
#     b = find_parent(parent,b)
#
#     if a<b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# n,m = map(int,input().split())
# parent = [0] * (n+1)
#
# for i in range(1,n+1):
#     parent[i] = i
#
# for i in range(n):
#     data = list(list(map(int,input().split())))
#     for j in range(n):
#         if data[j] == 1:
#             union_parent(parent,i+1,j+1)
#
# plan = list(map(int,input().split()))
#
# result = True
# for i in range(m-1):
#     if find_parent(parent,plan[i]) != find_parent(parent,plan[i+1]):
#         result = False
#
# if result:
#     print("YES")
# else:
#     print("NO")

# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3