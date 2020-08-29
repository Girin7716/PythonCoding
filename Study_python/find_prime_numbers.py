# 문제> 소수 찾기
# 1부터 n 사이에 있는 소수의 갯수를 반환하는 함수 solution 작성

# 간단하게 생각하면
def solution(n):
    a = [False, False] + [True] * (n - 1)

    primes = []

    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False
    print(primes)


# solution 함수 코드 줄여보기
def short_solution(n):
    # 2부터 입력받은 n까지 숫자를 갖는 'set'을 만든다
    n_list = set([num for num in range(2, n + 1)])

    # n_list는 계속 바뀔거기 때문에, range(2,n+1)을 기준으로 for문을 돌린다
    for i in range(2, n + 1):
        if i in n_list:  # list가 아닌 set이기 때문에 요걸 해도 i를 탐색하는 것이 부담스럽지 않다.
            # range(a,b,c) -> a: range 시작 범위 / b: range 마지막 범위 / c: range 간격 지정(생략==1)
            n_list -= set([i for i in range(i * 2, n + 1, i)])
            # i에 해당하는 지워야 할 것들을 집합으로 만들어서 n_list에서 차집합 시행으로 없애준다다
    print(n_list)


solution(100)
short_solution(100)
