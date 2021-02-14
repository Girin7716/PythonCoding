# 구슬 탈출2
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
board = []
red = (0,0)
blue = (0,0)
hole = (0,0)

for i in range(N):
    board.append(input())
    for j in range(M):
        if board[i][j] == 'R':
            red = (i,j)
        elif board[i][j] == 'B':
            blue = (i, j)
        elif board[i][j] == 'O':
            hole = (i, j)

q = set()
q.add((0,red,blue))

# 남,동,북,서
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def marble_move(red,blue,dx,dy):
    rx,ry = red
    bx,by = blue

    # move red marble
        # check red marble goal and return hole x,y
    while board[rx+dx][ry+dy] != '#':
        rx += dx
        ry += dy
        if board[rx][ry] == 'O':
            break
    # move blue marble
        # check blue marble goal
    while board[bx+dx][by+dy] != '#':
        bx += dx
        by += dy
        if board[bx][by] == 'O':
            break

    return (rx,ry), (bx,by)

def check_in_hole(red,blue):
    if board[red[0]][red[1]] == 'O' and board[blue[0]][blue[1]] == 'O':
        return 2
    elif board[red[0]][red[1]] == 'O':
        return 1
    elif board[blue[0]][blue[1]] == 'O':
        return 2
    return 0

def overlap_marble(red,blue,n_red,n_blue,dir):
    # dir -> 0:남, 1:동, 2:북, 3:서
    if n_red == n_blue:
        if dir == 0:
            if red[0] < blue[0]:    # 움직이기전 더 위쪽에 위치했었다.
                n_red = (n_red[0]-1,n_red[1])
            else:
                n_blue = (n_blue[0]-1,n_blue[1])
        elif dir == 1:
            if red[1] < blue[1]:
                n_red = (n_red[0],n_red[1]-1)
            else:
                n_blue = (n_blue[0],n_blue[1]-1)
        elif dir == 2:
            if red[0] > blue[0]:
                n_red = (n_red[0]+1,n_red[1])
            else:
                n_blue = (n_blue[0]+1,n_blue[1])
        else:
            if red[1] > blue[1]:
                n_red = (n_red[0],n_red[1]+1)
            else:
                n_blue = (n_blue[0],n_blue[1]+1)
    return n_red,n_blue

result = -1
min_value = int(1e9) + 1
while q:
    move_cnt,red,blue = q.pop()
    if move_cnt > 10:
        continue
    if min_value <= move_cnt:
        continue
    # 남,동,북,서
    # 4방향으로 기울여보기
    for i in range(4):
        # move
        n_red,n_blue = marble_move(red,blue,dx[i],dy[i])

        # check in hole
        temp = check_in_hole(n_red, n_blue)
        if temp  == 1:  # success
            result = move_cnt+1
            min_value = min(min_value,result)
        elif temp == 2:
            continue
        # overlap marble?
        n_red,n_blue = overlap_marble(red,blue,n_red,n_blue,i)
        # no move
        if red == n_red and blue == n_blue:
            continue
        q.add((move_cnt+1,n_red,n_blue))

if result > 10:
    print(-1)
else:
    print(result)


