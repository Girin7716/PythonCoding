# 곱하기 혹은 더하기 / p312

input = input()

result = 0
for i in input:
    if i == '0':
        continue
    if i == '1':
        result += 1
        continue
    if result == 0:
        result += int(i)
    else:
        result *= int(i)

print(result)




