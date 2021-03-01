# 입국심사
def solution(n, times):
    answer = 0
    left = 1
    right = min(times) * n

    while left <= right:
        mid = (left+right)//2
        temp = n

        for t in times:
            temp -= mid//t
            if temp <= 0:
                right = mid - 1
                answer = mid
                break

        if temp >0:
            left = mid + 1

    return answer




# #naive
# import heapq
#
# def solution(n, times):
#     answer = 0
#     pq = []
#     for t in times:
#         heapq.heappush(pq,[t,t])
#
#     while n != 0 :
#         answer,ori = heapq.heappop(pq)
#         heapq.heappush(pq,[ori + answer,ori])
#         n-=1
#
#     return answer

print(solution(6,[7,10]))