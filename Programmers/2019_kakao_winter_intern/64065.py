# 튜플
def solution(s):
    answer = []
    s = s.replace('},{','/')
    s = s.replace('{','')
    s = s.replace('}','')
    s = s.split('/')
    s.sort(key= lambda x : len(x))

    rem = set()
    for number in s:
        for n in number.split(','):
            if n not in rem:
                rem.add(n)
                answer.append(int(n))
                break

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))

















# def solution(s):
#     answer = []
#
#     s = s.replace("{","")
#     s = s.replace("},", "#")
#     s = s.replace("}","")
#     s=s.split("#")
#
#     replace_s=[]
#     for i in range(len(s)):
#         replace_s.append(list(map(int,s[i].split(','))))
#
#     replace_s.sort(key=len) #2/2,1/2,1,3/2,1,3,4/
#
#     rem = set()
#     temp = []
#     for i in range(len(replace_s)):
#         temp.append(set(replace_s[i]).difference(rem))
#         rem = rem | set(replace_s[i])
#
#     hi = []
#     for i in range(len(temp)):
#         hi.append(list(map(int,temp[i])))
#         answer.append(hi[i].pop())
#     print(answer)
#
#     return answer