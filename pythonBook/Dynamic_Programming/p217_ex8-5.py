# 1로 만들기
# 풀이 시간 20분 / 시간 제한 1초 / 메모리 제한 128MB
## 책에서 푼 방법 ##
x = int(input())

d = [0] * 30001 #X 범위가 30,000

for i in range(2,x+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i%3==0:
        d[i] = min(d[i],d[i//3]+1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i%5==0:
        d[i] = min(d[i],d[i//5]+1)

print(d[x])

## 내가 푼 방법 ##

# 틀림;;
# X = int(input())
#
# count = 0
# while X!=1:
#     count += 1
#     if not X%5==0 or X%3==0 or X%2==0:
#         X-=1
#         continue
#     if X%5==0:
#         X/=5
#     elif X%3==0:
#         X/=3
#     elif X%2==0:
#         X/=2
#
# print(count)

# 해설보고 다시 풀어봄
# X = int(input())
#
# d = [0] * 30001
#
#
# for x in range(2,X+1):
#     d[x] = d[x-1] + 1
#     if x%2==0:
#         d[x] = min(d[x],d[x//2]+1)
#     if x%3==0:
#         d[x] = min(d[x],d[x//3]+1)
#     if x%5==0:
#         d[x] = min(d[x],d[x//5]+1)
#
# print(d[X])
