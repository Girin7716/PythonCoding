# Q9 / 문자열 압축
def solution(s):
    if len(s) == 1:
        return 1
    answer = 9999999999
    digit = 1

    # 자릿수 1 부터 s의 절반만큼만 검사
    while digit <= len(s)//2:
        cnt = 1
        result = []
        #0부터 digit만큼++해서 s 검사
        for i in range(0,len(s),digit):
            rem = []
            # 다음 숫자 검사
            for j in range(i,i+digit):
                try:
                    rem.append(s[j])
                except:
                    continue
            # 다음 숫자가 같은 숫자면 cnt++
            if ''.join(rem[0:digit]) == s[i+digit:i+2*digit]:
                cnt+=1
            # 다르면 cnt가 1이면 그냥 영어만 붙이고, cnt>1이면 cnt와 영어를 붙인다
            else:
                if cnt == 1:
                    result.append(''.join(rem))
                else:
                    result.append(str(cnt))
                    result.append(''.join(rem))
                cnt=1
        # digit에 대해서 검사가 끝난 result의 길이가 가장 짧은걸 answer에 저장
        if answer > len(''.join(result)):
            answer = len(''.join(result))
        digit+=1

    return answer

#solution('aabbaccc')
#solution('aaabaccc')
#print(solution('ababcdcdababcdcd'))
#print(solution('xababcdcdababcdcd'))
print(solution('a'))