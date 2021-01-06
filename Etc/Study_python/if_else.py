# if-else도 한줄로

# 그냥 input으로 받으면 string으로 받아진다
a = int(input('숫자 입력 : '))

# 이것을
if a > 7:
    print('yes')
else:
    print('no')
print()

# 이렇게 한줄로 줄일 수 있다
print('yes') if a > 7 else print('no')
