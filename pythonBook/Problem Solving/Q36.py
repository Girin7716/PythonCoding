# 편집 거리 / p382 / DP
A = input()
B = input()

board = [[i for i in range(len(A)+1)]]
for i in range(len(B)):
    board.append([(i+1) for _ in range(len(A)+1)])

# A => sunday
# B => saturday

def check_num(i,j):
    if A[j-1] == B[i-1]:
        board[i][j] = board[i-1][j-1]
    else:
        # # check left, up, left_up and +1
        # if min > board[i][j-1]:
        #     min = board[i][j-1]
        # if min > board[i-1][j-1]:
        #     min = board[i-1][j-1]
        # if min > board[i-1][j]:
        #     min = board[i-1][j]
        # board[i][j] = min+1
        board[i][j] = min(board[i][j-1],board[i-1][j-1],board[i-1][j])+1


for i in range(1,len(B)+1):
    for j in range(1,len(A)+1):
        check_num(i,j)

print(board[len(B)][len(A)])
