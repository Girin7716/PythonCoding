# 완주하지 못한 선수
def solution(participant, completion):
    answer = ''
    dic = {}
    for p in participant:
        try:
            dic[p] += 1
        except:
            dic[p] = dic.get(p, 1)

    for element in completion:
        dic[element]-=1

    for key, value in dic.items():
        if value == 1:
            answer = key
    return answer

#print(solution(['leo', 'kiki', 'eden'],['eden', 'kiki']))
#print(solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'],['josipa', 'filipa', 'marina', 'nikola']))
#print(solution(['mislav', 'stanko', 'mislav', 'ana'],['stanko', 'ana', 'mislav']))