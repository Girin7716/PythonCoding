# 큰 수의 법칙
## 책에서 푼 방법 ##
n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1)) * k
count += m% (k+1)

result =0
result += (count) * first
result += (m-count) * second

print(result)

## 내가 푼 방법 ##
# N,M,K = map(int,input().split())
# list = list(map(int,input().split()))
#
# list.sort(reverse=True)
#
# count=0
# sum=0
# for i in range(M):  # 6 5 4 4 2
#     if count == K:
#         count=0
#         sum+=list[1]
#         i+=1
#         continue
#     count += 1
#     sum += list[0]
# print(sum)