# 낚시왕
from collections import deque
import sys
input = sys.stdin.readline

R,C,M = map(int,input().split())
shark = {}
board = [[0 for _ in range(C+1)] for _ in range(R+1)]
for i in range(M):
    r,c,s,d,z = map(int,input().split())
    shark[z] = [r,c,s,d,False]    # z: 크기, (r,c) : 좌표, s : 속력, d : 이동방향, T/F 포획?
    board[r][c] = z

def print_board():
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j],end=' ')
        print()
    print('----------------')

# 1. 낚시왕이 오른쪽으로 한 칸 이동한다.
# 2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
# 3. 상어가 이동한다.

def get_shark(fisherman):
    result = 0
    for i in range(1,R+1):
        if board[i][fisherman] != 0:
            result += board[i][fisherman]
            #shark[board[i][fisherman]][4] = True # 포획
            del(shark[board[i][fisherman]])
            board[i][fisherman] = 0

            break
    return result

# d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4(0)인 경우는 왼쪽을 의미
dx = [0,-1,1,0]
dy = [-1,0,0,1]
# z: 크기, (r,c) : 좌표, s : 속력, d : 이동방향, T/F 포획?
def move_shark():
    q = deque()
    for s in shark:
        board[shark[s][0]][shark[s][1]] = 0

        if shark[s][3] == 1 or shark[s][3] == 2:
            shark[s][2] = shark[s][2]%(2*R-2)
        elif shark[s][3] == 3 or shark[s][3] == 0:
            shark[s][2] = shark[s][2]%(2*C-2)

        for i in range(shark[s][2]):
            shark[s][0] += dx[shark[s][3] % 4]
            shark[s][1] += dy[shark[s][3] % 4]
            if shark[s][0] > R:
                shark[s][3] = 1
                shark[s][0] = R-1
            elif shark[s][0] < 1:
                shark[s][3] = 2
                shark[s][0] = 2
            elif shark[s][1] > C:
                shark[s][3] = 4
                shark[s][1] = C-1
            elif shark[s][1] < 1:
                shark[s][3] = 3
                shark[s][1] = 2

        q.append((shark[s][0],shark[s][1],s))

    for r,c,z in q:
        if board[r][c] == 0:
            board[r][c] = z
        elif board[r][c] > z:
            del(shark[z])
            continue
        elif board[r][c] < z:
            #shark[board[r][c]][4] = True
            del(shark[board[r][c]])
            board[r][c] = z

    return

result = 0
for fisherman in range(1,C+1):
    result += get_shark(fisherman)
    move_shark()
#    print_board()
#    print(shark)

print(result)





# # 10%에서 틀렸습니다????
# from collections import deque
# import sys
# input = sys.stdin.readline
#
# R,C,M = map(int,input().split())
# board = [[-1 for _ in range(C+1)] for _ in range(R+1)]
# shark = []
# shark_dic = {}
# for i in range(M):
#     shark.append(list(map(int,input().split())) + [True])
#     shark_dic[shark[i][4]] = shark[i][0:4]+shark[i][5:]
#     board[shark[i][0]][shark[i][1]] = shark[i][4]
#
# dx = [0,-1,1,0]
# dy = [-1,0,0,1]
#
# def move_shark():
#     q = deque()
#     global R,C
#     for s in shark_dic:
#         if shark_dic[s][4] is False:
#             continue
#         board[shark_dic[s][0]][shark_dic[s][1]] = -1
#         if shark_dic[s][3] == 0 or shark_dic[s][3] == 1:
#             shark_dic[s][2] = shark_dic[s][2] % (2*R-2)
#         elif shark_dic[s][3] == 2 or shark_dic[s][3] == 3:
#             shark_dic[s][2] = shark_dic[s][2] % (2 * C - 2)
#
        # for i in range(shark_dic[s][2]):
        #     shark_dic[s][0] += dx[shark_dic[s][3] % 4]
        #     shark_dic[s][1] += dy[shark_dic[s][3] % 4]
        #     if shark_dic[s][0] > R:
        #         shark_dic[s][3] = 1
        #         shark_dic[s][0] = R-1
        #     elif shark_dic[s][0] < 1:
        #         shark_dic[s][3] = 2
        #         shark_dic[s][0] = 2
        #     elif shark_dic[s][1] > C:
        #         shark_dic[s][3] = 4
        #         shark_dic[s][1] = C-1
        #     elif shark_dic[s][1] < 1:
        #         shark_dic[s][3] = 3
        #         shark_dic[s][1] = 2
#
#         q.append((shark_dic[s][0], shark_dic[s][1], s))
#
#     for r,c,s in q:
#         if board[r][c] == -1:
#             board[r][c] = s
#         elif board[r][c] > s:
#             shark_dic[s][4] = False
#         elif board[r][c] < s:
#             shark_dic[board[r][c]][4] = False
#             board[r][c] = s
#
# result = 0
# for fisherman in range(1,C+1):
#     for i in range(1,R+1):
#         if board[i][fisherman] != -1:
#             shark_dic[board[i][fisherman]][4] = False
#             result += board[i][fisherman]
#             board[i][fisherman] = -1
#             break
#     # 상어 이동
#     move_shark()
#
# print(result)
#
# # 4 4 4
# # 1 1 1 2 10
# # 2 1 0 1 1
# # 3 1 1 2 10
# # 4 1 0 1 1
#
#
# # 100 7 7
# # 3 2 2 3 9
# # 3 3 1 3 3
# # 3 5 1 4 7
# # 3 6 2 4 6
# # 2 4 1 2 8
# # 1 4 2 2 4
# # 4 4 1 1 5
#
# # 3 3 9
# # 1 1 1000 1 1
# # 1 2 999 2 2
# # 2 1 1000 3 3
# # 2 2 999 4 4
# # 1 3 1000 1 5
# # 3 1 999 2 6
# # 2 3 1000 3 7
# # 3 2 999 4 8
# # 3 3 1000 1 9
#
# # 10 10 2
# # 1 9 8 2 1
# # 5 10 7 4 2
#
# # 2 5 1
# # 1 5 1 3 1