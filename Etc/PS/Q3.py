# 문자열 뒤집기
S = input()

data = [0,0]
prev = S[0]
for str in S[1:]:
    if prev != str:
        data[int(prev)] += 1
        prev = str
data[int(prev)] += 1
print(min(data))
# 0001100