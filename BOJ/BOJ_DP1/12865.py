# 평범한 배낭
N, K = map(int,input().split())

things = []
for _ in range(N):
    things.append(list(map(int,input().split())))   # weight, value

things.sort()