# import heapq
#
# N,M = map(int,input().split())
# board = []
# red = (0,0)
# blue = (0,0)
# hole = (0,0)
#
# for i in range(N):
#     board.append(input())
#     for j in range(M):
#         if board[i][j] == 'R':
#             red = (i,j)
#         elif board[i][j] == 'B':
#             blue = (i, j)
#         elif board[i][j] == 'O':
#             hole = (i, j)
#
# q = []
# heapq.heappush(q, (abs(red[0]-hole[0])+abs(red[1]-hole[1]),0, red, blue))   # red와 hole과의 거리, move, red, blue
#
# # 남,동,북,서
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
#
# def marble_move(red,blue,dx,dy):
#     rx,ry = red
#     bx,by = blue
#
#     # move red marble
#         # check red marble goal and return hole x,y
#     while board[rx+dx][ry+dy] != '#':
#         rx += dx
#         ry += dy
#         if board[rx][ry] == 'O':
#             break
#     # move blue marble
#         # check blue marble goal
#     while board[bx+dx][by+dy] != '#':
#         bx += dx
#         by += dy
#         if board[bx][by] == 'O':
#             break
#
#     return (rx,ry), (bx,by)
#
# def check_in_hole(red,blue):
#     if board[red[0]][red[1]] == 'O' and board[blue[0]][blue[1]] == 'O':
#         return 2
#     elif board[red[0]][red[1]] == 'O':
#         return 1
#     return 0
#
# def overlap_marble(red,blue,n_red,n_blue,dir):
#     # dir -> 0:남, 1:동, 2:북, 3:서
#     if n_red == n_blue:
#         if dir == 0:
#             if red[0] < blue[0]:    # 움직이기전 더 위쪽에 위치했었다.
#                 n_red = (n_red[0]-1,n_red[1])
#             else:
#                 n_blue = (n_blue[0]-1,n_blue[1])
#         elif dir == 1:
#             if red[1] < blue[1]:
#                 n_red = (n_red[0],n_red[1]-1)
#             else:
#                 n_blue = (n_blue[0],n_blue[1]-1)
#         elif dir == 2:
#             if red[0] > blue[0]:
#                 n_red = (n_red[0]+1,n_red[1])
#             else:
#                 n_blue = (n_blue[0]+1,n_blue[1])
#         else:
#             if red[1] > blue[1]:
#                 n_red = (n_red[0],n_red[1]+1)
#             else:
#                 n_blue = (n_blue[0],n_blue[1]+1)
#
#     return n_red,n_blue
#
# result = -1
# cnt = 0
# while q:
#     cnt+=1
#     #red,blue,move_cnt = q.popleft()
#     dis,move_cnt,red,blue = heapq.heappop(q)
#     if move_cnt > 10:
#         continue
#
#     # 남,동,북,서
#     # 4방향으로 기울여보기
#     for i in range(4):
#         # move
#         n_red,n_blue = marble_move(red,blue,dx[i],dy[i])
#
#         # check in hole
#         temp = check_in_hole(n_red, n_blue)
#         if temp  == 1:  # success
#             result = move_cnt+1
#             break
#         elif temp == 2:
#             continue
#         # overlap marble?
#         n_red,n_blue = overlap_marble(red,blue,n_red,n_blue,i)
#         # no move
#         if red == n_red and blue == n_blue:
#             continue
#         q.append((abs(n_red[0]-hole[0])+abs(red[1]-hole[1]),move_cnt+1,n_red,n_blue))
#
#     if result != -1:
#         break
#
# print(result)


