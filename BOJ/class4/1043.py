# 거짓말
import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N,M = map(int,input().split())
known_people = list(map(int,input().split()))   # 몇명, 사람1, 사람2, ~~~
parent = [i for i in range(N+1)]
party = []
for i in range(M):
    party.append(list(map(int,input().split())))

for p in party:
    rem1 = find_parent(parent,p[1])
    for i in range(p[0]-1):
        rem2 = find_parent(parent,p[i+2])
        if rem1 != rem2:
            union_parent(parent,p[1],p[i+2])
# print(parent) -> [0, 1, 2, 3, 4, 1, 2, 7, 7, 9, 3]
known_people = known_people[1:]

for i in range(len(known_people)):
    known_people[i] = find_parent(parent,known_people[i])

for i in range(len(party)):
    for j in range(party[i][0]):
        party[i][j+1] = find_parent(parent,party[i][j+1])

result = M
for i in range(len(party)):
    for j in range(1,party[i][0]+1):
        if party[i][j] in known_people:
            result-=1
            break
print(result)