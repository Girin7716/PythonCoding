# Q1
# https://www.acmicpc.net/problem/1931와 유사하다고 함.
import heapq
import sys
input = sys.stdin.readline

N = int(input())
pq = []
answer = 0
for i in range(N):
    start,end = map(int,input().split())
    heapq.heappush(pq,(end,start))

start,end = 0,0

while pq:
    nowEnd,nowStart = heapq.heappop(pq)
    if nowStart >= end:
        answer+=1
        start,end = nowStart, nowEnd

print(answer)