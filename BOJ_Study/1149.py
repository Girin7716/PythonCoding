# RGB 거리
N = int(input())
costs = []
for i in range(N):
    costs.append(list(map(int,input().split())))

result = 0
i_rem = 0
for i in range(N):
    for j in range(N):
