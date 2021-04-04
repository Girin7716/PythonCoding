def solution(clothes):
    answer = 1
    clothes_dict = {}

    for c in clothes:
        clothes_dict[c[1]] = clothes_dict.get(c[1],[])+[c[0]]

    for key in clothes_dict.keys():
        answer = answer * (len(clothes_dict[key]) + 1)
    return answer - 1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
print(solution([["a", "face"], ["b", "face"],
                ["c", "up"],["d", "up"],
                ["e", "down"],["f", "down"]]))

# 1 : a b
# 2 : c d
# 3 : e f

# a,b,c,d,e,f => 3C1 2C1
# ac/ad/ae/af/bc/bd/be/bf/ce/cf/de/df  => 3C2 2C1 2C1
# ace/acf/ade/aef/bce/bcf/bde/bdf => 3C3 2C1 2C1 2C1 = 8