# Quick Sort(퀵 소트)
# Time Complexity : O(NlogN)

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start >= end:    # 원소가 1개인 경우 종류
        return
    pivot = start
    left = start + 1
    right = end
    while left<= right:
        # pivot보다 큰 데이터를 찾을 때까지 반복
        while left<= end and array[left] <= array[pivot]:
            left += 1
        # pivot보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right :   # 교차한다면 작은 right -= 1 데이터와 pivot 교체
            array[right],array[pivot] = array[pivot],array[right]
        else: # 교차하지 않는다면 작은 데이터와 큰 데이터 교체
            array[left],array[right] = array[right],array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정령 수행
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)