# N-Queen
N = int(input())
cnt = 0

board = [[0 for _ in range(N)] for _ in range(N)]


def solution(depth):
    global cnt

    if depth == N:
        cnt+=1
        return

