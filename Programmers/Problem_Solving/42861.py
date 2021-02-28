# # 섬 연결하기
import heapq

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

def solution(n, costs):
    answer = 0
    pq = []
    graph = [[] for _ in range(n)]
    parent = [i for i in range(n)]

    for a,b,c in costs:
        graph[a].append([b,c])
        graph[b].append([a,c])
        heapq.heappush(pq,[c,a,b])

    edges_cnt = 0
    while edges_cnt != n-1:
        c,a,b = heapq.heappop(pq)

        a = find_parent(parent,a)
        b = find_parent(parent,b)

        if a != b:
            union_parent(parent,a,b)
            answer += c
            edges_cnt+=1

    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))


# def find_parent(parent,x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent,parent[x])
#     return parent[x]
#
# def union_parent(parent,a,b):
#     a = find_parent(parent,a)
#     b = find_parent(parent,b)
#
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# def solution(n, costs):
#     answer = 0
#     graph = [[] for _ in range(n)]
#     parent = [i for i in range(n)]
#     costs.sort(key = lambda x:x[2])
#
#     for a,b,c in costs:
#         graph[a].append([b,c])
#         graph[b].append([a,c])
#
#     edges_cnt = 0
#     for a,b,c in costs:
#         if edges_cnt == n-1:
#             break
#         a = find_parent(parent,a)
#         b = find_parent(parent,b)
#
#         if a != b:
#             union_parent(parent,a,b)
#             answer += c
#             edges_cnt += 1
#
#     return answer
#
# print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))