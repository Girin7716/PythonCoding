# 키패드 누르기 09:04 ~ 09:40
from collections import deque
def solution(numbers, hand):
    answer = ''
    q = deque(numbers)
    left_location = 10
    right_location = 12
    while q:
        now = q.popleft()
        if now == 0:
            now = 11
        if now%3 == 1:
            answer += 'L'
            left_location = now
        elif now % 3 == 0:
            answer += "R"
            right_location = now
        else:
            left_dist = (int((abs(now-left_location)/3))) + abs(now-left_location)%3
            right_dist = (int((abs(now - right_location) / 3))) + abs(now-right_location)%3
            if left_dist < right_dist:
                left_location = now
                answer += "L"
            elif left_dist > right_dist:
                right_location = now
                answer += "R"
            elif left_dist == right_dist and hand == "right":
                right_location = now
                answer += "R"
            elif left_dist == right_dist and hand == "left":
                left_location = now
                answer += "L"

    return answer


# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"))