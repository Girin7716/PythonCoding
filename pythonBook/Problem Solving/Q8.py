# 문자열 재정렬 / Q8 / 구현 문제
N = input()

alpha = []
sum = 0
for x in N:
    try:    # number
        if 1<=int(x)<=9:
            sum += int(x)
    except: # english
        alpha.append(x)
alpha.sort()
alpha.append(str(sum))

print(''.join(alpha))
# for x in alpha:
#     print(x,end='')