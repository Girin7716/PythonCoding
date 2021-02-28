# 블록 이동하기 / p355 / DFS&BFS, BFS
# 실패
from collections import deque

def check_right_rotate(x1,y1,x2,y2,move_cnt,queue):
    # down
    nx1,ny1,nx2,ny2 = x1+1,y1+1,
    # up
    return True

def check_left_rotate(x1,y1,x2,y2,move_cnt,queue):
    # down
    # up
    return True

def solution(board):
    answer = 0
    N = len(board)
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    queue = deque()
    queue.append([0,0,0,1,0])   ## x1,y1,x2,y2,move_cnt
    while queue:
        x1,y1,x2,y2,move_cnt = queue.popleft()
        if 0 <= x1 < N and 0 <= y1 < N and 0 <= x2 < N and 0 <= y2 < N and (x1,y1 == N-1,N-1 or x2,y2 == N-1,N-1):
            answer = move_cnt
            return answer
        for i in range(4):  # 4방향 check
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]
            if 0<=nx1<N and 0<=ny1<N and 0<=nx2<N and 0<=ny2<N and board[nx1][ny1] != 1 and board[nx2][ny2] != 1:
                queue.append([nx1,ny1,nx2,ny2,move_cnt+1])
        # 반시계 방향 회전 check
        check_right_rotate(x1,y1,x2,y2,move_cnt,queue)
        # 시계 방향 회전 check
        check_left_rotate(x1,y1,x2,y2,move_cnt,queue)


    return answer


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))