# 안테나 / p360 / 정렬
N = int(input())
data = list(map(int,input().split()))

data.sort()
print(data[(N-1)//2])