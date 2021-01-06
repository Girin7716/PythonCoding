# 상자의 균형
N, L = map(int,input().split())
a = list(map(int,input().split()))

for i in range(N-1):
    total = 0
    cnt = 0
    for j in range(i+1,N):
        total += a[j]
        cnt+=1
    avg = total/cnt
    if a[i] - L < avg and a[i] + L > avg:
        continue
    else:
        print('unstable')
        exit()
print('stable')
