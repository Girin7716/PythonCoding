board = [[int(x) for x in input().split()] for y in range(10)]

# 시작 좌표 1,1
stack = []
x = 1
y = 1
while x!=8 or y!=8:
    if board[x][y] == 2:
        break

    if board[x][y+1] == 0 or board[x][y+1] == 2:
        board[x][y]=9
        y+=1
    elif board[x][y+1] == 1:
        board[x][y]=9
        x+=1

board[x][y] = 9
for i in range(10):
    for j in range(10):
        print(board[i][j],end=" ")
    print()

