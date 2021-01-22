# 전화번호 목록

# 통과
def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    length = len(phone_book)
    #print(phone_book[0]==phone_book[2][0:3])
    for i in range(length):
        #phone_book[i]
        l = len(phone_book[i])
        for j in range(i+1,length):
            if phone_book[i] == phone_book[j][0:l]:
                answer = False
                return answer
    return answer

# 정확성 : 100%, 효율성 0%
# def solution(phone_book):
#     answer = True
#     phone_book.sort(key=len)
#     length = len(phone_book)
#     #print(phone_book[0]==phone_book[2][0:3])
#     for i in range(length):
#         #phone_book[i]
#         l = len(phone_book[i])
#         for j in range(i+1,length):
#             if phone_book[i] == phone_book[j][0:l]:
#                 answer = False
#     return answer

# 정확도 : 50%, 효율성: 0%
# def solution(phone_book):
#     answer = True
#     phone_book.sort(key=len)
#     length = len(phone_book)
#
#
#     for i in range(length):
#         check=0
#         #print(phone_book[i])
#         for j in range(i+1,length):
#             #print(phone_book[j])
#             for k in range(len(phone_book[i])):
#                 if phone_book[i][k] == phone_book[j][k]:
#                     check+=1
#         if check == len(phone_book[i]):
#             answer = False
#             break
#
#     return answer

print(solution(['119', '97674223', '1195524421']))
print(solution(['123','456','789']))
print(solution(['12','123','1235','567','88']))

# [119, 97674223, 1195524421]	false
# [123,456,789]	true
# [12,123,1235,567,88]	false