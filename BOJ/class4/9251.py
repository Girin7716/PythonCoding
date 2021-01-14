# LCS
from itertools import combinations

str1 = input()
str2 = input()

result = 0
for i in range(1,len(str1)+1):
    a = list(set(combinations(str1,i)))
    b = list(set(combinations(str2,i)))
    for j in a:
        if j in b:
            result = i
            break
print(result)