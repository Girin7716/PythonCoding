# 양팔 저울
N = int(input())
sinker = list(map(int,input().split())) + [0]
M = int(input())
marbles = list(map(int,input().split())) + [0]
visited = [[False for _ in range(15001)] for _ in range(31)]


def backtracking(result, depth):
    if depth > N: return
    if visited[depth][result]: return

    visited[depth][result] = True

    backtracking(result+sinker[depth],depth+1)
    backtracking(abs(result-sinker[depth]),depth+1)
    backtracking(result,depth+1)

backtracking(0,0)

for marble in marbles:
    if marble == 0:
        continue
    if marble > 15000:
        print('N',end=' ')
    elif visited[N][marble]:
        print('Y',end=' ')
    else:
        print('N',end=' ')