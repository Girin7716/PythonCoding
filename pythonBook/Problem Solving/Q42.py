# 탑승구 / q395 / 그래프 이론 문제
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

G = int(input())
P = int(input())

parent = [i for i in range(G+1)]

def is_empty(parent,x):
    if x == 0:
        return False
    if find_parent(parent,x) != 0:
        union_parent(parent,0,x)
    else:
        return is_empty(parent,x-1)
    return True

x = []
for i in range(P):
    x.append(int(input()))


for p in range(P):
    # check
    check = is_empty(parent,x[p])
    if check == False:
        print(p)
        exit()
print(P)

