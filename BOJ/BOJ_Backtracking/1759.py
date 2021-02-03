# 암호 만들기
def check(combStr):
    vowel = 0
    consonant = 0

    for char in combStr:
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowel += 1
        else:
            consonant += 1

    if consonant >= 2 and vowel >= 1:
        return True
    else:
        return False


def solution(L, inputList, combStr, index):
    if len(combStr) is L:
        if check(combStr) is True:
            print(''.join(combStr))
        return;

    if index >= len(inputList):
        return;

    solution(L, inputList, combStr + list(inputList[index]), index + 1)
    solution(L, inputList, combStr, index + 1)


answer = 0
L, C = map(int, input().split())
inputList = list(map(str, input().split()))
inputList.sort()

combStr = []
index = 0

solution(L, inputList, combStr, index)


# from itertools import combinations
# import sys
# input = sys.stdin.readline
#
# L, C = map(int,input().split())
# data = sorted(list(input().split()))
# comb = list(combinations(data,L))
#
# for c in comb:
#     cnt = 0
#     for i in range(L):
#         if c[i] in 'aeiou':
#             cnt +=1
#     if cnt >=1 and L-cnt >=2:
#         print(''.join(list(c)))
