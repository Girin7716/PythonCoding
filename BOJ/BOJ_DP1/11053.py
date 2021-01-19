# 가장 긴 증가하는 부분 수열
N = int(input())
arr = list(map(int,input().split()))
result = [1] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            result[i] = max(result[i],result[j]+1)

print(max(result))