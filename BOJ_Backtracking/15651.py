N,M = map(int,input().split())

visited = [0 for _ in range(N+1)]
out = []

def solution(depth):
    if depth == M:
        for i in range(len(out)):
            print(out[i],end=' ')
        print()
        return
    for i in range(1,N+1):
        if visited[i] == 0:
            visited[i]=1
            out.append(i)
            solution(depth+1)
            out.pop()
            visited[i]=0
        else:
            out.append(i)
            solution(depth+1)
            out.pop()

solution(0)