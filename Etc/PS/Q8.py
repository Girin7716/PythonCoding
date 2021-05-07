# 문자열 재정렬
import re

S = input()

result = 0
alpha = []
for str in S:
    if str.isalpha():
        alpha.append(str)
    else:
        result += int(str)

alpha.sort()
alpha.append(result)
for a in alpha:
    print(a,end='')


# for str in S:
#     if str
    # print(str)

# K1KA5CB7  result -> ABCKK13
# AJKDLSI412K4JSJ9D     result -> ADDIJJJKKLSS20