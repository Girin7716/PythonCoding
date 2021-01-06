# 에너지 드링크
import collections
import heapq

N = int(input())
a = list(map(int,input().split()))
energy = collections.deque(a)
min = []
max = []
for i in a:
    heapq.heappush(min, i)
    heapq.heappush(max, -i)

for i in range(N-1):
    a = heapq.heappop(min)
    b = heapq.heappop(max)
    new = -b+(a/2)
    heapq.heappush(min,new)
    heapq.heappush(max,-new)
b = heapq.heappop(max)
print(-b)
