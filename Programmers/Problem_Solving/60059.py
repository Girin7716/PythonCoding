# 자물쇠와 열쇠

def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] += key[i][j]


def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] -= key[i][j]


def rotate90(arr):
    return list(zip(*arr[::-1]))


def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M + i][M + j] != 1:
                return False;
    return True


def solution(key, lock):
    M, N = len(key), len(lock)

    board = [[0] * (M * 2 + N) for _ in range(M * 2 + N)]
    # 자물쇠 중앙 배치
    for i in range(N):
        for j in range(N):
            board[M + i][M + j] = lock[i][j]

    rotated_key = key
    # 모든 방향 (4번 루프)
    for _ in range(4):
        rotated_key = rotate90(rotated_key)
        for x in range(1, M + N):
            for y in range(1, M + N):
                # 열쇠 넣어보기
                attach(x, y, M, rotated_key, board)
                # lock 가능 check
                if (check(board, M, N)):
                    return True
                # 열쇠 빼기
                detach(x, y, M, rotated_key, board)

    return False

# 풀다가 모르겠다 ㅈㅈ
# # 5,6,8,9,10,13,14,16,17,19,20,21,34,37,38
# # lock에서 0이 이루는 사각형의 좌표 찾기
# def findSquare(lock):
#     length = len(lock)
#
#     minX,minY,maxX,maxY = length,length,0,0
#
#     for i in range(length):
#         for j in range(length):
#             if lock[i][j] == 0:
#                 minX = min(minX,i)
#                 minY = min(minY,j)
#                 maxX = max(maxX,i)
#                 maxY = max(maxY,j)
#
#     return minX,minY,maxX,maxY
#
# #key를 시계방향으로 회전
# def rotateKey(key):
#     rem = []
#     length = len(key)
#     for i in range(length):
#         temp = []
#         for j in range(length):
#             temp.append(key[length-1-j][i])
#         rem.append(temp)
#
#     return rem
#
# def checkKey(key,eLock,minX,minY,maxX,maxY,length,startX,startY):
#
#     for i in range(minX,maxX+1):
#         for j in range(minY,maxY+1):
#             if eLock[length+i-1][length+j-1] + key[i-minX][j-minY] != 1:
#                 return False
#
#     return True
#
# def extendLock(lock):
#     extendSize = len(lock)*3
#     zeroColumn = [0] * (extendSize)
#     zeroColumn2 = [0] * (len(lock))
#     rem = []
#     cnt = 0
#     for i in range(extendSize):
#         if i >= extendSize//3 and i < (extendSize//3)*2:
#             temp = [0] * (len(lock))
#             for j in lock[cnt]:
#                 temp.append(j)
#             cnt+=1
#             for j in range(extendSize//3):
#                 temp.append(0)
#             rem.append(temp)
#         else:
#             rem.append(zeroColumn)
#
#     return rem
# def solution(key, lock):
#     answer = False
#     length = len(lock)
#
#     minX,minY,maxX,maxY = findSquare(lock)
#
#     eLock = extendLock(lock)
#     # print(eLock)
#     for i in range(4):  # 회전 4방향
#         for j in range((maxX-minX)*(maxY-minY)):
#             answer = checkKey(key,eLock,minX,minY,maxX,maxY,length)
#             if answer is True:
#                 break
#         if answer is True:
#             break
#         key = rotateKey(key)
#
#     return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
               [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
