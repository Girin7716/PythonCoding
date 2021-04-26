# 동굴 탐험
from collections import deque
def solution(n, path, order):
    answer = True
    adj = {n: [] for n in range(n)}
    for s, e in path:
        adj[s].append(e)
        adj[e].append(s)

    precedeA = {}
    precedeB = {}

    for a, b in order:
        precedeA[a] = b
        precedeB[b] = a
        if b == 0:
            return False
        if a == 0:
            precedeA[0] = 0

    visited = [0]*n
    visited[0] = 1

    q = deque()
    q.append(0)

    while q:
        current = q.popleft()
        # 알고보니 아직 못가는 상태
        if current == precedeA.get(precedeB.get(current)):
            visited[current] = 2
        else:
            for neighbor in adj[current]:
                if visited[neighbor] == 0:
                    q.append(neighbor)
                    visited[neighbor] = 1

                    if precedeA.get(neighbor):  # 선행조건 일 때
                        if visited[precedeA[neighbor]] == 2:  # 이 선행조건을 필요로 하는 친구가 준비상태이면
                            q.append(precedeA[neighbor])  # 출발시킨다
                            visited[precedeA[neighbor]] = 1

                        precedeA[neighbor] = 0

    for i in visited:
        if i == 0:
            return False
    return answer


print(solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],[[8,5],[6,7],[4,1]]))
print(solution(9,[[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]],[[4,1],[5,2]]))
# print(solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],[[4,1],[8,7],[6,5]]))
# print(solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],[[6,5],[5,1],[2,7]]))
# print(solution(10,[[0,1],[0,2],[0,3],[1,4],[1,5],[3,6],[3,7],[4,8],[7,9]],[[2,9],[9,1],[8,3]]))
# print(solution(4,[[0,1],[0,2],[0,3]],[[0,2]]))
# print(solution(4,[[0,1],[0,2],[0,3]],[[2,0]]))
# print(solution(5,[[0,1],[0,2],[0,3],[1,4]],[[4,3]]))
print(solution(5,[[0,1],[1,2],[2,3],[3,4]],[[1,3],[4,2]]))
# print(solution(5,[[0,1],[1,2],[2,3],[3,4]],[[1,2],[4,3]]))