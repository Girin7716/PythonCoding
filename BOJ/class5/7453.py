# 합이 0인 네 정수
import sys
input = sys.stdin.readline

n = int(input())

A = []
B = []
C = []
D = []
for i in range(n):
    a,b,c,d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab = {}
cd = {}
for a in A:
    for b in B:
        if not ab.get(a+b):
            ab[a+b] = 1
        else:
            ab[a+b] += 1
for c in C:
    for d in D:
        if not cd.get(c+d):
            cd[c+d] = 1
        else:
            cd[c+d] += 1

result = 0
for i in ab:
    if cd.get(-i):
        result += ab[i] * cd[-i]

print(result)