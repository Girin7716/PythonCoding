str = list(input())
bomb = list(input())
s_len = len(str)
size = len(bomb)

index = 0
result = []

for i in range(size):
    result.append(str[index])
    index+=1

cnt = index
while True:
    if result[index - size:index] == bomb:
        for _ in range(size):
            result.pop()
            index-=1
    try:
        result.append(str[cnt])
        index+=1
        cnt+=1
    except:
        break

if result:
    print(''.join(result))
else:
    print('FRULA')