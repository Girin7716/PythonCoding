# 세 용액
import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))

data.sort()

near_zero = int(1e9)
result = [0,1,2]
for i in range(N-2):
    if i > 0 and data[i] == data[i - 1]:
        continue

    left = i+1
    right = N-1
    while left < right:
        sum_value = data[i]+data[left]+data[right]
        if abs(near_zero) > abs(sum_value):
            near_zero = sum_value
            result[0] = i
            result[1] = left
            result[2] = right

        if sum_value > 0:
            right -= 1
        elif sum_value < 0:
            left += 1
        else:
            print(data[i],data[left],data[right])
            exit()


for i in result:
    print(data[i],end=' ')

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# data = list(map(int,input().split()))
#
# data.sort()
#
# left = 0
# right = N-1
# near_zero = int(1e9)
# result = [data[0],data[1],data[2]]
#
# while left < right-1:
#     mid = (left + right) // 2
#     mid2 = mid+1
#     sum_value = abs(data[left]+data[mid]+data[right])
#     sum_value2 = abs(data[left]+data[mid2]+data[right])
#
#     if abs(sum_value) > abs(sum_value2):
#         sum_value = sum_value2
#         mid = mid2
#
#     if abs(near_zero) > abs(sum_value):
#         near_zero = sum_value
#         result[0] = data[left]
#         result[1] = data[mid]
#         result[2] = data[right]
#     if sum_value > 0:
#         right -= 1
#     elif sum_value < 0:
#         left +=1
#     else:
#         break
# print(result[0],result[1],result[2])