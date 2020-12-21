# 책에서 푼 방법
N,M = map(int,input().split())

data = list(map(int,input().split()))
data.sort()
weight = [0 for _ in range(10+1)]

for x in data:
    weight[x]+=1

result = 0
for i in range(1,M+1):
    N -= weight[i]
    result += weight[i] * N

print(result)
# #Naive
# N,M = map(int,input().split())
#
# data = list(map(int,input().split()))
#
# count = 0
#
# for i in range(len(data)):
#     for j in range(i+1,len(data)):
#         if data[i] == data[j]:
#             continue
#         count+=1
# print(count)