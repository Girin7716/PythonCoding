# 수식 최대화 8:44 ~
from itertools import permutations
import copy

def solution(expression):
    answer = 0
    expression_list = []
    rem = ''

    init(expression_list, expression, rem)

    prior = permutations(['+','-','*'],3)
    #print(list(prior))

    for p in prior:
        ex_list = copy.deepcopy(expression_list)
        for i in range(3):
            idx = -1
            while True:
                idx += 1
                if ex_list[idx] == 'end':
                    break
                if ex_list[idx] == p[i]:
                    ex_list = ex_list[:idx-1]+[str(eval(''.join((ex_list[idx-1:idx+2]))))]+ex_list[idx+2:]
                    idx-=1
        answer = max(answer,abs(int(ex_list[0])))


    return answer


def init(ex_list, expression, rem):
    index = -1
    for i in range(len(expression)):
        if expression[i] == '-' or expression[i] == '+' or expression[i] == '*':
            index += 2
            ex_list.append(rem)
            ex_list.append(expression[i])
            rem = ''
        else:
            rem += expression[i]
    ex_list.append(rem)
    ex_list.append('end')
    # print(ex_list)


#result : 60420
print(solution("100-200*300-500+20"))
#result : 300
print(solution("50*6-3*2"))
