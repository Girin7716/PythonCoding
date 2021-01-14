# N과 M(9)
from itertools import permutations

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
data = map(int,input().split())

result = list(set(permutations(data,M)))
result.sort()

for i in result:
    for j in i:
        print(j,end=' 15')
    print()
