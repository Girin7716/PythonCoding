# 자물쇠와 열쇠 / Q10 / 구현 문제
def solution(key, lock):
    answer = True
    start_x,end_x,start_y,end_y = 21,0,21,0   # x 세로, y 가로
    rem_locations = []
    for i in range(len(lock)):
        for j in range(len(lock[i])):
            if lock[i][j] == 0:
                rem_locations.append([i,j])
                if start_x > i:
                    start_x = i
                if start_y > j:
                    start_y = j
                if end_x < i:
                    end_x = i
                if end_y < j:
                    end_y = j
    for i in range(len(rem_locations)):
        rem_locations[i][0] -= start_x
        rem_locations[i][1] -= start_y
    end_y -= start_y
    end_x -= start_x
    start_x,start_y = 0,0

    lock_cp = [[1 for _ in range(end_y+1)] for _ in range(end_x+1)]
    # 열쇠 압축 버전
    for i in rem_locations:
        lock_cp[i[0]][i[1]] = 0
    #print(lock_cp)

    test = [[1,0],[0,1]]
    print(lock_cp in test)

    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))