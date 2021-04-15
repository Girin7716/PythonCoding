# 주식가격
from collections import deque

def solution(prices):
    answer = [0] * (len(prices))
    q = deque()
    index = -1
    for price in prices:
        index+=1
        if q == deque():
            q.append((price,index))
            continue

        while q != deque():
            if q[-1][0] > price:
                p,i = q.pop()
                answer[i] = index-i
            else:
                break
        q.append((price,index))

    last_p,last_i = q.pop()
    while q:
        p,i = q.popleft()
        answer[i] = last_i-i

    return answer

# (1,0),(2,2,),(1,4),(7,5)
print(solution([1,5,2,3,1,7]))  # 5,1,2,1,1,0
print(solution([3,1,5,2,4,7]))  # 1,4,1,2,1,0
print(solution([1, 2, 3, 2, 3]))
print(solution([1,2,3,4,5]))
print(solution([5,4,3,2,1]))
print(solution([1,3,2,3,4,6]))
print(solution([1,2,3,2,3,1]))
print(solution([1,1,1,1,1]))
print(solution([1,2,3,2,3,3,1]))
print(solution([3,1]))