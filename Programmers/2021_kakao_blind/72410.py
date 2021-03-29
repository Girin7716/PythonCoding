# 신규 아이디 추천
# 아이디의 길이는 3자 이상 15자 이하여야 합니다.
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
def solution(new_id):
    answer = ''

    #1단계
    new_id = new_id.lower()
    # print("1단계 : "+new_id)
    #2단계
    if checkEmpty(new_id) is False:
        temp = ''
        for s in new_id:
            if s.isalpha() or s.isnumeric() or s=='-'or s=='_' or s=='.':
                temp+=s
        new_id = temp
        # print("2단계 : "+new_id)
    #3단계
    # new_id=new_id.replace(new_id[0:3],'.')
    if checkEmpty(new_id) is False:
        start = 0
        end=0
        temp=''
        for i in range(len(new_id)):
            end=i
            if new_id[i] != '.':
                # new_id = new_id.replace(new_id[start:end],'.')
                if new_id[i-1] == '.':
                    temp+='.'
                temp += new_id[i]
        new_id = temp
        # print("3단계 : "+new_id)

    #4단계
    if checkEmpty(new_id) is False and new_id[0]=='.':
        new_id = new_id[1:]
    if checkEmpty(new_id) is False and new_id[-1]=='.':
        new_id = new_id[:len(new_id)-1]
    # print("4단계 : " +new_id)


    #5단계
    if checkEmpty(new_id):
        new_id += 'a'
    # print("5단계 : "+new_id)

    #6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] =='.':
            new_id = new_id[:len(new_id)-1]
    # print("6단계 : "+new_id)

    #7단계
    length = len(new_id)
    if length <= 2:
        while length < 3:
            length+=1
            new_id += new_id[-1]
    # print("7단계 : " + new_id)

    return new_id


def checkEmpty(id):
    if id=='':
        return True
    return False


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))