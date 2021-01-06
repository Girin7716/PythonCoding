def solution(a,m,d,n):
    for i in range(n-1):
        a=(a*m)+d
    print(a)
a,m,d,n = input().split()

a=int(a)
m=int(m)
d=int(d)
n=int(n)

solution(a,m,d,n)