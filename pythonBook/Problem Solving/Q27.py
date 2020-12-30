# 정렬된 배열에서 특정 수의 개수 구하기 / p367 / 이진 탐색
# O(log N)에 통과해야함.
# 내가 푼 방법
from bisect import bisect_left, bisect_right

N,x = map(int,input().split())
data = list(map(int,input().split()))

def bisect_count(data,left_value,right_value):
    answer = bisect_right(data,x) - bisect_left(data,x)
    if answer == 0:
        return -1
    return answer

print(bisect_count(data,x,x))

# # 이진 탐색 직접 구현 코드
# n,x = map(int,input().split())
# array = list(map(int,input().split()))
#
# def count_by_value(array,x):
#     # 데이터의 개수
#     n = len(array)
#
#     # x가 처음 등장한 인덱스 계산
#     a = first(array,x,0,n-1)
#
#     # 수열에 x가 존재하지 않는 경우
#     if a == None:
#         return 0
#
#     # x가 마지막으로 등장한 인덱스 계산
#     b = last(array,x,0,n-1)
#
#     # 개수를 반환
#     return b - a + 1
#
# # 처음 위치를 찾는 이진 탐색 메서드
# def first(array,target,start,end):
#     if start > end:
#         return None
#     mid = (start + end)//2
#     # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
#     if (mid == 0 or target > array[mid-1]) and array[mid] == target:
#         return mid
#     # 중간값의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 화깅ㄴ
#     elif array[mid] >= target:
#         return first(array,target,start,mid-1)
#     # 중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 확인
#     else:
#         return first(array,target,mid+1,end)
#
# def last(array,target,start,end):
#     if start>end:
#         return None
#     mid = (start + end) // 2
#     # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
#     if (mid==n-1 or target<array[mid+1]) and array[mid] == target:
#         return mid
#     # 중간점의 값 보다 찾고자 하는 값이 작은 경우 왼쪽 확인
#     elif array[mid] > target:
#         return last(array,target,start,mid-1)
#     # 중간점의 값 보다 찾고자 하는 값이 크거나 같은 경우 오른쪽 확인
#     else:
#         return last(array,target,mid+1,end)
#
#
# # 값이 x인 데이터의 개수 계산
# count = count_by_value(array,x)
#
# # 값이 x인 원소가 존재하지 않는다면
# if count == 0:
#     print(-1)
# else:
#     print(count)



