# 풍선 터트리기
def solution(a):
    answer = 0
    rem = [0 for i in range(len(a))]

    def binary_search(line, cnt):
        left = 0
        right = cnt

        index = 0
        while left <= right:
            mid = (left + right) // 2
            if lis[mid] > line:
                right = mid - 1
                index = mid
            else:
                left = mid + 1
        lis[index] = line

        return index

    cnt = 1
    lis = [a[0]]

    r_index = 0
    rem[r_index] = 1
    for line in a[1:]:
        r_index += 1
        if lis[-1] < line:
            lis.append(line)
            cnt += 1
            rem[r_index] = cnt
        else:
            rem[r_index] = binary_search(line, cnt) + 1

    min = int(1e9)
    for r in rem[::-1]:
        # print(r)
        if min > r:
            answer+=1
            min = r
        elif r == 1:
            min = 1
            answer+=1
    print(rem)
    return answer

print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
print(solution([7,10,-13,21,-98,100,102]))
print(solution([1,2,3,4,5,6]))