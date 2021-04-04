# 두 개 뽑아서 더하기
from itertools import combinations

def solution(numbers):
    answer = set()
    for c in combinations(numbers,2):
        answer.add(c[0]+c[1])

    answer = list(answer)
    answer.sort()
    return answer

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))