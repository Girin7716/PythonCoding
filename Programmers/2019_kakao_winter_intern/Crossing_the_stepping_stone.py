def solution(stones, k):
    min = 1
    max = 200000000

    while min < max-1:
        mid = (min+max)//2
        cnt = 0

        for s in stones:
            if s <=mid: # mid명은 못건넌다
                cnt +=1
                if cnt>=k:
                    max = mid
                    break
            else:
                cnt = 0
        if max != mid:
            min = mid

    return max

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))



# 정확성 o, 효율성 x
# def solution(stones, k):
#     lengths = len(stones)
#
#     answer = int(1e9)
#     for i in range(lengths - k + 1):
#         m = max(stones[i:i + k])
#         if answer > m:
#             answer = m
#
#     return answer