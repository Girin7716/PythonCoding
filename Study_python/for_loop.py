for x in range(6):
    print(x)
else:
    print('for loop is finished\n')

# 기본적인 nested loop 중첩 반복문
nums = [1, 2, 3]
strings = ['a', 'b', 'c']

for num in nums:
    for str in strings:
        print(num, str)
else:
    print('nested loop is finished\n')

# while
i = 1
while i <= 6:
    print(i)
    i += 1
else:
    print('while loop is finished\n')


# function
def printName(name):
    print('Hello, ' + name)


printName('dg')

# for loop 연습
# 주석 : ctrl + /
# 현재소스 실행 : ctrl+shift+F10
# Break point 후
# shift+F9 한 후 한줄씩 실행 : F8
# 함수로 이동 : F7
# 경고 밑줄 -> alt + enter => enter
