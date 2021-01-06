def solution(n,check):
    for i in range(1,len(check)+1):
        print(check[-i],end=" ")

n = int(input())
check = list(map(int,input().split()))

solution(n,check)