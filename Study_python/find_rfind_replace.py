# find, rfind, replace

# list에서 원하는 값의 index찾기(첫 등장)
a = [1, 2, 3, 4, 3, 5]

print(a.index(3))
print()

# string에서 원하는 값 찾기
b = 'my love my love'

print(b.find('y'))  # 처음으로 발견한 'y'의 index 반환
print(b.rfind('y'))  # 맨 뒤에서 처음으로 발견한 'y'의 index 반환
print()

# replace 원본은 바꾸지 않고, replace한 결과를 리턴
replaced = b.replace('my', 'your')

print(replaced)
print(b)
print()

# 바꿀 횟수를 정해줄 수 있다
replaced_once = b.replace('my', 'your', 1)  # 한 번만 바꾸기
print(replaced_once)
