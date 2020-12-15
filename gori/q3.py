# 미아 노트
N,H,W = map(int,input().split())
a=[]
for i in range(H):
    a.append(input())

new = ['?' for _ in range(N*W)]

for i in range(H):
    for j in range(N*W):
        if a[i][j] != '?':
            new[j] = a[i][j]

result = []
check = 0
cnt = 0
for i in new:
    cnt+=1
    if i == '?':
        check+=1
    else:
        rem = i
    if check==W:
        result.append('?')
        check = 0
        cnt=0
    elif cnt==W:
        result.append(rem)
        cnt=0
        check=0

print(''.join(result))
