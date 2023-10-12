def main():
    n = int(input())
    if n <= 1:
        print(0)
    else:
        memo = [0] * (n+1)
        memo[0], memo[2] = 1, 3
        for i in range(4, n+1, 2):
            memo[i] += memo[i-2] * 3
            cur = 4
            while 0 <= i-cur:
                memo[i] += memo[i-cur] * 2
                cur += 2
        print(memo[n])


if __name__ == '__main__':
    main()
