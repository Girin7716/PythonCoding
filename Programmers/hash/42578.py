# 위장
def solution(clothes):
    answer = 0
    dic = {}

    for p in clothes:
        try:
            dic[p[1]].append(p[0])
        except:
            dic[p[1]] = dic.get(p[1], [p[0]])



    return answer

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))

# [[yellow_hat, headgear], [blue_sunglasses, eyewear], [green_turban, headgear]]	5
# [[crow_mask, face], [blue_sunglasses, face], [smoky_makeup, face]]	3