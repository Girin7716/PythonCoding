# 게임 개발
# 어느 방법이 맞는지 모르겠음
## 책에서 푼 방법 ##
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐리거트이 X 좌표, Y 좌표, 방향 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)

## 내가 푼 방법 ##
# import copy
# N, M = map(int, input().split())
# A, B, d = map(int, input().split())
#
# board = []
# for i in range(N):
#     board.append(list(map(int, input().split())))
#
# direction = [(-1,0),(0,1),(1,0),(0,-1)] # 북0 동1 남2 서3 이동 좌표
# visited = copy.deepcopy(board) # 0은 안가본 칸, 1은 바다거나 가본 칸
#
# count = 1
# check = 0
# while True:
#     visited[A][B]=1
#     if visited[A+direction[d][0]][B+direction[d][1]] == 0:  # 방문한적이 없다
#         A=A+direction[d][0]
#         B=B+direction[d][1]
#         count+=1
#         check = 0
#     else:   # 방문했다 == 방향 회전
#         d += 3
#         d %= 4
#         check +=1
#
#     if check==4 and board[A+direction[(d+2)%4][0]][B+direction[(d+2)%4][1]]==1: # 사방이 1인데 뒤에는 바다
#         break
#     elif check == 4:
#         A=A+direction[(d+2)%4][0]
#         B=B+direction[(d+2)%4][1]
#         check=0
#
# print(count)
