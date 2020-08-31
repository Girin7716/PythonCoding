# 떡볶이 떡 만들기
# 1<=N<=1,000,000 / 1<=M<=2,000,000,000 / 시간 제한 : 2초
## 책에서 푼 방법 ##
n,m = list(map(int,input().split(' ')))
array = list(map(int,input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while(start<=end):
    total = 0
    mid = (start+end)//2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

print(result)

## 내가 푼 방법 ##
# N,M=map(int,input().split())
# heights = list(map(int,input().split()))
#
# heights.sort(reverse=True)
#
# for i in range(N):
#     sum = 0
#     rem = heights[i]
#     for j in range(0,i):
#         sum += heights[j] - rem
#     if sum >= M:
#         print(heights[i])
#         break