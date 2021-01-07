# 행성 터널 / p398 / 그래프 이론 문제
import sys
input = sys.stdin.readline

N = int(input())

planet = []
for i in range(N):
    x,y,z = map(int,input().split())
    planet.append((x,y,z,i))


edges = []
planet.sort()
for i in range(N-1):
    cost = min(abs(planet[i][0] - planet[i+1][0]), abs(planet[i][1] - planet[i+1][1]), abs(planet[i][2] - planet[i+1][2]))
    edges.append((cost,planet[i][3],planet[i+1][3]))
planet.sort(key = lambda x:x[1])
for i in range(N-1):
    cost = min(abs(planet[i][0] - planet[i+1][0]), abs(planet[i][1] - planet[i+1][1]), abs(planet[i][2] - planet[i+1][2]))
    edges.append((cost,planet[i][3],planet[i+1][3]))
planet.sort(key = lambda x:x[2])
for i in range(N-1):
    cost = min(abs(planet[i][0] - planet[i+1][0]), abs(planet[i][1] - planet[i+1][1]), abs(planet[i][2] - planet[i+1][2]))
    edges.append((cost,planet[i][3],planet[i+1][3]))

edges.sort()

parent = [i for i in range(N)]

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,a,b,):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0
cnt = 0
for cost,a,b in edges:
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
        cnt += 1
    if cnt==N-1:
        break
print(result)



# 5
# 11 -15 -15
# 14 -5 -15
# -1 -1 -5
# 10 -4 -1
# 19 -4 19