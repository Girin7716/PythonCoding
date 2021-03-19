# [카카오 인턴] 보석 쇼핑
import copy
def solution(gems):
    answer = []
    diction = {}
    for a in set(gems):
        diction[a] = 0
    length = len(diction)
    length_g = len(gems)
    start,end = 0,0

    cnt = 0
    while start<=end or end < length_g:
        if diction[gems[start]] == 0:
            cnt += 1
            diction[gems[start]] += 1
        else:
            cnt -= 1

        if diction[gems[end]] == 0:
            cnt += 1

        if cnt < length:
            end += 1
        elif cnt == length:
            answer = [start,end]
            start += 1



    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))