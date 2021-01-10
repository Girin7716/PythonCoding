# 가운데를 말해요
import heapq
import sys
input = sys.stdin.readline

N = int(input())

max_h = []
min_h = []

for i in range(N):
    data = int(input())

    if len(max_h) == len(min_h):
        heapq.heappush(max_h,-data)
    else:
        heapq.heappush(min_h,data)

    if min_h and (-max_h[0])>min_h[0]:
        left = heapq.heappop(max_h)
        right = heapq.heappop(min_h)
        heapq.heappush(max_h,-right)
        heapq.heappush(min_h,-left)

    print(-max_h[0])

# 6
# 5
# 4
# 4
# 4
# 3
# 3
