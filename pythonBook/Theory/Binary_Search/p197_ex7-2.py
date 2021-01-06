# 부품 찾기
# 시간 제한 : 1초 / 메모리 제한 : 128MB
## 책에서 푼 방법(1)(이진 탐색) ##
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         # 찾은 경우 중간점 인덱스 변환
#         if array[mid] == target:
#             return mid
#         # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
#         elif array[mid] > target:
#             end = mid - 1
#         # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
#         else:
#             start = mid + 1
#     return None
#
# n = int(input())
# array = list(map(int,input().split()))
# array.sort()    # 이진 탐색을 수행하기 위해 사전에 정렬 수행
#
# m = int(input())
# x = list(map(int,input().split()))
#
# # 손님이 확인 요청한 부품 번호를 하나씩 확인
# for i in x:
#     # 해당 부품이 존재하는지 확인
#     result = binary_search(array,i,0,n-1)
#     if result != None:
#         print('yes', end=' ')
#     else:
#         print('no',end=' ')

## 책에서 푼 방법(2)(Count Sort) ##
# n = int(input())
# array = [0] * 1000000
#
# # 가게에 있는 전체 부품 번호를 입력받아서 기록
# for i in input().split():
#     array[int(i)] = 1
#
# m = int(input())
# x = list(map(int,input().split()))
#
# for i in x:
#     if array[i] == 1:
#         print('yes', end=' ')
#     else:
#         print('no',end=' ')

## 책에서 푼 방법(3)(set() 함수) ##
n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
array = set(map(int,input().split()))

m = int(input())
x = list(map(int,input().split()))

for i in x:
    if i in array:
        print('yes',end=' ')
    else:
        print('no',end=' ')


## 내가 푼 방법 ##
# N = int(input())
# items = list(map(int,input().split()))
# M = int(input())
# clients = list(map(int,input().split()))
#
# for i in clients:
#     if i in items:
#         print("yes",end=' ')
#     else:
#         print("no",end=' ')