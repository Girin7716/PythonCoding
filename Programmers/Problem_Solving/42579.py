# 베스트앨범
import heapq

def solution(genres, plays):
    answer = []
    bestMusic = {}
    totalplay = {}

    for i in range(len(genres)):
        totalplay[genres[i]] = totalplay.get(genres[i],0) + plays[i]
        try:
            heapq.heappush(bestMusic[genres[i]], (-plays[i], i))
        except:
            bestMusic[genres[i]] = [(-plays[i], i)]


    totalplay = sorted(totalplay, key=lambda x: totalplay[x],reverse=True)

    for t in totalplay:
        for i in range(len(bestMusic[t])):
            if i == 2:
                break
            answer.append(heapq.heappop(bestMusic[t])[1])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))