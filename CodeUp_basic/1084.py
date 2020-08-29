r,g,b = input().split()
r=int(r)
g=int(g)
b=int(b)

cnt=0
for i in range(r):
    for j in range(g):
        for k in range(b):
            cnt+=1
            print(i,j,k)

print(cnt)