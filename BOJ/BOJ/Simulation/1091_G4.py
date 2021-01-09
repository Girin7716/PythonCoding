
num = int(input())
idx = [int(input().split())]
init_state = [i for i in idx]



# # 카드 섞기
#
# N = int(input())
# P = list(map(int, input().split()))
# S = list(map(int, input().split()))
#
# card = list(x for x in range(N))
# temp = []
# Final = [[] for i in range(3)]
# Player = [[j for j in range(N) if j % 3 == i] for i in range(3)]
# First = [[j for j in range(N) if j % 3 == i] for i in range(3)]
#
# index = 0
# for i in P:
#     Final[i].append(card[index])
#     index += 1
#
# for i in range(3):
#     Final[i].sort()
#
# shuffle_cnt = 0
# while Final != Player:
#     index = 0
#     for i in range(3):
#         Player[i].clear()
#
#     for i in S:
#         Player[i % 3].append(card[index])
#         temp.append(card[S[i]])
#         index += 1
#
#     card = temp
#     shuffle_cnt += 1
#
#     for i in range(3):
#         Player[i].sort()
#
#     if First == Player:
#         shuffle_cnt = -1
#         break
#
# print(shuffle_cnt)
