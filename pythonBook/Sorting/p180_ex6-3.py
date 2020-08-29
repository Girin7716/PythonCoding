# 성적이 낮은 순서로 학생 출력하기
## 책에서 푼 방법 ##
n=int(input())

array = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로 ,점수는 정수형으로 변환하여 저장
    array.append((input_data[0],int(input_data[1])))

# 키를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0],end=' ')

## 내가 푼 방법 ##
# N = int(input())
#
# students = []
# for i in range(N):
#     student = list(input().split())
#     student[1] = int(student[1])
#     students.append(student)
#
# def setting(data):
#     return data[1]
#
# students.sort(key=setting)
# for i in students:
#     print(i[0],end=' ')