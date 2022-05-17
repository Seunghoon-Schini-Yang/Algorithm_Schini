def sol(n: int, k: int) -> int:
    ans = 0
    memo = [0]*(n-1)
    memo[0] = 1
    for i in range(k-1):
        temp = [0]*(n-1)
        acc = 0
        for j in range(i*2 + 2, n-1):
            acc += memo[j-2]
            temp[j] += acc
        memo = temp
    
    ans += sum(memo)

    memo = [1]*n
    memo[0] = 0
    for i in range(k-1):
        temp = [0]*n
        acc = 0
        for j in range(i*2 + 3, n):
            acc += memo[j-2]
            temp[j] += acc
        memo = temp

    ans += sum(memo)

    return ans%1_000_000_003


print(sol(int(input()), int(input())))
