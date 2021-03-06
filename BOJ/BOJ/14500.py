# 테트로미노
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

tet = [
    [(0,0), (0,1), (1,0), (1,1)], # ㅁ
    [(0,0), (0,1), (0,2), (0,3)], # ㅡ
    [(0,0), (1,0), (2,0), (3,0)], # ㅣ
    [(0,0), (0,1), (0,2), (1,0)],
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], # ㄴ
    [(0,0), (0,1), (0,2), (1,2)], # ㄱ
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], # ㅜ
    [(1,0), (1,1), (1,2), (0,1)], # ㅗ
    [(0,0), (1,0), (2,0), (1,1)], # ㅏ
    [(1,0), (0,1), (1,1), (2,1)], # ㅓ
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]
answer = 0

def search(t):
    global answer
    # b1,b2,b3,b4 = t
    for i in range(N):
        for j in range(M):
            temp = 0
            flag=False
            for k in range(4):
                if t[k][0]+i < 0 or t[k][0]+i >= N or t[k][1]+j < 0 or t[k][1]+j >= M:
                    flag = True
                    continue
                temp+=board[t[k][0]+i][t[k][1]+j]
            if flag is True:
                continue
            answer = max(answer,temp)

for t in tet:
    search(t)

print(answer)

# 5 5
# 1 2 3 4 5
# 5 4 3 2 1
# 2 3 4 5 6
# 6 5 4 3 2
# 1 2 1 2 1