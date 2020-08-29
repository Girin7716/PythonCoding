# Insertion Sort(삽입 정렬)
# Time Complexity : O(N^2)
# 정렬이 거의 되어있는 데이터 셋에서는 빠르다
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
        else:
            break

print(array)