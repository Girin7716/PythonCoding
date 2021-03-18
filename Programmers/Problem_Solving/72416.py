# 매출 하락 최소화
def solution(sales, links):
    answer = 0
    graph = [[] for _ in range(len(sales)+1)]
    for link in links:
        leader,member = link
        #graph[leader].append((sales[member-1],member))
        graph[leader].append(member)
    print(graph)


    return answer


print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],[[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))
print(solution([5, 6, 5, 3, 4],[[2,3], [1,4], [2,5], [1,2]]))
print(solution([5, 6, 5, 1, 4],	[[2,3], [1,4], [2,5], [1,2]]))
print(solution([10, 10, 1, 1],	[[3,2], [4,3], [1,4]]))