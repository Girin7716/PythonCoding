# 감시 피하기 / p351 / DFS, BFS
from itertools import permutations

N = int(input())
board = []
teacher = []
wall = []

for i in range(N):
    board.append(list(input().split()))
    for j in range(N):
        if board[i][j] == 'T':
            teacher.append((i,j))
        if board[i][j] == 'X':
            wall.append((i,j))

def find_student(board,x,y):
    # up
    for i in range(x,-1,-1):
        if board[i][y] == 'S':
            return True
        if board[i][y] == 'O':
            break
    # right
    for i in range(y,N):
        if board[x][i] == 'S':
            return True
        if board[x][i] == 'O':
            break
    # down
    for i in range(x,N):
        if board[i][y] == 'S':
            return True
        if board[i][y] == 'O':
            break
    # left
    for i in range(y,-1,-1):
        if board[x][i] == 'S':
            return True
        if board[x][i] == 'O':
            break

def check_find(board):
    for x,y in teacher:
        if find_student(board,x,y) == True: # 학생 발각 == 실패
            return False
    return True

per = list(permutations(wall,3))
for i in range(len(per)):
    # 장애물 세우기
    for x in per[i]:
        board[x[0]][x[1]] = 'O'

    if check_find(board) == True:
        print('YES')
        exit()

    # 장애물 복구
    for x in per[i]:
        board[x[0]][x[1]] = 'X'
print('NO')

# 5
# X S X X T
# T X S X X
# X X X X X
# X T X X X
# X X T X X

# 4
# S S S T
# X X X X
# X X X X
# T T T X