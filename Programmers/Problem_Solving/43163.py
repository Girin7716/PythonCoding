# 단어 변환
import heapq

def solution(begin, target, words):
    answer = 0
    if target not in words:
        answer = 0
        return answer
    if begin not in words:
        words.append(begin)

    length = len(words)
    graph = {}
    for word in words:
        graph[word] = []

    def check(i, j,l):
        cnt = 0
        for k in range(l):
            if words[i][k] != words[j][k]:
                cnt += 1
        if cnt >= 2:
            return False
        return True
    l = len(begin)
    for i in range(length):
        for j in range(i + 1, length):
            if check(i, j,l):
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])

    pq = []
    heapq.heappush(pq,(0,begin))
    while pq:
        cnt,now = heapq.heappop(pq)
        if cnt > length:
            break
        if now == target:
            answer = cnt
            break
        for nxt in graph[now]:
            heapq.heappush(pq,(cnt+1,nxt))

    return answer

print(solution("hit","hhh",["hhh","hht"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit","cog",["cog","log","lot","dog",'dot','hot']))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
print(solution('hit','wow',['hot','dog','dot','wow']))