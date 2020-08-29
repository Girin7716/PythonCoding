# 문자열 만들기 #
# 1."~~~~"  -> 문자열에 작은따옴표(') 포함시키기
food = "Python's favorite food is perl\n"
print(food)
# 2.'~~~~'  -> 문자열에 큰따옴펴(") 포함시키기
say = '"Python is ver easy." he says\n'
print(say)
# 3."""~~~~~~~~~~~~~~~"""   ->여러 줄인 문자열을 변수에 대입하고 싶을 때
multiline = '''
Life is too short
You need python
'''
print(multiline)
# 4.'''~~~~~~~~~~~~~~~'''
multiline2 = '''
    Life is too long
I need python
'''
print(multiline2)

# 문자열 연산 #
# 1.문자열 더해서 연결하기
head = 'Python'
tail = ' is fun!'
print(head + tail)
# 2.문자열 곱하기
a = "python"
print(a * 2)
print()
# 3.문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)
print()
# 4.문자열 길이 구하기
a = "Life is too short"
print(len(a))
print()

# 문자열 인덱싱과 슬라이싱 #
# indexing == 가리킨다 / slicing == 잘라낸다 #
# 문자열 인덱싱
a = "Life is too short, You need Python"
print(a[19])
print(a[-1])  # 제일 뒷 문자 / -는 뒤에서부터 접근
print()
# 문자열 슬라이싱 -> 한 문자가 아닌 단어를 뽑아내기
a = "Life is too short, You need Python"
print(a[0:4])
print(a[0:3])
print(a[5:7])
print(a[12:17])
print(a[:17])  # 처음부터 17까지
print(a[19:])  # 19부터 끝까지
print(a[:])  # 시작부터 끝까지
print(a[19:-7])  # a[19]에서 a[-8]까지
print()
# 슬라이싱을 문자열 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)
print()

# 문자열 포매팅 따라 하기 #
# 1.숫자 바로 대입
print("I eat %d apples." % 3)
print()
# 2.문자열 바로 대입
print("I eat %s apples." % "five")
print()
# 3.숫자 값을 나타내는 변수로 대입
number = 4
print("I eat %d apples." % number)
print()
# 4.2개 이상의 값 넣기
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days" % (number, day))
print()

# format 함수를 사용한 포매팅 #
# 문자열의 format 함수를 사용하면 좀 더 발전된 스타일로 문자열 포맷을 지정할 수 있다.
# 1.숫자 바로 대입하기
print("I eat {0} apples".format(3))
print()
# 2.문자열 바로 대입하기
print("I eat {0} apples".format("five"))
print()
# 3.숫자 값을 가진 변수로 대입하기
number = 4
print("I eat {0} apples".format(number))
print()
# 4.2개 이상의 값 넣기
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days".format(number, day))
print()
# 5.이름으로 넣기
print("I ate {number} apples. so I was sick for {day} days".format(number=10, day=3))
print()
# format 함수에는 반드시  name = value 형태로 와야한다

# 6. 인덱스와 이름을 혼용해서 넣기
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))
print()
# 7.왼쪽 정렬 :<
print("{0:<10}".format("hi"))
print()
# 8.오른쪽 정렬 :>
print("{0:>10}".format("hi"))
print()
# 9.가운데 정렬 :^
print("{0:^10}".format("hi"))
print()
# 10.공백 채우기 :와 (>,<,^) 사이에 넣기
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))
print()
# 11.소수점 표현하기
y = 3.42134234
print("{0:0.4f}".format(y))
print()

# 문자열 관련 함수들 #
# 1.문자 개수 세기(count)
a = "hobby"
print(a.count('b'))
print()
# 2.위치 알려주기1(find)
a = "Python is the best choice"
print(a.find('b'))  # 있으면 나온 위치
print(a.find('k'))  # 없으면 -1
print()
# 3.문자열 삽입(join)
print(",".join('abcd'))  # abcd 문자열 각각 사이에 ','를 삽입
print(",".join(['a', 'b', 'c', 'd']))  # 리스트나 튜플도 입력으로 사용 가능
print()
# 4.소문자를 대문자로 바꾸기(upper)
a = "hi, I'm Kihyun"
print(a.upper())
print()
# 5.대문자를 소문자로 바꾸기(lower)
a = "hi, I'm Kihyun"
print(a.lower())
print()
# 6.왼쪽 공백 지우기(lstrip)
a = "      hi     "
print(a.lstrip())
# 7.오른쪽 공백 지우기(rstrip)
print(a.rstrip())
print()
# 8.문자열 바꾸기(replace)
a = "Life is too short"
print(a.replace("Life", "Your leg"))
print()
# 9.문자열 나누기(split) ->문자열이 리스트가 된다
a = "Life is too short"
print(a.split())    # split안에 아무 것도 넣어주지 않으면 공백(space, tab, enter) 기준
b = "a:b:c:d"
print(b.split(':')) # split안 문자를 구분자로 나눈다
print()
