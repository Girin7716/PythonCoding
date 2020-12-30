# 카드 정렬하기 / p363 / 정렬
import heapq

N = int(input())
data = []
for i in range(N):
    heapq.heappush(data,int(input()))

min = []
result = 0
for i in range(N-1):
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    result += a+b
    heapq.heappush(data,a+b)

print(result)