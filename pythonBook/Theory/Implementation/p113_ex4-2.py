# 시각 / 완전 탐색(브루트 포스)
## 책에서 푼 방법 ##
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k): # ex> 03시20분35초 -> '3' in 032035 ?
                count += 1

print(count)

## 내가 푼 방법 ##
# N = int(input())
#
# hour, minute, second = 0, 0, 0
# count = 0
#
# for i in range(N + 1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) or '3' in str(j) or '3' in str(k):
#                 count += 1
#
# print(count)
