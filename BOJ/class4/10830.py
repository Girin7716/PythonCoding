# 행렬 제곱
import sys
input = sys.stdin.readline
N,B = map(int,input().split())

matrix = []
temp = []
for i in range(N):
    matrix.append(list(map(int,input().split())))
    temp.append(matrix[i])

def ori_squared():
    result = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rem = 0
            for k in range(N):
                rem += matrix[i][k] * temp[k][j]
            result[i][j] = rem % 1000


    return result

def matrix_squared():
    global N
    result = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rem = 0
            for k in range(N):
                rem += matrix[i][k] * matrix[k][j]
            result[i][j] = rem % 1000

    return result

while B!=1:
    if B%2:
        matrix = ori_squared()
        B-=1
    else:
        matrix = matrix_squared()
        B//=2

for mat in matrix:
    print(*mat)

# cnt = 1
# while True:
#     if B==1:
#         for i in range(N):
#             for j in range(N):
#                 matrix[i][j] = matrix[i][j] % 1000
#     if cnt == B:
#         for mat in matrix:
#             print(*mat)
#         # for i in range(N):
#         #     for j in range(N):
#         #         print(matrix[i][j],end=' ')
#         #     print()
#         break
#     elif (cnt*2) < B and (cnt % 2 == 0):
#         matrix = matrix_squared()
#         cnt*=2
#     else:
#         matrix = ori_squared()
#         cnt += 1


# 3 3
# 1 2 3
# 4 5 6
# 7 8 9