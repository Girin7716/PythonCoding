# # 보석 도둑
import heapq
from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
jew = []
bag = []

for i in range(N):
    m,v = map(int,input().split())
    jew.append((m,-v))

for i in range(K):
    weight = int(input())
    bag.append(weight)

jew = deque(list(sorted(jew)))
bag.sort()

pq = []

result = 0

for bag_weight in bag:
    while jew and bag_weight >= jew[0][0]:
        heapq.heappush(pq,jew[0][1])
        jew.popleft()
    if pq:
        result += -heapq.heappop(pq)

print(result)

# naive
# N,K = map(int,input().split())
# M = []
# V = []
# for i in range(N):
#     m,v = map(int,input().split())
#     M.append((v,m))
# for i in range(K):
#     weight = int(input())
#     V.append([weight,False])    # 무게, 보석이 있나?
#
# M.sort(reverse=True)
# V.sort()
#
# result = 0
# for value,m in M:
#     for v in V:
#         if v[1] is True:
#             continue
#         if v[0] > m:
#             result += value
#             v[1] = True
#             break
#
# print(result)