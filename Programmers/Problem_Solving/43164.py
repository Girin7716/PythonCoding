# 여행경로
def solution(tickets):
    answer = []
    tickets.sort()
    graph = {}
    for ticket in tickets:
        a, b = ticket
        graph[a] = graph.get(a,[]) + [b]

    stack = ['ICN']
    while stack:
        now = stack[-1]
        if now not in graph or len(graph[now]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(graph[now].pop())

    return answer[::-1]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))