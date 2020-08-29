N,M = map(int,input().split())
visited = [0]*(N+1)
out = []
cnt = 1

def solution(depth):
    if depth == M:
        for i in range(len(out)):
            print(out[i],end=' ')
        print()
        return
    for i in range(1,N+1):
        if visited[i]==0:
            visited[i]=1
            out.append(i)
            solution(depth+1)
            out.pop()
            for j in range(i+1,N+1):
                visited[j] = 0


solution(0)


