# 고정점 찾기 / p368 / 이진 탐색
# O(logN)에 해결해야함.
from bisect import bisect_left, bisect_right
N = int(input())
data = list(map(int,input().split()))

def find_gojung(data,start,end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if mid > data[mid]: # right
        return find_gojung(data,mid+1,end)
    elif mid < data[mid]:   # left
        return find_gojung(data,start,mid-1)
    else:   # mid == data[mid]
        return mid

print(find_gojung(data,0,N))