# 긴급 회의
N = int(input())
a = list(map(int,input().split()))
# 0 : skipped, 숫자는 그번호에게 투표

dic = {}
for i in range(N+1):
    dic[i] = 0

for i in a:
    dic[i] +=1

def f2(x):
    return x[1]

res = sorted(dic.items(),key=f2,reverse = True)

# 3
# 0 1 2

if res[0][1] == res[1][1]:
    if res[1][1] == res[2][1]:
        print('skipped')
        exit()
    if res[0][0] == 0:
        print(res[1][0])
    elif res[1][0] == 0:
        print(res[0][0])
    else:
        print('skipped')
elif res[0][0] == 0 and res[0][1] == N:
    print('skipped')
elif res[0][0] == 0:
    if res[1][1] == res[2][1]:
        if res[1][0] == 0:
            print(res[2][0])
        elif res[2][0] == 0:
            print(res[1][0])
        else:
            print('skipped')
    else:
        print(res[1][0])
else:
    print(res[0][0])