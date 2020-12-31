# 떡볶이 떡 만들기 / p201 / 이진 탐색
# 4 6
# 19 15 10 17
N,M = list(map(int,input().split()))
array = list(map(int,input().split()))

start = 0
end = max(array)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in array:
        if x > mid:
            total += x - mid

    if total > M:
        start = mid + 1
    else:
        result = mid
        end = mid-1

print(result)

# n,m = list(map(int,input().split(' ')))
# array = list(map(int,input().split()))
#
# start = 0
# end = max(array)
#
# result = 0
# while start <= end:
#     total = 0
#     mid = (start + end) // 2
#     for x in array:
#         if x > mid:
#             total += x - mid
#     if total < m:
#         end = mid - 1
#     else:
#         result = mid
#         start = mid + 1
# print(result)

# 4 6
# 19 15 10 17