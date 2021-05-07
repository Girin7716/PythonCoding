# 럭키 스트레이트
N = input()

left = 0
for i in range(len(N)//2):
    left += int(N[i])

right = 0
for i in range(len(N)//2,len(N)):
    right += int(N[i])
if left == right:
    print('LUCKY')
else:
    print('READY')
# 123402
# 7755