# N과 M (2)
from itertools import combinations

N, M = map(int,input().split())
data = [i for i in range(1,N+1)]

result = list(combinations(data,M))
for i in result:
    for j in i:
        print(j,end=' ')
    print()