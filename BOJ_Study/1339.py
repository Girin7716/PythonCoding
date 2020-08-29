# 단어 수학
N = int(input())

alpha = []
alpha_collection = {}
for i in range(N):
    alpha.append(input())

for i in range(N):
    digit = 1
    for j in range(len(alpha[i])-1,-1,-1):
        if alpha[i][j] not in alpha_collection:
            alpha_collection[alpha[i][j]]=digit
        else:
            alpha_collection[alpha[i][j]]+=digit
        digit*=10

sort_alpha = sorted(alpha_collection.values(),reverse=True)

sum = 0
num = 9
for i in range(len(sort_alpha)):
    sum += sort_alpha[i]*num
    num-=1
print(sum)