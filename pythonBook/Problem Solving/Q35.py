# 못생긴 수 / p381 / DP
n = int(input())

idx2=1
idx3=1
idx5=1
cnt = 1
ugly = [1]
while True:
    if cnt == n:
        break

    two = 2*idx2
    three = 3*idx3
    five = 5*idx5

    min_value = min(two, three, five)
    if  min_value == two:
        idx2+=1
    if min_value == three:
        idx3+=1
    if min_value == five:
        idx5+=1
    ugly.append(min_value)
    cnt+=1

print(ugly[n-1])