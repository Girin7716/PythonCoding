# 공유기 설치 / p369 / 이진 탐색 문제
import sys
input = sys.stdin.readline

N,C = map(int,input().split())
data = []
for i in range(N):
    data.append(int(input()))
data.sort()

#start = data[1] - data[0]   # min
start = 1e9
for i in range(N-1):
    if start > data[i+1] - data[i]:
        start = data[i+1] - data[i]

end = data[-1] - data[0]    # max
result = 0
while start <= end:
    gap = (start + end) // 2
    value = data[0]
    count = 1

    for i in range(1,N):
        if data[i] >= value + gap:
            value = data[i]
            count += 1
    if count >= C:
        start = gap + 1
        result = gap
    else:
        end = gap - 1

print(result)



# 실패
# from bisect import bisect_left, bisect_right
#
# N, C = map(int,input().split())
# data = []
# for i in range(N):
#     data.append(int(input()))
# data.sort()
#
# interval = N/(C-1)
# sum = 0
# min = 9999999999
# for i in range(C-1):
#     a = data[round(sum)]
#     sum+=interval
#     if sum == N:
#         sum -=1
#     b = data[round(sum)]
#     if min > b-a:
#         min = b-a
#
# print(min)