#
#
#
# import heapq
#
# N,M = map(int,input().split())
# board = []
# red = (0,0)
# blue = (0,0)
# hole = (0,0)
#
# for i in range(N):
#     board.append(input())
#     for j in range(M):
#         if board[i][j] == 'R':
#             red = (i,j)
#         elif board[i][j] == 'B':
#             blue = (i, j)
#         elif board[i][j] == 'O':
#             hole = (i, j)
#
# q = []
# heapq.heappush(q, (0, red, blue))
#
# # 남,동,북,서
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
#
# def marble_move(red,blue,dx,dy):
#     rx,ry = red
#     bx,by = blue
#
#     # move red marble
#         # check red marble goal and return hole x,y
#     while board[rx+dx][ry+dy] != '#':
#         rx += dx
#         ry += dy
#         if board[rx][ry] == 'O':
#             break
#     # move blue marble
#         # check blue marble goal
#     while board[bx+dx][by+dy] != '#':
#         bx += dx
#         by += dy
#         if board[bx][by] == 'O':
#             break
#
#     return (rx,ry), (bx,by)
#
# def check_in_hole(red,blue):
#     if board[red[0]][red[1]] == 'O' and board[blue[0]][blue[1]] == 'O':
#         return False
#     elif board[red[0]][red[1]] == 'O':
#         return True
#     return False
#
# def overlap_marble(red,blue,n_red,n_blue,dir):
#     # dir -> 0:남, 1:동, 2:북, 3:서
#     if n_red == n_blue:
#         if dir == 0:
#             if red[0] < blue[0]:    # 움직이기전 더 위쪽에 위치했었다.
#                 n_red = (n_red[0]-1,n_red[1])
#             else:
#                 n_blue = (n_blue[0]-1,n_blue[1])
#         elif dir == 1:
#             if red[1] < blue[1]:
#                 n_red = (n_red[0],n_red[1]-1)
#             else:
#                 n_blue = (n_blue[0],n_blue[1]-1)
#         elif dir == 2:
#             if red[0] > blue[0]:
#                 n_red = (n_red[0]+1,n_red[1])
#             else:
#                 n_blue = (n_blue[0]+1,n_blue[1])
#         else:
#             if red[1] > blue[1]:
#                 n_red = (n_red[0],n_red[1]+1)
#             else:
#                 n_blue = (n_blue[0],n_blue[1]+1)
#
#     return n_red,n_blue
#
# result = -1
# while q:
#     #red,blue,move_cnt = q.popleft()
#     move_cnt,red,blue = heapq.heappop(q)
#     # 남,동,북,서
#     # 4방향으로 기울여보기
#     for i in range(4):
#         # move
#         n_red,n_blue = marble_move(red,blue,dx[i],dy[i])
#
#         # check in hole
#         if check_in_hole(n_red, n_blue):  # success
#             result = move_cnt+1
#             break
#         # overlap marble?
#         n_red,n_blue = overlap_marble(red,blue,n_red,n_blue,i)
#         # no move
#         if red == n_red and blue == n_blue:
#             continue
#
#
#         q.append((move_cnt+1,n_red,n_blue))
#
#     if result != -1:
#         break
#
# print(result)
#
#
#
#
# # from collections import deque
# # import heapq
# #
# # N,M = map(int,input().split())
# # board = []
# # red = (0,0)
# # blue = (0,0)
# # hole = (0,0)
# #
# # for i in range(N):
# #     board.append(input())
# #     for j in range(M):
# #         if board[i][j] == 'R':
# #             red = (i,j)
# #         elif board[i][j] == 'B':
# #             blue = (i, j)
# #         elif board[i][j] == 'O':
# #             hole = (i, j)
# #
# # q = deque()
# # q.append((red,blue,0))    # (red_x,red_y),(blue_x,blue_y),move_cnt
# #
# # # 남,서,북,동
# # dx = [1,0,-1,0]
# # dy = [0,1,0,-1]
# #
# # def marble_move(red,blue,dx,dy):
# #     rx,ry = red
# #     bx,by = blue
# #
# #     # move red marble
# #         # check red marble goal and return hole x,y
# #     while board[rx][ry] != '#':
# #         rx += dx
# #         ry += dy
# #         if board[rx][ry] == 'O':
# #             break
# #     # move blue marble
# #         # check blue marble goal
# #     while board[bx][by] != '#':
# #         bx += dx
# #         by += dy
# #         if board[bx][by] == 'O':
# #             break
# #
# #     return (rx,ry), (bx,by)
# #
# # def check_in_hole(red,blue):
# #     if board[red[0]][red[1]] == 'O' and board[blue[0]][blue[1]] == 'O':
# #         return False
# #     elif board[red[0]][red[1]] == 'O':
# #         return True
# #     return False
# #
# # def overlap_marble(red,blue,n_red,n_blue,dir):
# #     # dir -> 0:남, 1:서, 2:북, 3:동
# #     if n_red == n_blue:
# #         if dir == 0:
# #             if red[0] < blue[0]:    # 움직이기전 더 위쪽에 위치했었다.
# #                 n_red = (n_red[0]-1,n_red[1])
# #             else:
# #                 n_blue = (n_blue[0]-1,n_blue)
# #         elif dir == 1:
# #             if red[1] > blue[1]:
# #                 n_red = (n_red[0],n_red[1]+1)
# #             else:
# #                 n_blue = (n_blue[0],n_blue[1]+1)
# #         elif dir == 2:
# #             if red[0] > blue[0]:
# #                 n_red = (n_red[0]+1,n_red[1])
# #             else:
# #                 n_blue = (n_blue[0]+1,n_blue[1])
# #         else:
# #             if red[1] < blue[1]:
# #                 n_red = (n_red[0],n_red[1]-1)
# #             else:
# #                 n_blue = (n_blue[0],n_blue[1]-1)
# #
# #     return n_red,n_blue
# #
# # result = -1
# # while q:
# #     red,blue,move_cnt = q.popleft()
# #     #print(red,blue,move_cnt)
# #
# #     # 4방향으로 기울여보기
# #     for i in range(4):
# #         # move
# #         n_red,n_blue = marble_move(red,blue,dx[i],dy[i])
# #
# #         # check in hole
# #         if check_in_hole(red, blue):  # success
# #             result = move_cnt+1
# #             break
# #         # overlap marble?
# #         n_red,n_blue = overlap_marble(red,blue,n_red,n_blue,i)
# #         q.append((n_red,n_blue,move_cnt+1))
# #
# #     if result != -1:
# #         break
# #
# # print(result)
