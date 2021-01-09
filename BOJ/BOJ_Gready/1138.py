# 한 줄로 서기
N = int(input())
known = list(map(int,input().split()))

while 0 in known:
    for i in range(len(known)):
        if known[i] == 0:
            print(i+1,end=' ')
            for j in range(i+1):
                known[j]-=1
            break