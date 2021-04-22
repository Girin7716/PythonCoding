# 이중우선순위큐
from collections import deque
def solution(operations):
    answer = deque()

    for op in operations:
        if op[0] == 'I':
            num = int(op.split()[1])
            answer.append(num)
            answer = deque(sorted(answer))
        else:
            if answer == deque():
                continue
            if op.split()[1] == '1':    # 최댓값 삭제
                answer.pop()
            else:   # 최솟값 삭제
                answer.popleft()
    if answer == deque():
        answer = [0,0]
        return answer

    return [answer[-1],answer[0]]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))
print(solution(["I 7","I 5","I -5","I -199","I 9"]))
print(solution(["I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1", "I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1"]))
print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))
print(solution(["D 5"]))