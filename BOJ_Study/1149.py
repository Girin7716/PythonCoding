# RGB 거리
import sys
N = int(input())

costs = []
for i in range(N):
    costs.append(list(map(int,sys.stdin.readline().split())))
result = [costs[0]]
for i in range(N-1):
    result.append(list(10000001 for _ in range(3)))

for i in range(N-1):
    for j in range(3):
        if result[i][j] + costs[i+1][(j+1)%3] < result[i+1][(j+1)%3]:
            result[i+1][(j+1)%3] = result[i][j] + costs[i+1][(j+1)%3]
        if result[i][j] + costs[i+1][(j+2)%3] < result[i+1][(j+2)%3]:
            result[i+1][(j+2)%3] = result[i][j] + costs[i+1][(j+2)%3]

print(min(result[N-1][0],result[N-1][1],result[N-1][2]))