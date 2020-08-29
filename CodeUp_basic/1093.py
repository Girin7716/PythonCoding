def solution(n,stu_check):
    student = [0 for _ in range(1,25)]
    for i in range(n):
        student[stu_check[i]]+=1
    for i in range(1,len(student)):
        print(student[i],end=" ")


n = int(input())
student_check = list(map(int,input().split()))

solution(n,student_check)
