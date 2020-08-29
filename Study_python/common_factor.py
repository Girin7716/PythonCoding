# 문제>최대공약수와 최소공배수
# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수
# solution을 작성하기

def solution(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t

    answer = [c, int(a * b / c)]

    return answer


print(solution(3, 11))
