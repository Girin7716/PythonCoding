# 호텔 방 배정
import sys
sys.setrecursionlimit(10**8)

def find_parent(parent,x):
    if x not in parent:
        parent[x] = x+1
        return x
    parent[x] = find_parent(parent,parent[x])
    return parent[x]

def solution(k, room_number):
    answer = []
    parent = {}

    for r in room_number:
        answer.append(find_parent(parent,r))
    return answer

print(solution(10,[1,3,4,1,3,1]))



# naive(정확도o, 효율성x)
# def solution(k, room_number):
#     answer = []
#     data = [0 for i in range(k+1)]
#
#
#     for r in room_number:
#         if data[r] == 0:
#             data[r] = r
#             answer.append(r)
#         else:
#             rem = r
#             while True:
#                 rem += 1
#                 if data[rem] == 0:
#                     data[rem] = rem
#                     answer.append(rem)
#                     #answer[rem] = rem
#                     break
#     return answer