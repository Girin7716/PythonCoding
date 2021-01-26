# 부분합
N,S = map(int,input().split())
data = list(map(int,input().split()))

min_value = int(1e9)
min_index = 0
for size in range(N):
    for i in range(N):
        rem = sum(data[i:i+size])
        if rem == S:
            print(size)
            exit()
        elif rem>S and rem < min_value:
            min_value = rem
            min_index = size
            break
print(min_index)
