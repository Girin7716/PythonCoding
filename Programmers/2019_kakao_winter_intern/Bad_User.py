# 불량 사용자
#통과
from itertools import permutations

def solution(user_id, banned_id):
    rem = []
    for candidate_users in permutations(user_id, len(banned_id)):
        #print(candidate_users)
        check = True
        for i in range(len(banned_id)):
            c_len = len(candidate_users[i])
            b_len = len(banned_id[i])
            if c_len != b_len:
                check = False
                break
            for j in range(b_len):
                if banned_id[i][j] == '*' or banned_id[i][j] == candidate_users[i][j]:
                    continue
                else:
                    check = False
                    break
        if check == False:
            continue
        candidate_users = set(candidate_users)
        if candidate_users not in rem:
            rem.append(candidate_users)

    return len(rem)


# from itertools import product
#
#     def solution(user_id, banned_id):
#         digit = [[] for _ in range(9)]
#         rem = []
#         for u in user_id:
#             digit[len(u)].append(u)
#         for i in range(len(banned_id)):
#             rem.append([])
#             b_len = len(banned_id[i])
#             for d in digit[b_len]:
#                 cnt = 0
#                 for j in range(b_len):
#                     if banned_id[i][j] != '*' and banned_id[i][j] != d[j]:
#                         break
#                     cnt+=1
#                 if cnt == b_len:
#                     rem[i].append(d)
#
#         temp = []
#         for i in list(product(*rem)):
#             temp.append(tuple(sorted(i)))
#
#         temp = list(set(temp))
#         answer = len(temp)
#         for x in temp:
#             for j in range(len(i)-1):
#                 if x[j] == x[j+1]:
#                     answer-=1
#                     break
#         return answer

    # temp = list(set(temp))
    # answer = len(temp)
    # for x in temp:
    #     for j in range(len(i)-1):
    #         if x[j] == x[j+1]:
    #             answer-=1
    #             break
    # return answer





# test case 5 빼고 다 통과
# from itertools import product
#
# def solution(user_id, banned_id):
#     digit = [[] for _ in range(9)]
#     rem = []
#     for u in user_id:
#         digit[len(u)].append(u)
#     for i in range(len(banned_id)):
#         rem.append([])
#         b_len = len(banned_id[i])
#         for d in digit[b_len]:
#             cnt = 0
#             for j in range(b_len):
#                 if banned_id[i][j] != '*' and banned_id[i][j] != d[j]:
#                     break
#                 cnt+=1
#             if cnt == b_len:
#                 rem[i].append(d)
#
#     temp = []
#     for i in list(product(*rem)):
#         temp.append(tuple(sorted(i)))
#
#     temp = list(set(temp))
#     answer = len(temp)
#     for x in temp:
#         for j in range(len(i)-1):
#             if x[j] == x[j+1]:
#                 answer-=1
#                 break
#     return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))
#print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["******","*****","*****"]))