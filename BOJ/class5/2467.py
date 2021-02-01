# 용액
import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))

left = 0
right = N-1

near_zero = int(1e9)
result = [data[0],data[1]]
while left < right:
    sum_value = data[left] + data[right]
    if abs(near_zero) > abs(sum_value):
        near_zero = sum_value
        result[0] = data[left]
        result[1] = data[right]
    if sum_value > 0:
        right -= 1
    elif sum_value < 0:
        left += 1
    else:   # sum_value == 0
        break
print(result[0],result[1])

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# data = list(map(int,input().split()))
#
# start = 1
# end = N-1
# result = [data[0],data[1]]
#
# near_zero = int(1e9)
# for i in range(N):
#     start = i
#     end = N-1
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if data[i] + data[mid] == 0:
#             result[0] = data[i]
#             result[1] = data[mid]
#             near_zero = data[i] + data[mid]
#             break
#         elif data[i] + data[mid] < 0:
#             start = mid + 1
#         else:  # data[i]+data[mid] > 0
#             end = mid - 1
#         if i == mid:
#             continue
#         if abs(near_zero) > abs(data    [i] + data[mid]):
#             near_zero = data[i] + data[mid]
#             result[0] = data[i]
#             result[1] = data[mid]
#
#
# print(result[0],result[1])