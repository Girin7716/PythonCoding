# set = 집합 자료형
s1 = set([1, 2, 3])
print(s1)

s2 = set("Hello")
print(s2)

# set의 특징
# 1.중복을 허용하지 않는다 2.순서가 없다 == indexing 값을 얻을 수 없다(dictionary와 비슷)
# 만약 set 자료형에 저장된 값을 인덱싱으로 접근하려면 list나 tuple로 변환후 접근해야 한다

# set을 list나 tuple로 변환
l1 = list(s1)
print(l1)
print(l1[0])

t1 = tuple(s1)
print(t1)
print(t1[2])

# 교집합, 합집합, 차집합 구하기
s3 = set([1, 2, 3, 4, 5, 6])
s4 = set([4, 5, 6, 7, 8, 9, ])

print(s3 & s4)  # 교집합
print(s3.intersection(s4))  #intersection함수 = 교집합
print()

print(s3 | s4)  # 합집합
print(s3.union(s4)) # union함수 == 합집합
print()

print(s3-s4)    # 차집합
print(s3.difference(s4))    #difference함수 == 차집합
print()

# set 관련 함수들
s1.add(4)   # set 자료형에 값 추가
print(s1)
print()

s1.update([5,6,7])  # set 자료형에 값 여러개 추가하기
print(s1)
print()

s1.remove(3)    # set 자료형에 특정 값 제거하기
print(s1)