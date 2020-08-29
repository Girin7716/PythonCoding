# 문제> 나누어 떨어지는 숫자배열
# array의 각 element 중 divisor로 나누어 떨어지는 값을
# 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성하시오.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을
# 담아 반환하기

def solution(arr, divisor):
    result = [x for x in arr if x % divisor == 0]

    return sorted(result) or [-1]  # 빈 배열 = false
    # or 앞의 조건이 false라면 뒤의 조건을 반환해라


list = [1, 2, 3, 4, 5, 6]
#divisor = 7
divisor = 3

print(solution(list, divisor))
