# # Q6 무지의 먹방 라이브 / p316
import heapq

def solution(food_times, k):
    answer = 0
    if k >= sum(food_times):
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))

    previous = 0
    cnt = len(q)
    data, index = heapq.heappop(q)
    while k >= (data-previous)*cnt:
        k -= (data-previous)*cnt
        cnt -= 1
        previous = data
        data, index = heapq.heappop(q)

    heapq.heappush(q,(data,index))
    q.sort(key=lambda x : x[1])

    return q[k%cnt][1]

print(solution([8,6,4,],15))

# 책에서 푼 방법

# import heapq
#
# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1
#
#     q = []
#     for i in range(len(food_times)):
#         heapq.heappush(q,(food_times[i],i+1))
#
#     sum_value = 0
#     previous = 0
#     length = len(food_times)
#
#     while sum_value + ((q[0][0] - previous) * length) <= k:
#         now = heapq.heappop(q)[0]
#         sum_value += (now - previous) * length
#         length -= 1
#         previous = now
#
#     result = sorted(q,key = lambda x : x[1])
#     return result[(k-sum_value) % length][1]