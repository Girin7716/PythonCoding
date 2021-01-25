# 백트래킹은 dfs + promising이 합쳐진 모습. dfs를 돌릴 때 promising함수의 결과가 false라면 무신 true라면 실행
N = int(input())
row = [0] * N
result = 0

def promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def dfs(x):
    global result

    if x == N:
        result += 1

    else:
        for i in range(N):
            row[x] = i
            if promising(x):
                dfs(x + 1)

dfs(0)
print(result)