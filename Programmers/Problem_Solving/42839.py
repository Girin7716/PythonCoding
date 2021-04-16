# 소수 찾기
from itertools import permutations

def prime_list(n):
    # 에라토스테네스의 체 초기화 : n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n  #sieve : 체

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2,m+1):
        if sieve[i] == True:    # i가 소수인 경우
            for j in range(i+i,n,i):    #i 이후 i의 배수들을 False로 판정
                sieve[j] = False
    # 소수 목록 산출
    return {i : True for i in range(2,n) if sieve[i] == True}
    # return [i for i in range(2,n) if sieve[i] == True]

def solution(numbers):
    answer = 0

    primeDict = prime_list(10**len(numbers))

    for i in range(1,len(numbers)+1):
        for p in (permutations(numbers,i)):
            num = int(''.join(p))
            if num in primeDict and primeDict[num] is True:
                primeDict[num] = False
                answer+=1

    return answer

print(solution("17"))
print(solution("011"))