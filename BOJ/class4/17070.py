# 파이프 옮기기1
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))

q = deque()
q.append((0,0,0,1)) # 시작 좌표
result = 0

def check_galo(x2,y2):
    # case1
    if y2+1<N and graph[x2][y2+1] != 1:
        q.append((x2,y2,x2,y2+1))
    # case2
    if x2+1<N and y2+1<N and graph[x2][y2+1] != 1 and graph[x2+1][y2] != 1 and graph[x2+1][y2+1] != 1:
        q.append((x2,y2,x2+1,y2+1))

def check_selo(x2,y2):
    # case1
    if x2+1<N and graph[x2+1][y2] != 1:
        q.append((x2,y2,x2+1,y2))
    # case2
    if x2+1<N and y2+1<N and graph[x2+1][y2] != 1 and graph[x2][y2+1] !=1 and graph[x2+1][y2+1] != 1:
        q.append((x2,y2,x2+1,y2+1))

def check_daegak(x2,y2):
    # case1
    if y2+1 < N and graph[x2][y2+1] != 1:
        q.append((x2,y2,x2,y2+1))
    # case2
    if x2+1 < N and graph[x2+1][y2] != 1:
        q.append((x2,y2,x2+1,y2))
    # case3
    if x2+1 < N and y2+1 < N and graph[x2+1][y2] != 1 and graph[x2][y2+1] != 1 and graph[x2+1][y2+1] != 1:
        q.append((x2,y2,x2+1,y2+1))
    return

def check(x1,y1,x2,y2):
    # 가로
    if (x2-x1 == 0) and (y2-y1 == 1):
        check_galo(x2, y2)
    # 세로
    elif (x2-x1 == 1) and (y2-y1 == 0):
        check_selo(x2, y2)
    # 대각선
    else:
        check_daegak(x2, y2)

while q:
    x1,y1,x2,y2 = q.popleft()
    if (x2 == N-1) and (y2 == N-1):
        result += 1
        continue
    if x1<0 or x1>=N or y1<0 or y1>=N or x2<0 or x2>=N or y2<0 or y2>=N:
        continue
    check(x1,y1,x2,y2)

print(result)




# 3
# 0 0 0
# 0 0 0
# 0 0 0
