# 구슬 탈출2
from collections import deque

N, M = map(int,input().split())
board = []
rx,ry,bx,by,hx,hy = 0,0,0,0,0,0

for i in range(N):
    board.append(list(input()))
    for j in range(M):
        if board[i][j] == 'R':
            rx=i
            ry=j
        elif board[i][j] == 'B':
            bx=i
            by=j
        elif board[i][j] == 'O':
            hx=i
            hy=j
q = deque()
q.append((rx,ry,bx,by,0))   # red_x,red_y,blue_x,blue_y, try

def up(rx,ry,bx,by,result):
    hole_check1 = 0
    hole_check2 = 0
    while True:
        check = 0   # 둘다 stop == 2
        if hole_check1 == 1:
            check+=1
        elif board[rx-1][ry] == '.':
            board[rx][ry] = '.'
            board[rx - 1][ry] = 'R'
            rx-=1
        elif board[rx-1][ry] == 'O':
            board[rx][ry] = '.'
            rx-=1
            hole_check1+=1
        else:
            check+=1
        if hole_check2 == 1:
            check+=1
        elif board[bx-1][by] == '.':
            board[bx][by] = '.'
            board[bx - 1][by] = 'B'
            bx-=1
        elif board[bx-1][by] == 'O':
            board[bx][by] = '.'
            bx-=1
            hole_check2+=1
        else:
            check+=1


        if check==2:
            q.append((rx,ry,bx,by,result+1))
            break
        elif hole_check1 == 0 and hole_check2 == 0:
            continue
        elif hole_check1 == 1 and hole_check2 !=1:
            q.append((rx,ry,bx,by,result+1))
            break

        else:
            break

    return

def right(rx,ry,bx,by,result):
    hole_check1 = 0
    hole_check2 = 0
    while True:
        check = 0  # 둘다 stop == 2
        if board[rx][ry+1] == '.':
            board[rx][ry] = '.'
            board[rx][ry+1] = 'R'
            ry += 1
        elif board[rx][ry+1] == 'O':
            board[rx][ry] = '.'
            ry+=1
            hole_check1+=1
            #q.append((rx, ry+1, bx, by, result + 1))
        else:
            check += 1
        if board[bx][by+1] == '.':
            board[bx][by] = '.'
            board[bx][by+1] = 'B'
            by += 1
        elif board[bx][by+1] == 'O':
            board[bx][by] = '.'
            by+=1
            hole_check2+=1
        else:
            check += 1
        if check == 2:
            q.append((rx, ry, bx, by, result + 1))
            break
        elif hole_check1 == 0 and hole_check2 == 0:
            continue
        elif hole_check1 == 1 and hole_check2 != 1:
            q.append((rx, ry, bx, by, result + 1))
            break
        else:
            break
    return
def down(rx,ry,bx,by,result):
    hole_check1 = 0
    hole_check2 = 0
    while True:
        check = 0  # 둘다 stop == 2
        if board[rx + 1][ry] == '.':
            board[rx][ry] = '.'
            board[rx + 1][ry] = 'R'
            rx += 1
        elif board[rx + 1][ry] == 'O':
            board[rx][ry] = '.'
            rx+=1
            hole_check1+=1
        else:
            check += 1
        if board[bx + 1][by] == '.':
            board[bx][by] = '.'
            board[bx + 1][by] = 'B'
            bx += 1
        elif board[bx + 1][by] == 'O':
            board[bx][by] = '.'
            bx+=1
            hole_check2+=1
        else:
            check += 1
        if check == 2:
            q.append((rx, ry, bx, by, result + 1))
            break
        elif hole_check1 == 0 and hole_check2 == 0:
            continue
        elif hole_check1 == 1 and hole_check2 != 1:
            q.append((rx, ry, bx, by, result + 1))
            break
        else:
            break
    return

def left(rx,ry,bx,by,result):
    hole_check1 = 0
    hole_check2 = 0
    while True:
        check = 0  # 둘다 stop == 2
        if board[rx][ry-1] == '.':
            board[rx][ry] = '.'
            board[rx][ry-1] = 'R'
            ry -= 1
        elif board[rx][ry-1] == 'O':
            board[rx][ry] = '.'
            ry-=1
            hole_check1+=1
            check+=1
        else:
            check += 1

        if board[bx][by-1] == '.':
            board[bx][by] = '.'
            board[bx][by-1] = 'B'
            by -= 1
        elif board[bx][by-1] == 'O':
            board[bx][by] = '.'
            by-=1
            hole_check2+=1
        else:
            check += 1

        if check == 2:
            q.append((rx, ry, bx, by, result + 1))
            break
        elif hole_check1 == 0 and hole_check2 == 0:
            continue
        elif hole_check1 == 1 and hole_check2 != 1 and check==2:
            q.append((rx, ry, bx, by, result + 1))
            break
        else:
            break
    return

while q:
    rx,ry,bx,by,result = q.popleft()
    if (rx,ry) == (hx,hy):
        break
    if result > 10:
        result = -1
        break
    # 위쪽
    up(rx, ry, bx, by,result)
    # 오른쪽
    right(rx,ry,bx,by,result)
    # 아래
    down(rx,ry,bx,by,result)
    # 왼쪽
    left(rx,ry,bx,by,result)

print(result)


# def up(rx,ry,bx,by,result):
#     while True:
#         check = 0   # 둘다 stop == 2
#         if board[rx-1][ry] == '.':
#             rx-=1
#         elif board[rx-1][ry] == 'O':
#             q.append((rx-1,ry,bx,by,result+1))
#             break
#         else:
#             check+=1
#         if board[bx-1][by] == '.':
#             bx-=1
#         elif board[bx-1][by] == 'O':
#             break
#         else:
#             check+=1
#
#         if check==2:
#             q.append((rx,ry,bx,by,result+1))
#             break
#     return
#
# def right(rx,ry,bx,by,result):
#     while True:
#         check = 0  # 둘다 stop == 2
#         if board[rx][ry+1] == '.':
#             ry += 1
#         elif board[rx][ry+1] == 'O':
#             q.append((rx, ry+1, bx, by, result + 1))
#             break
#         else:
#             check += 1
#         if board[bx][by+1] == '.':
#             by += 1
#         elif board[bx][by+1] == 'O':
#             break
#         else:
#             check += 1
#
#         if check == 2:
#             q.append((rx, ry, bx, by, result + 1))
#             break
#     return
# def down(rx,ry,bx,by,result):
#     while True:
#         check = 0  # 둘다 stop == 2
#         if board[rx + 1][ry] == '.':
#             rx += 1
#         elif board[rx + 1][ry] == 'O':
#             q.append((rx + 1, ry, bx, by, result + 1))
#             break
#         else:
#             check += 1
#         if board[bx + 1][by] == '.':
#             bx += 1
#         elif board[bx + 1][by] == 'O':
#             break
#         else:
#             check += 1
#
#         if check == 2:
#             q.append((rx, ry, bx, by, result + 1))
#             break
#     return
#
# def left(rx,ry,bx,by,result):
#     while True:
#         check = 0  # 둘다 stop == 2
#         if board[rx][ry-1] == '.':
#             ry -= 1
#         elif board[rx][ry-1] == 'O':
#             q.append((rx, ry-1, bx, by, result + 1))
#             break
#         else:
#             check += 1
#         if board[bx][by-1] == '.':
#             by -= 1
#         elif board[bx][by-1] == 'O':
#             break
#         else:
#             check += 1
#
#         if check == 2:
#             q.append((rx, ry, bx, by, result + 1))
#             break
#     return