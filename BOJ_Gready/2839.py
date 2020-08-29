N = int(input())


def solution(N):
    cnt = 0
    while N >= 0:
        if N % 5 == 0:
            cnt += N // 5
            return cnt
        if N==0:
            return cnt
        N-=3
        cnt+=1
    return -1

print(solution(N))