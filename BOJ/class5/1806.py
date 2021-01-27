# 부분합
import sys
input = sys.stdin.readline

N,S = map(int,input().split())
data = list(map(int,input().split()))

start = 0
end = 0
interval_sum = 0

min_index = int(1e9)
check = False
for start in range(N):
    while interval_sum < S and end < N:
        interval_sum += data[end]
        end += 1
    if interval_sum >= S and min_index > (end-start):
        min_index = end-start
        check = True

    interval_sum -= data[start]

if check == True:
    print(min_index)
else:
    print(0)
