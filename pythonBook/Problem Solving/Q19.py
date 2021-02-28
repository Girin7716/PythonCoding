# 연산자 끼워 넣기 / p349 / BFS, DFS&BFS
from itertools import permutations

N = int(input())
A = list(map(int,input().split()))
Cnt = list(map(int,input().split())) # +,-,*,/

op = []
for i in range(4):
    if i == 0:
        for _ in range(Cnt[i]):
            op.append('+')
    elif i == 1:
        for _ in range(Cnt[i]):
            op.append('-')
    elif i == 2:
        for _ in range(Cnt[i]):
            op.append('*')
    else:
        for _ in range(Cnt[i]):
            op.append('/')
per = set(permutations(op,len(op)))

def operation(A,op):
    result = A[0]
    for i in range(len(op)):
        if op[i] == '+':
            result += A[i+1]
        elif op[i] == '-':
            result -= A[i+1]
        elif op[i] == '*':
            result *= A[i+1]
        elif op[i] == '/':
            result = int(result / A[i+1])
    return result

max =-100000000
min =100000000
for i in per:
    rem = operation(A,i)
    if max < rem:
        max = rem
    if min > rem:
        min = rem
print(max)
print(min)

# 2
# 5 6
# 0 0 1 0
#
# 3
# 3 4 5
# 1 0 1 0
#
# 6
# 1 2 3 4 5 6
# 2 1 1 1