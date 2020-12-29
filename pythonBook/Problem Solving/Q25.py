# 실패율 / p361 / 정렬
# # 책에서 푼 방법
# def solution(N, stages):
#     answer = []
#     length = len(stages)
#
#     # 스테이지 번호를 1부터 N까지 증가시키며
#     for i in range(1,N+1):
#         # 해당 스테이지에 머물러 있는 사람의 수 계산
#         count = stages.count(i)
#
#         # 실패율 계산
#         if length == 0:
#             fail = 0
#         else:
#             fail = count / length
#
#         # 리스트에 (스테이지 번호, 실패율) 원소 삽입
#         answer.append((i,fail))
#         length -= count
#
#     # 실패율을 기준으로 각 스테이지를 내림차순 정렬
#     answer = sorted(answer, key = lambda t:t[1],reverse=True)
#     answer = [i[0] for i in answer]
#     return answer
#print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
# 내가 푼 방법
from bisect import bisect_left, bisect_right

# 값이 [left_value,right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

def solution(N, stages):
    answer = []
    rem = []
    stages.sort()
    denominator = len(stages)   # 분모
    for i in range(1,N+1):
        if denominator == 0:
            rem.append([0,i])
            continue
        numerator = count_by_range(stages,i,i)  # 분자
        rem.append([numerator / denominator,i])
        denominator -= numerator

    rem.sort(reverse=True, key=lambda x : (x[0],-x[1]))
    for x in rem:
        answer.append(x[1])
    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))