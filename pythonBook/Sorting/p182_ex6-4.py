# 두 배열의 원소 교체
## 책에서 푼 방법 ##
# n,k = map(int,input().split())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
#
# a.sort()
# b.sort(reverse=True)
#
# for i in range(k):
#     if a[i] < b[i]:
#         a[i],b[i] = b[i],a[i]
#     else:
#         break
# print(sum(a))


## 내가 푼 방법 ##
N,K = map(int,input().split())

array_A = list(map(int,input().split()))
array_B = list(map(int,input().split()))

array_A = sorted(array_A)
array_B = sorted(array_B)

for i in range(K):
    if array_A[i] < array_B[N-1-i]:
        array_A[i],array_B[N-1-i] = array_B[N-1-i],array_A[i]
    else:
        break

print(sum(array_A))
# result = 0
# # for i in array_A:
# #     result+= i
# #
# # print(result)
