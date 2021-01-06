# 팀 결성
# 난이도 2/3 , 풀이 시간 20분, 시간 제한 2초, 메모리 제한 128MB
# 책에서 푼 방법
def find_parent(parent, x):
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

n,m = map(int,input().split())
parent = [0] * (n+1)

for i in range(0,n+1):
    parent[i] = i

for i in range(m):
    oper,a,b=map(int,input().split())

    if oper==0:
        union_parent(parent,a,b)
    elif oper == 1:
        if find_parent(parent,a)==find_parent(parent,b):
            print('YES')
        else:
            print('NO')

# # 내가 푼 방법
# def find_parent(parent,x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent,parent[x])
#     return parent[x]
#
# # 두 원소가 속한 집합을 합치기
# def union_parent(parent,a,b):
#     a = find_parent(parent,a)
#     b = find_parent(parent,b)
#     if a<b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# N,M = map(int,input().split())
# parent = [0] * (N+1)
#
# # 부모 테이블상에서, 부모를 자기 자신으로 초기화
# for i in range(N+1):
#     parent[i] = i
#
# for i in range(M):
#     o,a,b=map(int,input().split())
#     if o == 0:
#         union_parent(parent, a, b)
#     else:
#         if find_parent(parent,a) == find_parent(parent,b):
#             print("YES")
#         else:
#             print("NO")

# case1
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1