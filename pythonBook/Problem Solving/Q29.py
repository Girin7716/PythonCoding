# 공유기 설치 / p369 / 이진 탐색 문제

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

