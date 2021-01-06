n = int(input())
location = []
for i in range(n):
    rem = input().split()
    rem = list(map(int,rem))
    location.append(rem)

board = [[0 for _ in range(19)] for x in range(19)]

for i in range(n):
    board[location[i][0]-1][location[i][1]-1]=1

for i in range(19):
    for j in range(19):
        print(board[i][j],end=" ")
    print()