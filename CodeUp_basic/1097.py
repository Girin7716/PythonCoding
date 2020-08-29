board = []
for i in range(19):
    rem = input().split()
    rem = list(map(int, rem))
    board.append(rem)
n = int(input())
location = []
for i in range(n):
    rem = input().split()
    rem = list(map(int, rem))
    location.append(rem)

for x in range(n):
    for i in range(19):
        if board[location[x][0]-1][i] == 0:
            board[location[x][0]-1][i] = 1
        else:
            board[location[x][0]-1][i] = 0
        if board[i][location[x][1]-1] == 0:
            board[i][location[x][1]-1] = 1
        else:
            board[i][location[x][1]-1] = 0

for i in range(19):
    for j in range(19):
        print(board[i][j],end=" ")
    print()

