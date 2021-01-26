# 서강그라운드

import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
items = list(map(int,input().split()))

INF = int(1e9)
D = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(r):
    a,b,d = map(int,input().split())
    D[a][b] = d
    D[b][a] = d
for i in range(1,n+1):
    D[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            D[i][j] = min(D[i][j],D[i][k]+D[k][j])

max_value = 0
for i in range(1,n+1):
    result = 0
    for j in range(1,n+1):
        if D[i][j] != INF and D[i][j] <= m:
            result += items[j-1]
    max_value = max(max_value,result)

print(max_value)
