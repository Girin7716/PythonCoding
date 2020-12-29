# 국영수 / p359 / 정렬
# 이름, 국어, 영어, 수학
# 책에서 푼 방법
n = int(input())
students = []

for _ in range(n):
    students.append(input().split())

students.sort(key=lambda x:(-int(x[1]),int(x[2]),-(int(x[3])),x[0]))

for student in students:
    print(student[0])


# 내가 푼 방법
# N = int(input())
# data = []
# for i in range(N):
#     name, korean, english, math = input().split()
#     data.append([name,int(korean),int(english),int(math)])
#
# #f = sorted(e, key = lambda x : (x[0], -x[1]))
# data.sort(key=lambda x : (-x[1], x[2], -x[3],x[0]))
# for i in range(N):
#     print(data[i][0])
# input
# 12
# Junkyu 50 60 100
# Sangkeun 80 60 50
# Sunyoung 80 70 100
# Soong 50 60 90
# Haebin 50 60 100
# Kangsoo 60 80 100
# Donghyuk 80 60 100
# Sei 70 70 70
# Wonseob 70 70 90
# Sanghyun 70 70 80
# nsj 80 80 80
# Taewhan 50 60 90