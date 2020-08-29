# 위에서 아래로
## 책에서 푼 방법 ##
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array,reverse=True)

for i in array:
    print(i,end=' ')

## 내가 푼 방법 ##
# N = int(input())
#
# Seq = []
# for i in range(N):
#     Seq.append(input())
# result = sorted(Seq,reverse=True)
#
# for i in result:
#     print(i,end=' ')
