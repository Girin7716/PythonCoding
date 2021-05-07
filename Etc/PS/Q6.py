# 무지의 먹방 라이브
import heapq

def solution(food_times, k):
    pq = []
    for idx, food_time in enumerate(food_times):
        heapq.heappush(pq,(food_time,idx+1))

    prev_food = 0
    now_food = 0

    while pq:
        now_food = pq[0][0]
        if k < (now_food-prev_food) * len(pq):
            break
        k -= (now_food - prev_food) * len(pq)

        prev_food = pq[0][0]
        value,idx = heapq.heappop(pq)
    if pq == []:
        return -1
    pq.sort(key = lambda x:x[1])
    k = k % len(pq)

    return pq[k][1]

print(solution([1,1,1,1],4))
print(solution([3,1,2],5))
print(solution([8,6,4],15))