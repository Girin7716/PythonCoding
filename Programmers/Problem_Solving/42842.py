# 카펫
def solution(brown, yellow):
    answer = []
    row = 3 # 최소 세로 길이

    totalBlock = brown + yellow

    for col in range(3,(totalBlock//row)+1):
        row = totalBlock//col
        yellowCnt = (row-2) * (col-2)
        if yellowCnt == yellow:
            answer = [col,row]
        if col > row:
            continue

    return answer

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))