# 괄호 변환 / p347 / BFS, DFS&BFS

def check_correct(u):
    left = 0
    right = 0
    for i in range(len(u)):
        if left - right < 0:
            return False
        if u[i] == '(':
            left += 1
        else:
            right += 1
    return True

def solution(p):
    answer = ''
    # 1
    if p == '':
        return answer
    # 2 w -> u + v
    # 균형 잡힌 문자열 = (와 )의 개수가 일치
    # 올바른 괄호 문자열 = (와 )의 짝이 일치
    left = 0
    right = 0
    u = []
    v = []
    for i in range(len(p)):
        if left != right or (left == 0 and right == 0):
            if p[i] == '(':
                u.append('(')
                left += 1
            elif p[i] == ')':
                u.append(')')
                right += 1
        else:
            v.append(p[i])
    if u == []:
        return
    # 3
    # 3-1
    if check_correct(u) == True:    # u가 올바른 괄호 문자열
        answer = ''.join(u) + ''.join(solution(''.join(v)))
    # 3-2
    else:   # u가 올바른 괄호 문자열이 아님
        answer += '('
        answer += ''.join(solution(''.join(v)))   # 4-2
        answer += ')'
        u.pop()
        u = u[1:]
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)

    return answer

#print(solution("(()())()"))
#print(solution(")("))
#print(solution("()))((()"))
#print(solution(""))
