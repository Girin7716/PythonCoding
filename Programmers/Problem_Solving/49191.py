# 순위
from collections import deque

def solution(n, results):
    answer = 0
    winner = [[] for _ in range(n+1)]
    loser = [[] for _ in range(n+1)]
    total = [0] * (n+1)

    for result in results:
        a,b = result
        loser[b].append(a)
        winner[a].append(b)

    def bfs(graph,i):
        q = deque()
        q.append(i)
        visited = [False] * (n+1)

        while q:
            now = q.popleft()
            for nxt in graph[now]:
                if visited[nxt] is True:
                    continue
                visited[nxt] = True
                total[i] += 1
                q.append(nxt)


    for i in range(1,n+1):
        bfs(winner,i)
        bfs(loser,i)

    for t in total:
        if t == n-1:
            answer+=1

    return answer

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))