# 병든 나이트
# 값 입력받기
N,M = map(int,input().split())  # N : 세로, M : 가로

if N==1 or M==1 or (N==2 and M==2):
    print(1)
else:
    if N ==2:
        if (M-1)//2 + 1 >4:
            print(4)
        else:
            print((M-1)//2 + 1)
    elif N>=3:
        if M<=4:
            print(M)
        elif M>=7:
            print(5+M-7)
        else:
            print('4')