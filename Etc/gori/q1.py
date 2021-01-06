# q1 사토르 마방진

N = int(input())
a = []
for i in range(N):
    a.append(input())

cnt = 0
check = 0
for j in range(N):
    b = []
    for i in a:
        b.append(i[cnt])
    if a[cnt] == ''.join(b):
        check+=1
    else:
        print('NO')
        break
    cnt += 1

if check == N:
    print('YES')