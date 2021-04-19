# H-Index
def solution(citations):
    answer = 0
    length = len(citations)
    citations.sort()
    for i in range(length):
        if citations[i] >= length - i:
            answer = length - i
            break

    return answer

print(solution([3, 0, 6, 1, 5]))
print(solution([0,1,2,3,4,5,6,7]))
print(solution([1,5,8,14,19]))
print(solution([1,7,8,14,19]))
print(solution([22,24]))
print(solution([1]))
print(solution([0,0,0]))