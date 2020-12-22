# 뱀 / p327 / 구현 문제
from collections import deque

N = int(input())
board = [[1 for _ in range(N + 2)] for _ in range(N + 2)]  # 1 : board 안, 2 : 사과, 0 : board 밖
for i in range(N + 2):
    for j in range(N + 2):
        if i == 0 or i == N + 1 or j == 0 or j == N + 1:
            board[i][j] = 0

K = int(input())
for i in range(K):
    x, y = map(int, input().split())
    board[x][y] = 2
L = int(input())
go = deque()
for i in range(L):
    move, rotate = input().split()
    go.append([int(move), rotate])

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
d_index = 0
snake_length = 1
snake_location = [1, 1]  # row column
snake = deque()
snake.append([1,1])

def check_ok(snake):
    if board[snake[0][0]][snake[0][1]] == 0:    # game over
        return False
    # body?
    for i in range(1,len(snake)):
        if snake[0] == snake[i]:    # touch
            return False
    return True

def move_snake(snake,head,length):
    x,y = head[0],head[1]
    if board[x][y] == 2:    # apple
        snake.appendleft([x,y]) # head
        board[x][y] = 1
        length += 1
    else:   # no apple
        snake.appendleft([x,y])
        if check_ok(snake) == False:
            print(time)
            exit()
        snake.pop() # tail move

time = 1
while True:
    # move
    snake_location[0] += direction[d_index][0]
    snake_location[1] += direction[d_index][1]
    move_snake(snake,snake_location,snake_length)
    # time check
    try:
        if time == go[0][0]:  # rotate
            if go[0][1] == 'L':
                go.popleft()
                d_index -= 1
                if d_index < 0:
                    d_index = 3
            elif go[0][1] == 'D':
                go.popleft()
                d_index = (d_index + 1) % 4
    except:  # go[] end
        pass
    time += 1
# input
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

# 10
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 4
# 8 D
# 10 D
# 11 D
# 13 L

# 10
# 5
# 1 5
# 1 3
# 1 2
# 1 6
# 1 7
# 4
# 8 D
# 10 D
# 11 D
# 13 L