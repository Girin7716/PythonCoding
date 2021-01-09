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

    left = heapq.heappop(max_h)
    mid = -left
    if i != 0:
        print(mid)
        continue
    right = heapq.heappop(min_h)
    mid = min(-left, right)
    heapq.heappush(max_h, right)
    heapq.heappush(min_h, left)

    print(mid)

# 6
# 5
# 4
# 4
# 4
# 3
# 3
