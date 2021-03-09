# 뉴스 클러스터링
def solution(str1, str2):
    answer = 0
    rem1 = []
    rem2 = []

    for i in range(1, len(str1)):
        if not (str1[i - 1].isalpha() and str1[i].isalpha()):
            continue
        rem1.append((str1[i - 1] + str1[i]).lower())
    for i in range(1, len(str2)):
        if not (str2[i - 1].isalpha() and str2[i].isalpha()):
            continue
        rem2.append((str2[i - 1] + str2[i]).lower())

    if len(rem1) > len(rem2):
        # 교집합의 개수를 구함
        inter = [rem1.remove(x) for x in rem2 if x in rem1]
    else:
        inter = [rem2.remove(x) for x in rem1 if x in rem2]

        # 합집합은 교집합 + 나머지 원소들

    list_uni = rem1 + rem2
    uni = len(list_uni)

    if uni == 0:
        return 65536
    else:
        answer = int(len(inter) / uni * 65536)
        return answer



# print(solution("FRANCE", "french"))
# print(solution("handshake", "shake hands"))
# print(solution("shake hands","handshake"))
# print(solution("aa1+aa2", "AAAA12"))
# print(solution("E=M*C^2", "e=m*c^2"))
# print(solution("AAbbaa_AA","BBB"))
# print(solution("abddd","ddefghh"))
# print(solution("ab","ba_bd"))
# print(solution("CCDEFGHH","ABCCC"))
# print(abc("CCDEFGHH","ABCCC"))
#
# print(solution("AACCC","A A A A A C C C C"))
# print(abc("AACCC","A A A A A C C C C"))
#
# print(solution("ABDDD","DDEFGHH"))
# print(abc("ABDDD","DDEFGHH"))


print(solution("abccc","cccdefff"))
# ab/bc/cc/cc  //  cc/cc/cd/de/ef/ff/ff
# 합 : ab/bc/cc/cc/cd/de/ef/ff/ff
# 곱 : cc/cc
print(abc("abccc","cccdefff"))

# print(solution("abcd","efgh"))
# print(abc("abcd","efgh"))
# #
# print(solution("abddd","ddefghh"))
# print(abc("abddd","ddefghh"))