# 소수의 연속합
N = int(input())

def prime_list(n):
    sieve = [True] * n

    m = int(n**0.5)
    for i in range(2,m+1):
        if sieve[i] == True:
            for j in range(i+i,n,i):
                sieve[j] = False
    return [i for i in range(2,n) if sieve[i] == True]

prime = prime_list(N+1)

#print(prime)

start = 0
end = 0
goal = N
result = 0
plen = len(prime)
while start <= plen and end <= plen:
    now = sum(prime[start:end+1])
    if goal > now:
        end += 1
    elif goal < now:
        start += 1
    else:
        result += 1
        start += 1
        end += 1

print(result)