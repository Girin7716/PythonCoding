# 늑대 사냥꾼
import heapq

N,M = map(int,input().split())
board = []
for i in range(N):
    board.append(list(input()))
    for j in range(M):
        if board[i][j] == '+':  # tree
            A,B = i,j
        if board[i][j] == 'V':
            R,C = i,j

def distance_tree(R,C,A,B): #현우 R행 C열 / 나무 A행 B 열
    return abs(R-A) + abs(C-B)

result = -1

q = []
#q.append((R,C))
dis = distance_tree(R,C,A,B)
heapq.heappush(q,(-dis,R,C))
dx = [1,0,-1,0]
dy = [0,1,0,-1]

while q:
    result+=1
    dis,R,C = heapq.heappop(q)
    if board[R][C] == 'J':
        break
    for i in range(4):
        nx = R + dx[i]
        ny = C + dy[i]
        if nx>= 0 and nx<N and ny >= 0 and ny<M:
            dis = distance_tree(nx,ny,A,B)
            heapq.heappush(q,(-dis,nx,ny))
print(result)