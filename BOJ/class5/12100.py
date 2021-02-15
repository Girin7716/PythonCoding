# # 2048(easy)
# 2048(easy)
from collections import deque

N = int(input())
board = []
for i in range(N):
    board.append(list(map(int,input().split())))

def move_left(move):
    global now
    global q
    temp = []
    one = deque()
    for i in range(N):
        for j in range(N):
            if now[i][j] != 0:
                one.append(now[i][j])
        index = 0
        length = len(one)
        while index < length:
            if index == length - 1:
                temp.append(one[index])
                index+=1
            elif one[index] == one[index+1]:
                #two.append(one[index]*2)
                temp.append(one[index] * 2)
                index+=2
            else:
                temp.append(one[index])
                index += 1
        one.clear()
        for j in range((N*(i+1))-len(temp)):
            temp.append(0)

    cnt = 0
    rem = []
    for i in range(N):
        rem.append(temp[cnt:cnt + N])  # 한 줄 문자열(1차원 리스트) -> 2차원 리스트로 바꾸기
        cnt += N
    if rem != now:
        q.append((rem,move+1))
    return


def move_right(move):
    global now
    global q
    temp = []
    one = deque()
    for i in range(N):
        for j in range(N-1,-1,-1):
            if now[i][j] != 0:
                one.append(now[i][j])
        index = 0
        length = len(one)
        while index < length:
            if index == length - 1:
                temp.append(one[index])
                index += 1
            elif one[index] == one[index + 1]:
                temp.append(one[index] * 2)
                index += 2
            else:
                temp.append(one[index])
                index += 1

        one.clear()
        for j in range((N * (i + 1)) - len(temp)):
            temp.append(0)

    cnt = 0
    rem = []
    for i in range(N):
        rem.append(list(reversed(temp[cnt:cnt + N])))  # 한 줄 문자열(1차원 리스트) -> 2차원 리스트로 바꾸기
        cnt += N
    if rem != now:
        q.append((rem, move + 1))
    return

def move_up(move):
    global now
    global q
    temp = []
    one = deque()
    for i in range(N):
        for j in range(N):
            if now[j][i] != 0:
                one.append(now[j][i])
        index = 0
        length = len(one)
        while index < length:
            if index == length - 1:
                temp.append(one[index])
                index += 1
            elif one[index] == one[index + 1]:
                # two.append(one[index]*2)
                temp.append(one[index] * 2)
                index += 2
            else:
                temp.append(one[index])
                index+=1
        one.clear()
        for j in range((N * (i + 1)) - len(temp)):
            temp.append(0)

    cnt = 0
    rem1 = []
    rem2 = []

    for i in range(N):
        for j in range(i, N * N, N):
            rem1.append(temp[j])

    for i in range(N):
        rem2.append(rem1[cnt:cnt + N])  # 한 줄 문자열(1차원 리스트) -> 2차원 리스트로 바꾸기
        cnt += N
    #[2,4,8,2,4,8,2,4,8,]

    if rem2 != now:
        q.append((rem2, move + 1))
    return


def move_down(move):
    global now
    global q
    temp = []
    one = deque()
    for i in range(N):
        for j in range(N-1,-1,-1):
            if now[j][i] != 0:
                one.append(now[j][i])
        index = 0
        length = len(one)
        while index < length:
            if index == length - 1:
                temp.append(one[index])
                index += 1
            elif one[index] == one[index + 1]:
                # two.append(one[index]*2)
                temp.append(one[index] * 2)
                index += 2
            else:
                temp.append(one[index])
                index += 1
        one.clear()
        for j in range((N * (i + 1)) - len(temp)):
            temp.append(0)

    cnt = 0
    rem1 = []
    rem2 = []

    for i in range(N):
        for j in range(i, N * N, N):
            rem1.append(temp[j])

    for i in range(N):
        rem2.append(rem1[cnt:cnt + N])  # 한 줄 문자열(1차원 리스트) -> 2차원 리스트로 바꾸기
        cnt += N
    # [2,4,8,2,4,8,2,4,8,]
    rem2.reverse()

    if rem2 != now:
        q.append((rem2, move + 1))
    return

q = deque()
q.append((board,0)) # board, move
result = -1
while q:
    now, move = q.popleft()
    if move>5:
        continue

    for i in range(N):
        for j in range(N):
            result = max(result,now[i][j])

    move_left(move)
    move_right(move)
    move_up(move)
    move_down(move)

print(result)

# from collections import deque
# import copy
#
# N = int(input())
# board = []
# for i in range(N):
#     board.append(list(map(int,input().split())))
#
# q = deque()
# q.append((board,0))
#
# def move_left():
#     global now
#     temp = copy.deepcopy(now)
#     for i in range(N):
#         for j in range(N-1):
#             if temp[i][j] == 0:
#                 temp[i][j] = temp[i][j+1]
#                 temp[i][j+1] = 0
#             elif temp[i][j] == temp[i][j+1]:
#                 temp[i][j] *= 2
#                 temp[i][j+1] = 0
#     return temp
#
# def move_right():
#     global now
#     temp = copy.deepcopy(now)
#
#     for i in range(N):
#         for j in range(N-1,0,-1):
#             if temp[i][j] == 0:
#                 temp[i][j] = temp[i][j-1]
#                 temp[i][j-1] = 0
#             elif temp[i][j] == temp[i][j-1]:
#                 temp[i][j] *= 2
#                 temp[i][j-1] = 0
#
#     return temp
#
# def move_up():
#     global now
#     temp = copy.deepcopy(now)
#     for i in range(N):
#         for j in range(N-1):
#             if temp[j][i] == 0:
#                 temp[j][i] = temp[j+1][i]
#                 temp[j+1][i] = 0
#             elif temp[j][i] == temp[j+1][i]:
#                 temp[j][i] *= 2
#                 temp[j+1][i] = 0
#     return temp
#
# def move_down():
#     global now
#     temp = copy.deepcopy(now)
#     for i in range(N):
#         for j in range(N - 1,0,-1):
#             if temp[j][i] == 0:
#                 temp[j][i] = temp[j - 1][i]
#                 temp[j - 1][i] = 0
#             elif temp[j][i] == temp[j - 1][i]:
#                 temp[j][i] *= 2
#                 temp[j - 1][i] = 0
#     return temp
#
# result = -1
# while q:
#     now,move = q.popleft()
#
#     # for i in range(N):
#     #     for j in range(N):
#     #         print(now[i][j],end=' ')
#     #     print()
#     # print('------------')
#     if move > 5:
#         continue
#
    # for i in range(N):
    #     for j in range(N):
    #         result = max(result,now[i][j])
#
#     #left
#     temp = move_left()
#     if now != temp:
#         q.append((temp,move+1))
#     #right
#     temp = move_right()
#     if now != move_right():
#         q.append((temp,move+1))
#     #up
#     temp = move_up()
#     if now != move_up():
#         q.append((temp,move+1))
#     #down
#     temp = move_down()
#     if now != move_down():
#         q.append((temp,move+1))
#
# print(result)