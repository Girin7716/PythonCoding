# 자물쇠와 열쇠 / Q10 / 구현 문제
# 책에서 푼 방법
# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a)  # 행 길이 계산
    m = len(a[0])   # 열 길이 계산
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1]= a[i][j]
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length,lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n*3) for _ in range(n*3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
        for x in range(n*2):
            for y in range(n*2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False

print(solution([[0,0,0],[1,0,0],[0,1,1]], [[1,1,1],[1,1,0],[1,0,1]]))

# 실패함
# def solution(key, lock):
#     answer = True
#     start_x,end_x,start_y,end_y = 21,0,21,0   # x 세로, y 가로
#     rem_locations = []
#     for i in range(len(lock)):
#         for j in range(len(lock[i])):
#             if lock[i][j] == 0:
#                 rem_locations.append([i,j])
#                 if start_x > i:
#                     start_x = i
#                 if start_y > j:
#                     start_y = j
#                 if end_x < i:
#                     end_x = i
#                 if end_y < j:
#                     end_y = j
#     for i in range(len(rem_locations)):
#         rem_locations[i][0] -= start_x
#         rem_locations[i][1] -= start_y
#     end_y -= start_y
#     end_x -= start_x
#     start_x,start_y = 0,0
#
#     lock_cp = [[1 for _ in range(end_y+1)] for _ in range(end_x+1)]
#     # 열쇠 압축 버전
#     for i in rem_locations:
#         lock_cp[i[0]][i[1]] = 0
#
#     print(lock_cp)
#     print(key)
#
#     # for _ in range(4):
#     #     for i in range(len(key)-end_x):
#     #         for j in range(len(key)-end_y):
#     #
#     #     key = rotate_90(key)
#     #print(lock_cp in test)
#
#     return answer
# def rotate_90(m):
#     N = len(m)
#     ret = [[0] * N for _ in range(N)]
#     # 왜 'ret = [[0] * N] * N'과 같이 하지 않는지 헷갈리시면 연락주세요.
#
#     for r in range(N):
#         for c in range(N):
#             ret[c][N-1-r] = m[r][c]
#     return ret
#
# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))