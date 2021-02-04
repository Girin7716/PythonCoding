# 스타트링크
from collections import deque
import sys
input = sys.stdin.readline

F,S,G,U,D = map(int,input().split())

q = deque()
visited = [-1] * (F+1)
q.append((S, 0))
visited[S] = 0

while q:
    loc,cnt = q.popleft()

    if loc == G:
        break

    if loc+U <= F and visited[loc+U] == -1:
        visited[loc+U] = cnt+1
        q.append((loc+U,cnt+1))
    if loc-D >= 1 and visited[loc-D] == -1:
        visited[loc-D] = cnt+1
        q.append((loc-D,cnt+1))


if visited[G] == -1:
    print('use the stairs')
else:
    print(visited[G])