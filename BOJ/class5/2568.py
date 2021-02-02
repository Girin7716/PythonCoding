# 전깃줄 - 2
N = int(input())
data = []
for _ in range(N):
    a,b = map(int,input().split())
    data.append((a,b))

data.sort()
record = []
lis = []

lis.append(data[0][1])
record.append(1)

def binary_serach(e):
    start = 0
    end = len(lis)
    while start < end:
        mid = (start + end) // 2
        if e > lis[mid]:
            start = mid + 1
        else:
            end = mid
    return end

cnt = 1
for i in range(1,N):
    if data[i][1] > lis[-1]:
        lis.append(data[i][1])
        cnt += 1
        record.append(cnt)
    else:
        pos = binary_serach(data[i][1])
        lis[pos] = data[i][1]
        record.append(pos+1)

length = len(lis)
temp = length
rem = []
cnt = N-1
for x in record[::-1]:
    if temp == x:
        temp-=1
        cnt-=1
    else:
        rem.append(cnt)
        cnt-=1

print(N-length)
rem.sort()
for i in rem:
    print(data[i][0])