# 디스크 컨트롤러
import heapq

def solution(jobs):
    answer = 0
    j_len = len(jobs)

    jobs_pq = []
    for job in jobs:
        heapq.heappush(jobs_pq,job)

    now_time = 0
    pq = []
    while jobs_pq:
        while jobs_pq:
            job = heapq.heappop(jobs_pq)
            if job[0] <= now_time:
                heapq.heappush(pq,[now_time+job[1],job])
            else:
                heapq.heappush(jobs_pq,job)
                break
        if pq == []:
            job =heapq.heappop(jobs_pq)
            now_time = job[0]
            heapq.heappush(jobs_pq,job)
            continue

        now_time, job = heapq.heappop(pq)
        answer += (now_time-job[0])

        while pq:
            time,job = heapq.heappop(pq)
            heapq.heappush(jobs_pq,job)

    answer /= j_len

    return int(answer)


print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[0, 3], [4, 9], [5, 6]]))
