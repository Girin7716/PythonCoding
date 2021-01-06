# 전자레인지
# A : 300초, B: 60초, C: 10초

T = int(input())

def solution(T):
    a,b,c=0,0,0
    while T>=0:
        if T%300==0:
            print(a+(T//300),b,c)
            return
        elif T>300:
            a+=1
            T-=300
            continue
        if T%60==0:
            print(a,b+(T//60),c)
            return
        T -= 10
        c+=1

    print('-1')
    return


solution(T)