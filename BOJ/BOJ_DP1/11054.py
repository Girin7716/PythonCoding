# 가장 긴 바이토닉 부분 수열
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

rem1 = [1] * N
rem2 = [1] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            rem1[i] = max(rem1[i],rem1[j]+1)

for i in range(N-1,-1,-1):
    for j in range(i,N):
        if arr[i] > arr[j]:
            rem2[i] = max(rem2[i],rem2[j]+1)
    rem1[i]+=rem2[i]

print(max(rem1)-1)