def sol(n: int) -> int:
    if n==1:
        return 0
    
    sieve = [1]*(n+1)
    for i in range(4, n+1, 2):
        sieve[i] = 0
    primes = [2]

    for i in range(3, n+1, 2):
        if sieve[i]:
            primes.append(i)
            if i <= int(pow(n,0.5)):
                for j in range(pow(i,2), n+1, i*2):
                    sieve[j] = 0

    i = j = sum_ij = cnt = 0
    len_primes = len(primes)
    while j <= len_primes:
        if sum_ij == n:
            cnt += 1
            if j == len_primes:
                break
            sum_ij += (primes[j]-primes[i])
            i += 1; j += 1
        elif sum_ij < n:
            if j == len_primes:
                break
            sum_ij += primes[j]
            j += 1
        else:
            sum_ij -= primes[i]
            i += 1

    return cnt


print(sol(int(input())))
