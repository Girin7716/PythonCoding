def solution(a,r,n):
    for i in range(n-1):
        a*=r
    print(a)

a,r,n = input().split()
a=int(a)
r=int(r)
n=int(n)

solution(a,r,n)