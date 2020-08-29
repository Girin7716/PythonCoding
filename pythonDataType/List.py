## 리스트 ##
# 리스트 만들기 #
# 리스트먕 = [요소1,요소2,요소3 ...]
a = []  # 비어 있는 리스트
b = [1, 2, 3]  # 숫자로만 이루어진 리스트
c = ['Life', 'is', 'too', 'short']  # 문자열로만 이루어진 리스트
d = [1, 2, 'Life', 'is']  # 숫자와 문자열 함께 이루어진 리스트
e = [1, 2, ['Life', 'is']]  # 리스트 자체를 요솟 값으로 가질 수도 있다
print(a, b, c, d, e)
print()

# 리스트의 인덱싱과 슬라이싱 #
# 리스트의 인덱싱
a = [1, 2, 3]
print(a)
print(a[0] + a[2])
print()

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3])
print(a[:])
print(a[-1][0])  # 요소인 리스트의 요소 출력
print()
# 리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2])  # 리스트 슬라이싱
a = "12345"
print(a[0:2])  # 문자열 슬라이싱
print()

a = [1, 2, 3, 4, 5]
b = a[:2]  # 리스트를 슬라이싱하면 리스트다
c = a[2:]
print(b)
print(c)
print()

# 중첩된 리스트에서 슬라이싱하기
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])  # 중첩된 리스트에서 슬라이싱하기

# 리스트 연산하기 #
# 리스트 더하기 (+)
a = [1, 2, 3]
b = ['a', 'b', 'c']
print(a + b)
print()
# 리스트 반복하기(*)
a = [1, 2, 3]
print(a * 3)
print()
# 리스트 길이구하기
a = [1, 2, 3]
print(len(a))
print()
# 리스트 + 할때 형을 맞춰야한다
# ex>
a = [1, 2, 3]
# print(a[2]+"hi") -> 오류 int와 string 서로 못더해서
print(str(a[2]) + "hi")
print()

# 리스트의 수정과 삭제 #
# 리스트에서 값 수정하기
a = [1, 2, 3]
a[2] = 4
print(a)
print()
# del 함수 사용해 리스트 요소 삭제 (파이썬 내장 함수)
a = [1, 2, 3]
# del(a[1]) -> 이거도 됨
# del 객체(=파이썬에서 사용되는 모든 자료형)
del a[1]
print(a)
print()
# 슬라이싱 기법을 사용하여 리스트 요소 여러 개 삭제
a = [1, 2, 3, 4, 5]
del a[:2]
print(a)

# 리스트 관련 함수들 #
# 리스트에 요소 추가(append)
a = [1, 2, 3]
a.append(4)
print(a)
a.append([5, 6])  # 리스트도 append가 된다
print(a)
print()
# 리스트 정렬(sort)
a = [1, 4, 3, 2]  # 문자 순으로 정렬
a.sort()
print(a)

a = ['a', 'c', 'b']  # 알파벳 순서로 정렬
a.sort()
print(a)
print()
# 리스트 뒤집기(reverse)
a = ['a', 'c', 'b']
a.reverse()
print(a)
print()
# 위치 변환(index) -> 리스트에 x 값이 있으면 x의 위치값을 알려줌
a = [1, 2, 3]
print(a.index(3))
print(a.index(1))
print()
# 만약 없을경우 오류
# 리스트에 요소 삽입(insert)
# insert(a,b) 리스트의 a번째 위치에 b를 삽입
a = [1, 2, 3]
a.insert(0, 4)
print(a)
a.insert(3, 5)
print(a)
print()
# 리스트 요소 제거(remove)
# remove(x) 첫 번째로 나오는 x 삭제
a = [1, 2, 3, 1, 2, 3, ]
a.remove(3)
print(a)
a.remove(3)
print(a)
print()
# 리스트 요소 끄집어내기(pop)
a = [1, 2, 3]
print(a.pop())  # 리스트의 맨 마지막 요소를 돌려주고 그 요소 삭제
print(a)
print()

a = [1, 2, 3]
print(a.pop(1))  # 리스트의 index 1을 돌려주고 그 요소 삭제
print(a)
print()
# 리스트에 포함된 요소 x의 개수 세기(count)
a=[1,2,3,1,5,1]
print(a.count(1))
print()
# 리스트 확장(extend)
#extend(x)에서 x에는 리스트만 올 수 있으며 원래의 a 리스트에 x 리스트를 더하게 된다
a = [1,2,3]
a.extend([4,5]) # a+=[4,5]와 동일
print(a)
b = [6,7]
a.extend(b)
print(a)
