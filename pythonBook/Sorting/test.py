
good = []
for i in range(40):
    a,b,c,d = map(float,input().split())
    good.append((a,b,c,d))

#good.sort(key=b,reverse=True)
f= sorted(good, key = lambda x : (-x[3]))
g= sorted(good, key = lambda x : (-x[1]))
print("이론 등수")
for i in range(40):
    print(i+1,g[i])

print("총합 등수")
for i in range(40):
    print(i+1,f[i])


