# 단어 암기
N, M = map(int,input().split())
alpha = [[] for _ in  range(26)]
for i in range(N):
    words = set(input())
    for word in words:
        alpha[ord(word)-ord('a')].append(i)
        print(word,ord(word)-ord('a'))
check = [0] * (N)
answer = N
for _ in range(M):
    o, x = input().split()
    if o == '1':    # 까먹음
        for i in alpha[ord(x)-ord('a')]:
            if check[i] == 0:
                answer-=1
            check[i]+=1
    else:   #기억해냄
        for i in alpha[ord(x)-ord('a')]:
            check[i] -= 1
            if check[i] == 0:
                answer +=1
    print(answer)

# import sys
# input=sys.stdin.readline
#
# n,m=map(int,input().split())
# a=[[] for _ in range(26)]
#
# for i in range(n):
#     w=set(input().rstrip())
#     for x in w:
#         a[ord(x)-97].append(i)
# c=[0]*n
# ans=n
# for _ in range(m):
#     o,x=input().split()
#     if o=='1':
#         for i in a[ord(x)-97]:
#            if c[i]==0:
#                 ans-=1
#             c[i]+=1
#     else:
#         for i in a[ord(x)-97]:
#             c[i]-=1
#             if c[i]==0:
#                 ans+=1
#     print(ans)



# RuntimeError(ValueError)
# import sys
# input = sys.stdin.readline
#
# N,M= map(int,input().split())
# remember = 0
# for i in range(26):
#     remember = remember + (1<<i)
# arr = [0] * (100001)
# for i in range(N):
#     temp = input()
#
#     for j in range(len(temp)):
#         cur = ord(temp[j]) - ord('a')
#         arr[i] |= (1<<cur)
#
# for i in range(M):
#     count = 0
#     o,x = input().split()
#
#     remember ^= (1<<(ord(x)-ord('a')))
#
#     for j in range(N):
#         if (arr[j] & remember) == arr[j]:
#             count+=1
#     print(count)


# TLE
# from bisect import bisect_left, bisect_right
#
# # 값이 [left_value,right_value]인 데이터의 개수를 반환하는 함수
# def count_by_range(a, left_value, right_value):
#     right_index = bisect_right(a,right_value)
#     left_index = bisect_left(a,left_value)
#     return right_index - left_index
#
# N,M=map(int,input().split())
# words = [list(input()) for _ in range(N)]
# for word in words:
#     word.sort()
# forget = []
# #print(count_by_range(a,5,5))
# for i in range(M):
#     num, fg = input().split()
#     answer = 0
#     if num == '1':  # 까먹기
#         forget.append(fg)
#         for word in words:
#             check = False
#             for f in forget:
#                 if count_by_range(word,f,f) !=0:
#                     check = True
#             if check == False:
#                 answer+=1
#         print(answer)
#     else:   # 기억
#         forget.remove(fg)
#         for word in words:
#             check = False
#             for f in forget:
#                 if count_by_range(word,f,f) !=0:
#                     check = True
#             if check == False:
#                 answer+=1
#         print(answer)

# import sys
# input = sys.stdin.readline
#
# N, M = map(int,input().split())
# words = [input() for _ in range(N)]
#
# forget = []
#
# for i in range(M):
#     num, word = input().split()
#     answer = 0
#     if num == '1':  # 잊어버리기
#         forget.append(word)
#         for j in words:
#             check = False
#             for k in forget:
#                 if k in j:
#                     check = True
#                     break
#             if check == False:
#                 answer += 1
#         print(answer)
#     else:   # 기억해내기
#         forget.remove(word)
#         for j in words:
#             check = False
#             for k in forget:
#                 if k in j:
#                     check = True
#                     break
#             if check == False:
#                 answer += 1
#         print(answer)