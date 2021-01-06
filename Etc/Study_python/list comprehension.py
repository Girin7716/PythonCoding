# 리스트 컴프리헨션

# 1부터 10까지 정수를 순서대로 가지고 있는 리스트
numbers = [x for x in range(10)]
print(numbers)
print()

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 이만큼의 코드를
result = []
for i in a:
    if i % 2 == 1:
        result.append(i)
print(result)
print()

# 이만큼으로 줄일 수 있다
result2 = [x for x in a if x % 2 == 1]
print(result2)
print()

# ex>
b = [1, 2, 3, 4, 5]
result_b = [2 * x for x in b]
print(result_b)
print()

# 중첩 표현
meal = ['soup', 'chicken', 'hamburger']
dessert = ['apple', 'icecream', 'coffee']

result_c = [(x, y) for x in meal for y in dessert]
print(result_c)
print()

# pprint를 사용하면 예쁘게 출력 됨
import pprint

pp = pprint.PrettyPrinter()
pp.pprint(result_c)
