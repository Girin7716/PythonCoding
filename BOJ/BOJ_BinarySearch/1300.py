# K번째 수
N = int(input())
k = int(input())

start = 0
end = k
result = 1
while(start<=end):
    mid = (start+end)//2

    count = 0
    for i in range(1,N+1):
        c = mid // i
        if c > N:
            c = N
        count += c
    if count < k:
        start = mid+1
    else:
        result = mid
        end = mid - 1
print(result)

# N = int(input())
# k = int(input())
#
# start = 0
# end = k
# result = 1
# while(start<=end):
#     mid = (start+end)//2
#     count = 0
#     for i in range(1,N+1):
#         count += min(mid//i,N)
#
#     if count < k:
#         start = mid + 1
#     else:
#         result = mid
#         end = mid - 1
#
# print(result)