# 수 묶기
N = int(input())
# Seq = list(map(int, input().split()))
Seq = []
for i in range(N):
    Seq.append(int(input()))

Seq.sort(reverse=True)

# minus zero plus 개수 파악
minus, zero, plus, one = 0, 0, 0, 0
for i in range(len(Seq)):
    if Seq[i] < 0:
        minus += 1
    elif Seq[i] == 0:
        zero += 1
    elif Seq[i] == 1:
        one += 1
    else:
        plus += 1

sum = 0
if plus % 2 == 0:  # plus 짝수
    for i in range(0, plus, 2):
        sum += Seq[i] * Seq[i + 1]
else:
    for i in range(0, plus - 1, 2):
        sum += Seq[i] * Seq[i + 1]
    sum += Seq[plus - 1]

sum+=one

if minus % 2 == 0 and minus!=0:
    for i in range(N - 1, plus +one+ zero, -2): # plus + one + zero + minus = N
        sum += Seq[i] * Seq[i - 1]
elif minus!=0:  # minus가 홀 수
    for i in range(N - 1, plus +one+ zero, -2):
        sum += Seq[i] * Seq[i - 1]
    if zero == 0:
        sum += Seq[N - minus]

print(sum)
