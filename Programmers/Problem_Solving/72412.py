# 순위 검색
from bisect import bisect_left
from itertools import product,combinations

info_dict = {}

def solution(infos, query):
    answer = []

    rem = [['j','p','c','-'],['b','f','-'],['j','s','-'],['p','c','-']]
    for x in list(product(*rem)):
        info_dict[''.join(x)] = []
    for info in infos:
        rem = info.split()
        string = ''
        for i in range(5):
            if i == 4:
                for k in range(5):
                    for j in combinations(range(1,5),k):
                        temp = list(string)
                        for x in j:
                            temp[x-1] = '-'
                        info_dict[''.join(temp)].append(int(rem[i]))
            string+=rem[i][0]

    for key in info_dict.keys():
        info_dict[key].sort()

    for qry in query:
        temp = qry.split(' and ')
        temp = temp[:3] + temp[3].split()
        score = temp[4]
        string = ''
        for i in range(4):
            string+=temp[i][0]
        answer.append(len(info_dict[string])-bisect_left(info_dict[string],int(score)))

    return answer


# [1,1,1,1,2,4]
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
