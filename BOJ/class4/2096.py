# 내려가기
N = int(input())
# graph = []
# for i in range(N):
#     graph.append(list(map(int,input().split())))
graph = [list(map(int, input().split())) for _ in range(N)]

max_value = graph[0]
min_value = graph[0]

for i in range(1,N):
    max_value = [max(max_value[0],max_value[1])+graph[i][0],
                 max(max_value[0],max_value[1],max_value[2])+graph[i][1],
                 max(max_value[1],max_value[2])+graph[i][2]]
    min_value = [min(min_value[0],min_value[1])+graph[i][0],
                 min(min_value[0],min_value[1],min_value[2])+graph[i][1],
                 min(min_value[1],min_value[2])+graph[i][2]]
print(max(max_value),min(min_value))






# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# N = int(input())
# graph = []
# for i in range(N):
#     graph.append(list(map(int,input().split())))
#
# q = deque()
# for i in range(N):
#     q.append((0,i,graph[0][i]))   # location, cost
#
# max_value = -1
# min_value = 99999999
# while q:
#     x,y,cost = q.popleft()
#     if x == N-1:
#         if max_value < cost:
#             max_value = cost
#         elif min_value > cost:
#             min_value = cost
#         continue
#     # left_down
#     if x+1<N and y-1>=0:
#         q.append((x+1,y-1,cost+graph[x+1][y-1]))
#     # down
#     if x+1<N:
#         q.append((x+1,y-1,cost+graph[x+1][y]))
#     # right_down
#     if x+1<N and y+1<N:
#         q.append((x+1,y+1,cost+graph[x+1][y+1]))
#
# print(max_value,min_value)