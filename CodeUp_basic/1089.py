#[기초-조합] 수 나열하기1

def solution(a,d,n):
    for i in range(n-1):
        a+=d
    print(a)


a,d,n = input().split()
a=int(a)
d=int(d)
n=int(n)

solution(a,d,n)