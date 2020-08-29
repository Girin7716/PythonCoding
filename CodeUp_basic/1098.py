h,w=input().split()
h=int(h)
w=int(w)

n=int(input())

stick = []
for i in range(n):
    rem=list(map(int,input().split()))
    stick.append(rem)

board = [[0 for x in range(w)] for _ in range(h)]

for i in range(n):
    for j in range(stick[i][0]):
        if stick[i][1] == 0:
            board[stick[i][2]-1][stick[i][3]+j-1] = 1
        else:
            board[stick[i][2] + j-1][stick[i][3]-1] = 1

for i in range(h):
    for j in range(w):
        print(board[i][j],end=" ")
    print()
