# 곱하기 혹은 더하기
S = input()

result = int(S[0])
for str in S[1:]:
    if str == '0' or str == '1' or result == 0 or result == 1:
        result += int(str)
    else:
        result *= int(str)

print(result)

# 02984
# 567