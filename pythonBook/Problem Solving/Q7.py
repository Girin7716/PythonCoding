# 럭키 스트레이트 / Q7 / 구현 문제
N = "".join(input())
arr = [0,0]

mid = len(N)/2 - 1
for i in range(len(N)):
    if i <= mid:
        arr[0]+=int(N[i])
    else:
        arr[1]+=int(N[i])

if arr[0] == arr[1]:
    print('LUCKY')
else:
    print('READY')