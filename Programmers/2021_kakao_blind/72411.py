# 메뉴 리뉴얼
# 단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 합니다.
# 또한, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함하기로 했습니다.
from itertools import combinations

def solution(orders, course):
    answer = []
    orders.sort(key=lambda x: len(x))  # 길이순으로 정렬해줌.)

    for c in course:
        comb = {}
        for order in orders:
            order = ''.join(list(sorted(list(order))))
            rems = list(combinations(order,c))
            for rem in rems:
                comb[rem] = comb.get(rem,0) + 1

        # print(comb)
        if comb == {}:
            continue
        else:
            max_value = max(comb.values())
            if max_value == 1:
                continue
            else:
                for cb in comb:
                    if comb[cb] == max_value:
                        answer.append(''.join(cb))

    answer.sort()
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))