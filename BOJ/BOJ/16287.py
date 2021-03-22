# Parcel
import sys
input = sys.stdin.readline

w,n = map(int,input().split())
parcel = list(map(int, input().split()))
dp = [False] * (w+1)

'''
parcel을 앞에서부터 검사함.
i와,i보다 큰 값들의 합을 구하고 dp[w-parcel[i]-parcel[j]이면 이미 i보다 작은 인덱스의 값들의 합이 있었다는 의미이므로 'yes' 출력
i 번째의 값 이전까지 2개씩 뽑아내면서 두 무게의 합이 w 보다 작다면 해당 무게의 dp를 True로 바꿈
'''
def check():
    for i in range(n):
        for j in range(i + 1, n):
            if parcel[i] + parcel[j] < w and dp[w - parcel[i] - parcel[j]]:
                return True
        for j in range(i):
            if parcel[i] + parcel[j] < w:
                dp[parcel[i] + parcel[j]] = True

    return False

if check():
    print('YES')
else:
    print('NO')

# 21 7
# 1 2 4 5 6 8 10

# 시간초과
# import sys
# input = sys.stdin.readline
#
# w,n = map(int,input().split())
# parcel = list(map(int,input().split()))
#
# parcel.sort()
#
# dp = [False] * (w+1)
#
# def check():
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             if parcel[i] + parcel[j] <= w and dp[parcel[i] + parcel[j]] is False:
#                 dp[parcel[i] + parcel[j]] = (i, j)
#
#         for j in range(i + 1, n):
#             weight = w - parcel[i] - parcel[j]
#             if weight < 0:
#                 continue
#             if parcel[i]+parcel[j]<=w:
#                 rem1, rem2 = dp[parcel[i] + parcel[j]]
#             if dp[weight] is not False and (i != rem1 and i != rem2) and (j != rem1 and j != rem2):
#                 return True
#     return False
#
# if check():
#     print('YES')
# else:
#     print('NO')


# 순열(DFS)로 풀어보기 -> 메모리초과
# from itertools import permutations
# import sys
#
# input = sys.stdin.readline
#
# w,n = map(int,input().split())
# parcel = list(map(int,input().split()))
#
#
# def check():
#     for p in list(permutations(parcel, 4)):
#         if w == sum(p):
#             return True
#     return False
#
# if check():
#     print('YES')
# else:
#     print('NO')