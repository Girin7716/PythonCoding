# 가사 검색 / p 370 / 이진 탐색
from bisect import bisect_left,bisect_right

def count_by_range(a,left_value,right_value):
    return bisect_left(a,right_value)-bisect_left(a,left_value)

def solution(words,queries):
    answer = []
    new_words = [[] for _ in range(10001)]
    reverse_words = [[] for _ in range(10001)]

    for word in words:
        new_words[len(word)].append(word)
        reverse_words[len(word)].append(word[::-1])

    for i in range(10001):
        new_words[i].sort()
        reverse_words[i].sort()

    for q in queries:
        if q == '?':
            result = count_by_range(reverse_words[len(q)],q[::-1].replace('?','a'),q[::-1].replace('?','z'))
        else:
            result = count_by_range(new_words[len(q)],q.replace('?','a'),q.replace('?','z'))
        answer.append(result)

    return answer


# from bisect import bisect_right,bisect_left
#
# def count_by_range(a,left_value,right_value):
#     return bisect_right(a,right_value)-bisect_left(a,left_value)
#
# def solution(words, queries):
#     answer = []
#     new_words = [[] for _ in range(10001)]
#     reversd_words = [[] for _ in range(10001)]
#     for word in words:
#         new_words[len(word)].append(word)
#         reversd_words[len(word)].append(word[::-1])
#
#     for i in range(10001):
#         new_words[i].sort()
#         reversd_words[i].sort()
#
#     for q in queries:
#         if q[0] == '?':
#             result = count_by_range(reversd_words[len(q)],q[::-1].replace('?','a'),q[::-1].replace('?','z'))
#         else:
#             result = count_by_range(new_words[len(q)],q.replace('?','a'),q.replace('?','z'))
#
#         answer.append(result)
#     return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))