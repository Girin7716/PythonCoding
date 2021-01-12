# 미세먼지 안녕!
from collections import deque
import sys
input = sys.stdin.readline

R,C,T = map(int,input().split())

machine_location = []
graph = []
for i in range(R):
    graph.append(list(map(int,input().split())))
    for j in range(C):
        if graph[i][j] == -1:
            machine_location.append((i,j))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def move_dirty():
    rem = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] != 0 and graph[i][j]!=-1:
                diffusion = graph[i][j] // 5
                check_dir = 0   # 몇개의 방향에 확산 되었는지에 대한 개수
                for p in range(4):
                    nx = i + dx[p]
                    ny = j + dy[p]
                    if nx < 0 or nx >= R or ny < 0 or ny >= C or (graph[nx][ny] == -1):
                        continue
                    check_dir += 1
                    rem[nx][ny] += diffusion
                rem[i][j] += graph[i][j] - (diffusion * check_dir)

    for i in range(R):
        for j in range(C):
            if rem[i][j] != 0 and graph[i][j] != -1:
                graph[i][j] = rem[i][j]


def air_cleaner(x1,y1,x2,y2):   # x1,y1은 위쪽 / x2,y2는 아래쪽
    rem = deque()
    rem.append(0)  # 기계에서 나온 공기
    # 위쪽 == 반시계 순환
    # 왼->오
    for i in range(y1+1,C):
        rem.append(graph[x1][i])
        graph[x1][i]=rem.popleft()
    # 아래->위
    for i in range(x1,0,-1):
        rem.append(graph[i-1][C-1])
        graph[i-1][C-1] = rem.popleft()
    # 오->왼
    for i in range(C-2,0,-1):
        rem.append(graph[0][i])
        graph[0][i] = rem.popleft()
    # 위->아래
    for i in range(x1):
        rem.append(graph[i][0])
        graph[i][0] = rem.popleft()
    rem.popleft()
    # 아래쪽 == 시계 순환
    # 왼->오
    rem.append(0)
    for i in range(y2+1,C):
        rem.append(graph[x2][i])
        graph[x2][i]=rem.popleft()
    # 위->아래
    for i in range(x2+1,R):
        rem.append(graph[i][C-1])
        graph[i][C-1] = rem.popleft()
    # 오->왼
    for i in range(C - 2, 0, -1):
        rem.append(graph[R-1][i])
        graph[R-1][i] = rem.popleft()
    # 아래->위
    for i in range(R-1,x2,-1):
        rem.append(graph[i][0])
        graph[i][0] = rem.popleft()


# T초까지 동작
for _ in range(T):
    move_dirty()
    air_cleaner(machine_location[0][0],machine_location[0][1],machine_location[1][0],machine_location[1][1])
    # for i in range(len(graph)):
    #     for j in range(len(graph[i])):
    #         print(graph[i][j],end=' ')
    #     print()
    # print('----------------------')
# T초 후 미세먼지 cnt
cnt = 0
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] != 0 and graph[i][j]!=-1:
            cnt += graph[i][j]
print(cnt)

# 7 8 1
# 0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0