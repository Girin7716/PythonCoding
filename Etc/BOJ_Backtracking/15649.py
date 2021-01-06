N,M=map(int,input().split())
visited = [0] * (N+1)
rem = []

def solution(depth):
    if depth == M:
        for i in range(len(rem)):
            print(rem[i], end=' ')
        print()
        return
    for i in range(1,N+1):
        if visited[i]==0:
            visited[i] = 1
            rem.append(i)
            solution(depth+1)
            rem.pop()
            visited[i] = 0

solution(0)