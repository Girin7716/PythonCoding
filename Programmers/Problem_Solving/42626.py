# 더 맵게
import heapq

def solution(scoville, K):
    answer = 0
    pq = []

    for s in scoville:
        heapq.heappush(pq,s)

    while pq:
        one = heapq.heappop(pq)
        if one >= K:
            break
        elif pq == []:
            answer = -1
            break

        two = heapq.heappop(pq)
        newScoville = one + 2*two

        heapq.heappush(pq,newScoville)
        answer+=1

    return answer

print(solution([1, 2, 3, 9, 10, 12],7))
print(solution([1,2],7))