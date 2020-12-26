# 인구 이동 / p353 / DFS, BFS
from collections import deque

n,l,r = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

result = 0

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신

def process(x,y,index):
    united = []
    united.append((x,y))

    q = deque()
    q.append((x,y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y]
    summary = graph[x][y]
    count = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if 0<=nx<n and 0<=ny<n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx,ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx,ny))
    # 연합 국가끼리 인구 분배
    for i,j in united:
        graph[i][j] = summary // count
    return count

total_count = 0
# 더 이상 인구 이동을 할 수 없을때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:   # 해당 나라가 아직 처리되지 않았다면
                process(i,j,index)
                index+=1
    # 모든 인구 이동이 끝난 경우
    # for i in range(len(graph)):
    #     for j in range(len(graph[i])):
    #         print(graph[i][j],end=' ')
    #     print()
    # print()
    if index == n*n:
        break
    total_count += 1
print(total_count)

# 실패
# from collections import deque
#
# N,L,R = map(int,input().split())
#
# A = []
# for i in range(N):
#     A.append(list(map(int,input().split())))
#
# def do_bfs(A,visited,i,j):
#     queue = deque()
#     queue.append([i,j])
#     rem = deque()
#     rem.append([i,j])
#     dx = [1,0,-1,0]
#     dy = [0,1,0,-1]
#     go = [[0 for _ in range(N)] for _ in range(N)]
#     avg = A[i][j]
#     while queue:
#         x,y = queue.pop()
#         go[x][y] = 1
#         visited[x][y] = 1
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<N and 0<=ny<N:
#                 distance = abs(A[nx][ny] - A[x][y])
#             else:
#                 continue
#             if L<=distance<=R and visited[nx][ny] == 0:
#                 avg+=A[nx][ny]
#                 rem.append([nx,ny])
#                 queue.append([nx,ny])
#
#
#
#     cnt = len(rem)
#     avg = int(avg/cnt)
#     while rem:
#         x,y = rem.pop()
#         A[x][y] = avg
#     if cnt == 1:
#         return False
#     else:
#
#         # for i in range(len(A)):
#         #     for j in range(len(A[i])):
#         #         print(A[i][j], end=' ')
#         #     print()
#         # print()
#         return True
#
# answer = 0
# while True:
#     check = 0
#     visited = [[0 for _ in range(N)] for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if visited[i][j] == 0:
#                 if do_bfs(A,visited,i,j) == True:    # visited and number change
#                     check = 1
#     if check == 0:
#         break
#     answer+=1
#
#     for i in range(len(A)):
#         for j in range(len(A[i])):
#             print(A[i][j],end = ' ')
#         print()
#     print()
#
# print(answer)

# 2 20 50
# 50 30
# 20 40

# 2 40 50
# 50 30
# 20 40

# 2 20 50
# 50 30
# 30 40

# 3 5 10
# 10 15 20
# 20 30 25
# 40 22 10

# 4 10 50
# 10 100 20 90
# 80 100 60 70
# 70 20 30 40
# 50 20 100 10